from flask import Flask
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path
from flask_login import LoginManager
from werkzeug.security import generate_password_hash, check_password_hash


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "TPYfvwikxqxYrtPNOXTTHyTO00E0Y05Y"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    

    

    
    with app.app_context():
        db.create_all()
    
            
    return app
 

        
    
    
