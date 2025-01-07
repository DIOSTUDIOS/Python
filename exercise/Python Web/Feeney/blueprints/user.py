from flask import Blueprint, render_template


user = Blueprint('user', __name__, url_prefix='/')
@user.route('/register')
def register():
    return render_template('register.html')
