from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect

db = SQLAlchemy()
bootstrap = Bootstrap()
csrf = CSRFProtect()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    print(f"DB path: {app.config['SQLALCHEMY_DATABASE_URI']}")  # Выведет путь
    
    db.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    
    from .routes import bp  # Важно: относительный импорт (с точкой)
    app.register_blueprint(bp)
    
    return app
