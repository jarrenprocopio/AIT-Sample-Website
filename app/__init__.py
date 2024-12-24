        # app/__init__.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from authlib.integrations.flask_client import OAuth

# Initialize SQLAlchemy and OAuth
db = SQLAlchemy()
oauth = OAuth()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize SQLAlchemy and OAuth
    db.init_app(app)
    oauth.init_app(app)

    # Import routes inside the app context
    with app.app_context():
        from . import routes  # Import the routes only after app is initialized
    
    app.discord = oauth.register(
        name='discord',
        client_id=app.config['DISCORD_CLIENT_ID'],
        client_secret=app.config['DISCORD_CLIENT_SECRET'],
        authorize_url='https://discord.com/api/oauth2/authorize',
        access_token_url='https://discord.com/api/oauth2/token',
        redirect_uri=app.config['DISCORD_REDIRECT_URI'],
        client_kwargs={'scope': 'identify email'}
    )
    
    return app
