from flask import Flask
from exts import db
from blueprints.cms import cms as cms_bp
from blueprints.front import front as front_bp
from blueprints.user import user as user_bp
from flask_migrate import Migrate
from models import user

import config
import commands

app = Flask(__name__)
app.config.from_object(config.DevelopmentConfig)
app.register_blueprint(cms_bp)
app.register_blueprint(front_bp)
app.register_blueprint(user_bp)

db.init_app(app)

migrate = Migrate(app, db)

app.cli.command('create-permission')(commands.create_permission)
app.cli.command('create-role')(commands.create_role)
app.cli.command('create-test-user')(commands.create_test_user)
app.cli.command('create-admin')(commands.create_admin)


@app.route('/')
def index():
    return 'Hello, Flask !'


if __name__ == '__main__':
    app.run()
