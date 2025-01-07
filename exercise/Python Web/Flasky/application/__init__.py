from flask import Flask
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy

import os


app = Flask(__name__)
app.config['SECRET_KEY'] = 'DC3Iw7c6e!cZvD5H'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.dirname(app.root_path), 'database.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)

moment = Moment(app)

db = SQLAlchemy(app)

from application import views
