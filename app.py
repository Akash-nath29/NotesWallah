#----------NotesWallah-----------#
#------Author: Akash Nath--------#
#-----https://github.com/Akash-nath29----#
#----------------https://akashnath.netlify.app----------------#


from flask import Flask, render_template, request, redirect, session, flash, url_for, send_file, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
# import secrets
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import pytz
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# import json
from os import environ as env
# from urllib.parse import quote_plus, urlencode

# from authlib.integrations.flask_client import OAuth
# from dotenv import find_dotenv, load_dotenv
import pyrebase


# ENV_FILE = find_dotenv()
# if ENV_FILE:
#     load_dotenv(ENV_FILE)

utc_now = datetime.utcnow()
ist_timezone = pytz.timezone('Asia/Kolkata')
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ist_timezone)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.secret_key = "kfwi4f4BEpiOoeninEknk"
app.config['UPLOAD_FOLDER'] = 'static/uploads'

# oauth = OAuth(app)

# oauth.register(
#     "auth0",
#     client_id=env.get("AUTH0_CLIENT_ID"),
#     client_secret=env.get("AUTH0_CLIENT_SECRET"),
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration'
# )

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    musics = db.relationship('Music', backref='author', lazy=True)
    profile_picture = db.Column(db.String(255), default='static/img/default.png')

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    file_description = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=False)
    posted_at = db.Column(db.DateTime, default=ist_now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

class Music(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    music_link = db.Column(db.String(100), nullable=False)
    music_name = db.Column(db.String(100), nullable=False)
    posted_at = db.Column(db.DateTime(), default=ist_now)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

admin = Admin(app)
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))
admin.add_view(ModelView(Music, db.session))

# firebaseConfig = {
#           'apiKey' : "AIzaSyCQkjV7XaPn6woOpi97Jl-XZtFsfz8NZFg",
#           'authDomain' : "noteswallah2023.firebaseapp.com",
#           'databaseURL' : "https://noteswallah2023-default-rtdb.asia-southeast1.firebasedatabase.app/",
#           'projectId' : "noteswallah2023",
#           'storageBucket' : "noteswallah2023.appspot.com",
#           'messagingSenderId' : "936818867625",
#           'appId' : "1:936818867625:web:41a3363ad80ce0e240d8b8",
#           'measurementId' : "G-7ZZH98GYBP"
#         };

# firebase = pyrebase.initialize_app(firebaseConfig)

# auth = firebase.auth()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        # try:
        #     auth.sign_in_with_email_and_password(email, password)
        #     session['user_id'] = user.id  
        #     flash('Login Successful', 'Success')
        #     return redirect(url_for('dashboard'))
        # except:
        #     flash('Enter Proper email and password', 'danger')
        #     return redirect(url_for('login'))



        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password, password):
            flash('Login successful!', 'success')
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            flash('Login failed. Check your username and password.', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']


        # try:
        #     auth.create_user_with_email_and_password(email, password)
        #     hashed_password = generate_password_hash(password)

        #     new_user = User(username=username, email=email, password=hashed_password)

        #     db.session.add(new_user)
        #     db.session.commit()

        #     flash('Registration successful! You can now log in.', 'success')
        #     return redirect(url_for('login'))
        # except:
        #     flash('Username or email already exists. Please choose a different one.', 'danger')
        #     return redirect(url_for('register'))


        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()

        if existing_user:
            flash('Username or email already exists. Please choose a different one.', 'danger')
        else:
            hashed_password = generate_password_hash(password)

            new_user = User(username=username, email=email, password=hashed_password)

            db.session.add(new_user)
            db.session.commit()

            flash('Registration successful! You can now log in.', 'success')
            return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    if 'user_id' in session:
        session.pop('user_id', None)
        flash('You have been logged out.', 'info')
    else:
        flash('You are not currently logged in.', 'warning')

    return redirect(url_for('home'))

@app.route('/dashboard')
def dashboard():
    posts = Post.query.order_by(desc(Post.id)).all()
    musics = Music.query.order_by(desc(Music.id)).all()
    post_details = []
    music_details = []

    for post in posts:
        author = post.author
        profile_picture = author.profile_picture
        post_details.append({'post': post, 'author_profile_picture': profile_picture})

    for music in musics:
        author = music.author
        profile_picture = author.profile_picture
        music_details.append({'music': music, 'author_profile_picture': profile_picture})

    return render_template('dashboard.html', post_details=post_details, musiclist=music_details)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def upload_file(file):
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
        return file_path
    return None

@app.route('/create_post', methods=['GET', 'POST'])
def create_post():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        file = request.files['file']
        file_name = request.form['file_name']
        file_description = request.form['file_description']

        if file:
            user_id = session['user_id']
            file_path = upload_file(file)

            new_post = Post(file_name=file_name, file_description=file_description, file_path=file_path, user_id=user_id)

            db.session.add(new_post)
            db.session.commit()

            flash('Post created successfully!', 'success')
            return redirect(url_for('dashboard'))

        else:
            flash('Please upload a file.', 'danger')

    return render_template('create_post.html')

@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get(post_id)
    file_path = post.file_path.replace("static/", "")
    # print(file_path)
    if post:
        return render_template('view_post.html', post=post, file_path=file_path)
    else:
        abort(404)

@app.route('/download_file/<int:post_id>')
def download_file(post_id):
    post = Post.query.get(post_id)

    if post:
        return send_file(post.file_path, as_attachment=True)
    else:
        abort(404)

@app.route('/profile', methods=['GET', 'POST'])
def profile():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    user = User.query.get(session['user_id'])

    if request.method == 'POST':
        file = request.files['profile_picture']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            user.profile_picture = file_path

        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', user=user)

@app.route('/author/<int:user_id>')
def author_profile(user_id):
    user = User.query.get(user_id)
    if user:
        user_profile_picture = user.profile_picture.replace('static/', '')
        user_profile_picture = f"{{{url_for('static', filename={user_profile_picture})}}}"
        return render_template('author_profile.html', user=user, user_profile_picture = user_profile_picture)
    else:
        abort(404)

@app.route('/study_music', methods=['GET', 'POST'])
def share_music():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))

    if request.method == 'POST':
        music_link = request.form['music_link']
        music_name = request.form['music_name']
        if music_link:
            user_id = session['user_id']
            music_link = music_link.split('/')[-1]
            new_music = Music(music_link=music_link, music_name=music_name, user_id=user_id)

            db.session.add(new_music)
            db.session.commit()

            flash('Music Added successfully!', 'success')
            return redirect(url_for('dashboard'))

        else:
            flash('Please upload a Music.', 'danger')

    return render_template('study_music.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_pass():
    if request.method == 'POST':
        password = request.form['password']
        new_password = request.form['confirm-password']
        if password == new_password:
            user = User.query.get(session['user_id'])
            user.password = generate_password_hash(password)
            db.session.commit()
            flash('Password changed successfully!', 'success')
            return redirect(url_for('dashboard'))
    return render_template('change_password.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6010)