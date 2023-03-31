from flask import Blueprint, render_template, redirect, url_for, jsonify, request
from flask_login import login_required, current_user
from datetime import datetime
from .models import Note, User




views = Blueprint("views", __name__) 

@views.route("/", methods=['GET', 'POST'])
@login_required
def home():
    


    return render_template("main.html")
