from flask import Flask
from application.index.views import indexPage
from application.exporter.views import exporterPage
from application.importer.views import importerPage


def create_app():
    app = Flask(__name__)

    register_blueprints(app)

    return app


def register_blueprints(app):
    app.register_blueprint(indexPage)
    app.register_blueprint(exporterPage)
    app.register_blueprint(importerPage)

    pass
