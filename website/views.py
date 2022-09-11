from unicodedata import category
from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Certificate
from . import db

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        certificate = request.form.get('certificate')
        if len(certificate) < 1:
            flash('Text is too short!', category='error')
        else:
            new_certificate = Certificate(title=certificate, user_id=current_user.id)
            db.session.add(new_certificate)
            db.session.commit()
    return render_template("home.html", user=current_user)