# config.py
import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "your_secret_key"
    DISCORD_CLIENT_ID = "1257844214503571496"
    DISCORD_CLIENT_SECRET = "h1YeRB4zpS37bMoEqNzpXrvBGmEN1NIP"
    DISCORD_REDIRECT_URI = "http://127.0.0.1:5000/callback"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False