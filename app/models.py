# app/models.py
from datetime import datetime
from . import db  # Import db from your app

class User(db.Model):
    id = db.Column(db.String(50), primary_key=True)  # Discord user ID
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    outprocessing_progress = db.Column(db.Float, default=0.0)  # Progress can be a float (0.0 to 100.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<User {self.username}#{self.discriminator}>'
