from app.auth import authentication as at
from app.auth.forms import RegistrationForm
from flask import render_template,request, flash, redirect, url_for
from app.auth.models import User


# @main.route('/')
# def display_books():
# books = Book.query.all()
# return render_template('home.html', books=books)


# @main.route('/display/publisher/<publisher_id>')
# def display_publisher(publisher_id):

# publisher = Publication.query.filter_by(id=publisher_id).first()
# publisher_books = Book.query.filter_by(pub_id=publisher.id).all()

@at.route('/register', methods=['GET', 'POST'])
def register_user():

    form = RegistrationForm()

    if form.validate_on_submit():
        User.create_user(
            user=form.name.data,
            email=form.name.data,
            password=form.password.data
        )
        flash('Registration Successful')
        return redirect(url_for('authentication.login_user'))
    return render_template('registration.html',form=form)


@at.route('/login', methods=['GET','POST'])
def login_user():
    return render_template('login.html')

# return render_template('publisher.html', publisher=publisher, publisher_books=publisher_books)
