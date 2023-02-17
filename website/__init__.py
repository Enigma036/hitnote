from flask import Flask
from sqlalchemy import desc
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from os import path


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "TPYfvwikxqxYrtPNOXTTHyTO00E0Y05Y"
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_NAME}"
    db.init_app(app)
    

    from .views import views
    from .messages import messages
    from .programmer import programmer
    
    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(messages, url_prefix="/")
    app.register_blueprint(programmer, url_prefix="/")
    
    from .models import User, Note
    
    with app.app_context():
        db.create_all()
    
            
    return app
 
def create_first_user():
    from .models import User, Note
    if User.query.count() == 0:
        new_programmer = User(jmeno = "Můj účet")
        db.session.add(new_programmer)
        db.session.commit()
        

        
    
    
