import os
from pathlib import Path

basedir = Path(__file__).parent
instance_path = basedir / "instance"
os.makedirs(instance_path, exist_ok=True)  # Создаст папку, если её нет

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-123'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        f'sqlite:///{instance_path/"climate.db"}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_SERVE_LOCAL = True