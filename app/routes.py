from flask import redirect, render_template, url_for, request, jsonify, session, current_app as app
from flask_login import login_required, current_user
from app import db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/tracker")
def tracker():
    return render_template("tracker.html")

@app.route('/login')
def login():
    return app.discord.authorize_redirect(redirect_uri=app.config['DISCORD_REDIRECT_URI'])

@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('index'))

@app.route('/save_progress', methods=['POST'])
@login_required
def save_progress():
    data = request.get_json()
    progress = data.get('progress', 0)

    # Update user's progress in the database
    current_user.outprocessing_progress = progress
    db.session.commit()
    
    return jsonify({'message': 'Progress saved successfully.'}), 200

@app.route('/callback')
def callback():
    # Get the user's information from Discord
    token = app.discord.authorize_access_token()
    user_data = app.discord.get('https://discord.com/api/users/@me').json()

    user_id = user_data['id']
    username = user_data['username']
    email = user_data.get('email')  # Email may not be provided

    # Check if the user already exists in the database
    user = User.query.get(user_id)
    
    if not user:
        # Create new user if they don't exist
        user = User(id=user_id, username=username, email=email)
        db.session.add(user)
        db.session.commit()  # Commit to save the new user
    
    # Store user data in session
    session['user'] = user_data
    
    # Redirect to the profile page
    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    user = session.get('user')
    if user:
        return render_template('profile.html', user=user)
    return redirect(url_for('login'))
