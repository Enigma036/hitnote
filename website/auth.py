from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from website import create_first_user
from . import db
from flask_login import login_user, login_required, logout_user, current_user


auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    create_first_user()
    
    er_succ_message = "Přihlášení"   
    trida = "none"
     
    if request.method == 'POST':
        username = request.form.get('user')
        password = request.form.get('pass')
        check = request.form.get('check')
        
        remember = False
        
        if check:
            if check == "on":
                remember = True
            else:
                remember = False
            

        email = User.query.filter_by(email=username).first()
        user = User.query.filter_by(jmeno=username).first()
        
        if email:
            user = email
        
        if user:
            if check_password_hash(user.password, password):
                er_succ_message = "Úspěšné přihlášení"   
                trida = "success" 
                login_user(user, remember=remember)
                return redirect(url_for('views.home'))
            else:
                er_succ_message = "Špatné heslo"   
                trida = "error" 
        else:
            er_succ_message = "Váš účet nebyl nalezen"   
            trida = "error" 
            
    return render_template("login_form.html", message = er_succ_message, trida=trida)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
