from flask import Flask, request, redirect, url_for, render_template, flash
from flask_login import LoginManager, current_user, login_user
import psycopg2

from user import User
from login_form import LoginForm


connection = psycopg2.connect(host='localhost',
                              database='postgres',
                              port=5432,
                              user='postgres',
                              password='postgres')


app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
login = LoginManager(app)


@login.user_loader
def load_user(user_id):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM users where users.id = (%s)', (user_id, ))
    person = cursor.fetchone()
    user = User(person[0], person[1], person[2])
    user.is_authenticated = True
    return user

@app.route('/')
def hello_world():
    print(request)
    return '<b>Hello, World!</b>'


@app.route('/folder1/index.html')
def index():
    return '<b>Ha ha!</b>'


@app.route('/user/<int:user_id>/<str:text>')
def user_info(user_id):
    cursor = connection.cursor()
    cursor.execute(f'SELECT * FROM users where users.id = (%s)', (user_id, ))
    connection.commit()
    person = cursor.fetchone()
    if person is not None:
        return f"""
    Username: {person[1]},
    Name: {person[2]}
        """
    return 'User not found'


@app.route('/user/<int:user_id>/status')
def user_status(user_id):
    if user_id == 300:
        user = {'username': 'Miguel'}
        return '''
        <html>
            <head>
                <title>Home Page - Microblog</title>
            </head>
            <body>
                <h1>Hello, ''' + user['username'] + '''!</h1>
            </body>
        </html>'''
    else:
        return '<b>Юзеру немає чого переживати!</b>'

@app.route('/login', methods=['GET', 'POST'])
def login():
    method = request.method
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        cursor = connection.cursor()
        cursor.execute(f'SELECT id, username, name, password_hash FROM users where users.username = (%s)', (form.username.data,))
        user_data = cursor.fetchone()
        user = User(user_data[0], user_data[1], user_data[2])
        user.password_hash = user_data[3]
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(f'/user/{user.id}')
    return render_template('index.html', title='Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='5000')