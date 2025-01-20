from flask import Blueprint, render_template


indexPage = Blueprint("indexPage", __name__)


@indexPage.route("/")
def index():
    return render_template('index.html')
