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
    app.config['JSON_SORT_KEYS'] = False
    app.config['JSON_AS_ASCII'] = False
    db.init_app(app)
    

    from .views import views
    from .messages import messages
    from .programmer import programmer
    from .auth import auth
    from .import_export import import_export
    from .api import api
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(messages, url_prefix="/")
    app.register_blueprint(programmer, url_prefix="/")
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(import_export, url_prefix='/')
    app.register_blueprint(api, url_prefix='/')
    
    from .models import User, Note
    
    with app.app_context():
        db.create_all()
        
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))
    
            
    return app
 
def create_first_user():
    from .models import User, Note
    if User.query.count() == 0:
        new_programmer = User(jmeno = "admin", email="admin@gmail.com", username="admin", role="Administrátor",password=generate_password_hash("123456"))
        db.session.add(new_programmer)
        db.session.commit()
        

        
    
    
