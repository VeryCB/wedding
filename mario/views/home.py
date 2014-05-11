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

from mario.forms import EmailSignupForm, LoginForm
from mario.models.user import User


bp = Blueprint('home', __name__, url_prefix='/')


@bp.route('signup/', methods=['GET', 'POST'])
def signup():
    next_ = request.args.get('next') or url_for('.index')

    if current_user.is_authenticated():
        return redirect(next_)

    form = EmailSignupForm()

    if form.validate_on_submit():
        email = form.data['email'].encode('utf-8')
        name = form.data['name'].encode('utf-8')
        password = form.data['password'].encode('utf-8')

        user = User.add(email=email, name=name)
        user.password = password
        login_user(user, force=True)

        return redirect(next_)

    return render_template('home/signup.html', form=form)


@bp.route('/', methods=['GET', 'POST'])
@bp.route('login/', methods=['GET', 'POST'])
def index():
    if current_user.is_authenticated():
        return render_template('home/index.html', user=current_user)

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
