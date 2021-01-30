from flask import Blueprint, render_template, redirect, url_for, flash
from application.forms.forms import LoginForm


form_sign_in_bp = Blueprint('form_sign_in_bp',
                            __name__,
                            template_folder='templates',
                            static_folder='static')

@form_sign_in_bp.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for the user {}, remember me {}'.format(form.username.data, form.remember_me.data))
        return redirect(url_for('home_bp.index'))
    return render_template('login.html', title='Sign in', form=form)



