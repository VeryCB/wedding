# coding: utf-8

from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
)
from flask.ext.login import (
    login_user,
    current_user,
    logout_user,
    login_required,
)

from mario.forms import  LoginForm


bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('/', methods=['GET'])
def index():
    if current_user.is_authenticated():
        you = u'你们' if current_user > 1 else u'你'
        return render_template('home/index.html', user=current_user, you=you)
    return redirect(url_for('.login'))


@bp.route('login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated():
        return redirect(url_for('.index'))

    form = LoginForm()

    if form.validate_on_submit():
        login_user(form.user, force=True)
        next_ = request.args.get('next') or url_for('.index')
        return redirect(next_)

    return render_template('home/login.html', form=form)


@bp.route('logout/')
@login_required
def logout():
    logout_user()
    return redirect(url_for('.index'))
