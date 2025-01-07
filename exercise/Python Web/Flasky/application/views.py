from application import app
from flask import render_template, session, redirect, url_for, flash
from datetime import datetime
from application.forms import NameForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()

    if form.validate_on_submit():
        oldName = session.get('name')
        if oldName is not None and oldName != form.name.data:
            flash('Looks like you have changed your name !')
        session['name'] = form.name.data
        return redirect(url_for('index'))

    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'))

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')
