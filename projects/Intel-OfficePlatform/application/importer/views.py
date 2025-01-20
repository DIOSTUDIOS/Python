from flask import Blueprint, render_template


importerPage = Blueprint('importerPage', __name__)


@importerPage.route('/importer')
def importer():
    return render_template('importer.html')
