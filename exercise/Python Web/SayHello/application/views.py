from application import app, db
from application.models import Message
from application.forms import HelloForm
from flask import flash, redirect, render_template, url_for


@app.route('/', methods=['GET', 'POST'])
def index():
    messages = Message.query.order_by(Message.timestamp.desc()).all()
    form = HelloForm()

    if form.validate_on_submit():
        name = form.name.data
        body = form.body.data

        message = Message(name=name, body=body)

        db.session.add(message)
        db.session.commit()

        flash('Your Message Have Been Sent To The World !')

        return redirect(url_for('index'))
    return render_template('index.html', form=form, messages=messages)
