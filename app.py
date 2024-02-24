#To, the developer, I made this site for fun. But eventually I messed it up. If it doesn't work on 
# your device, remember it runs on mine. So it's your responsibility to fix this. Good luck !!

#----------NotesWallah-----------#
#------Author: Akash Nath--------#
#-----https://github.com/Akash-nath29----#
#----------------https://akashnath.netlify.app----------------#


from flask import Flask, render_template, request, redirect, session, flash, url_for, send_file, abort
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
import secrets
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
import os
from werkzeug.utils import secure_filename
import pytz
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from os import environ as env
from dotenv import find_dotenv, load_dotenv
import google.generativeai as genai
import markdown2
from authlib.integrations.flask_client import OAuth
from urllib.parse import quote_plus, urlencode
import uuid
<<<<<<< HEAD
from flask_migrate import Migrate
from sqlalchemy.schema import CheckConstraint
=======
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0
# import json

# import pyrebase

ENV_FILE = find_dotenv()
if ENV_FILE:
    load_dotenv(ENV_FILE)

utc_now = datetime.utcnow()
ist_timezone = pytz.timezone('Asia/Kolkata')
ist_now = utc_now.replace(tzinfo=pytz.utc).astimezone(ist_timezone)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.secret_key = secrets.token_hex(64)
app.config['UPLOAD_FOLDER'] = 'static/uploads'

oauth = OAuth(app)

<<<<<<< HEAD
# oauth.register(
#     "auth0",
#     client_id=env.get("AUTH0_CLIENT_ID"),
#     client_secret=env.get("AUTH0_CLIENT_SECRET"),
#     redirect_uri=env.get("AUTH0_CALLBACK_URL"),
#     client_kwargs={
#         "scope": "openid profile email",
#     },
#     server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
# )
=======
oauth.register(
    "auth0",
    client_id=env.get("AUTH0_CLIENT_ID"),
    client_secret=env.get("AUTH0_CLIENT_SECRET"),
    redirect_uri=env.get("AUTH0_CALLBACK_URL"),
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f'https://{env.get("AUTH0_DOMAIN")}/.well-known/openid-configuration',
)
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0

db = SQLAlchemy(app)
migrate = Migrate(app,db,render_as_batch=True)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    email = db.Column(db.Text, nullable=False)
    password = db.Column(db.Text, nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    musics = db.relationship('Music', backref='author', lazy=True)
<<<<<<< HEAD
    comments = db.relationship('Comment', backref='author', lazy=True)
    profile_picture = db.Column(db.String(255), default='static/img/default.png')
=======
    profile_picture = db.Column(db.String(255))
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(100), nullable=False)
    file_description = db.Column(db.Text, nullable=True)
    file_path = db.Column(db.String(255), nullable=False)
<<<<<<< HEAD
    college = db.Column(db.String(255), nullable=True)
    posted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',name='fk_post_user'), nullable=False)
=======
    posted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0

class Music(db.Model):
    __tablename__ = 'music'
    id = db.Column(db.Integer, primary_key=True)
    music_link = db.Column(db.String(100), nullable=False)
    music_name = db.Column(db.String(100), nullable=False)
    posted_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',name='fk_music_user'), nullable=False)

<<<<<<< HEAD
class Comment(db.Model):
    __tablename__ = 'comment'
    id = db.Column(db.Integer, primary_key=True)
    comment = db.Column(db.Text, nullable=False)
    commented_at = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id',name='fk_comment_user'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id',name='fk_comment_post'), nullable=False)


# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Post, db.session))
# admin.add_view(ModelView(Music, db.session))

@app.route('/admin')
def admin_panel():
    
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    current_user = User.query.get(session['user_id'])
    if current_user.id != 1 and current_user.id != 2:
        flash('You do not have permission to access the admin panel.', 'danger')
        return redirect(url_for('dashboard'))
    
    posts = Post.query.all()
    users = User.query.all()
    musics = Music.query.all()
    comments = Comment.query.all()
    current_user = User.query.filter_by(id=session['user_id']).first()
    latest_post = Post.query.order_by(desc(Post.id)).first()
    latest_music = Music.query.order_by(desc(Music.id)).first()
    latest_comment = Comment.query.order_by(desc(Comment.id)).first()
    latest_user = User.query.order_by(desc(User.id)).first()
    return render_template("/admin/admin_panel.html", posts=posts, musics=musics, users=users, comments=comments, current_user=current_user, latest_post=latest_post, latest_music=latest_music, latest_comment=latest_comment, latest_user=latest_user)


=======
# admin = Admin(app)
# admin.add_view(ModelView(User, db.session))
# admin.add_view(ModelView(Post, db.session))
# admin.add_view(ModelView(Music, db.session))

@app.route('/admin')
def admin_panel():
    
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    current_user = User.query.get(session['user_id'])
    if current_user.id != 2 and current_user.id != 3:
        flash('You do not have permission to access the admin panel.', 'danger')
        return redirect(url_for('dashboard'))
    
    posts = Post.query.all()
    users = User.query.all()
    musics = Music.query.all()
    
    return render_template("/admin/admin_panel.html", posts=posts, musics=musics, users=users)


>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0

@app.route('/admin/deleteuser/<int:user_id>')
def admin_panel_delete_user(user_id):
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
    return redirect(url_for('admin_panel'))

@app.route('/admin/user/<int:user_id>', methods=['GET', 'POST'])
def admin_panel_edit_user(user_id):
    user = User.query.get(user_id)

    if request.method == 'POST':
        user.file_name = request.form.get('file_name')
        user.file_description = request.form.get('file_description')
        db.session.commit()
        return redirect(url_for('admin_panel'))

    return render_template('/admin/edit_user.html', user=user)



@app.route('/admin/deletepost/<int:post_id>')
def admin_panel_delete_post(post_id):
    post = Post.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for('admin_panel'))

@app.route('/admin/editpost/<int:post_id>', methods=['GET', 'POST'])
def admin_panel_edit_post(post_id):
    post = Post.query.get(post_id)

    if request.method == 'POST':
        post.file_name = request.form.get('file_name')
        post.file_description = request.form.get('file_description')
        db.session.commit()
        return redirect(url_for('admin_panel'))

    return render_template('/admin/edit_post.html', post=post)

@app.route('/admin/deletemusic/<int:music_id>')
def admin_panel_delete_music(music_id):
    music = Music.query.get(music_id)
    db.session.delete(music)
    db.session.commit()
    return redirect(url_for('admin_panel'))

@app.route('/admin/editmusic/<int:music_id>', methods=['GET', 'POST'])
def admin_panel_edit_music(music_id):
    music = Music.query.get(music_id)

    if request.method == 'POST':
        music.music_link = request.form.get('music_link')
        music.music_name = request.form.get('music_name')
        db.session.commit()
        return redirect(url_for('admin_panel'))

    return render_template('/admin/edit_music.html', music=music)
<<<<<<< HEAD

@app.route('/admin/deletecomment/<int:comment_id>')
def admin_panel_delete_comment(comment_id):
    comment = Comment.query.get(comment_id)
    db.session.delete(comment)
    db.session.commit()
    return redirect(url_for('admin_panel'))
=======
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0

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

    return render_template('/auth/login.html')


# @app.route('/login')
# def login():
#     return oauth.auth0.authorize_redirect(
#         redirect_uri=url_for("callback", _external=True)
#     )

# @app.route('/callback')
# def callback():
#     try:
#         token = oauth.auth0.authorize_access_token()
#         userinfo = oauth.auth0.parse_id_token(
#             token, nonce=session.get('nonce'))
#         session["user"] = userinfo
#         print(userinfo)
#         print(session["user"])
#         print(userinfo)

#         # Check if the user already exists in the local database
#         user = User.query.filter_by(email=userinfo['email']).first()

#         if not user:
#             # If the user doesn't exist, create a new user in the local database
#             user = User(
#                 username=userinfo['nickname'], email=userinfo['email'], profile_picture=userinfo['picture'])
#             db.session.add(user)
#             db.session.commit()

#         # Store the user information in the session
#         session['user'] = userinfo
#         user_id = userinfo['sub']

#         return redirect(url_for('dashboard'))
#     except Exception as e:
#         flash(f'Error during callback: {str(e)}', 'danger')
#         return redirect('/')


# # @app.route("/logout")
# # def logout():
# #     session.clear()
# #     return redirect(
# #         "https://"
# #         + env.get("AUTH0_DOMAIN")
# #         + "/v2/logout?"
# #         + urlencode(
# #             {
# #                 "returnTo": url_for("home", _external=True),
# #                 "client_id": env.get("AUTH0_CLIENT_ID"),
# #             },
# #             quote_via=quote_plus,
# #         )
# #     )


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

    return render_template('/auth/register.html')

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
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    posts = Post.query.order_by(desc(Post.id)).all()
    musics = Music.query.order_by(desc(Music.id)).all()
    post_details = []
    music_details = []
    for post in posts:
        author = post.author
        profile_picture = author.profile_picture
        college = post.college
        post_details.append({'post': post, 'author_profile_picture': profile_picture, 'college': college})

    for music in musics:
        author = music.author
        profile_picture = author.profile_picture
        music_details.append({'music': music, 'author_profile_picture': profile_picture})

    current_user = User.query.filter_by(id=session['user_id']).first()
    
    return render_template('dashboard.html', post_details=post_details, musiclist=music_details, curr_user=current_user)

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

def upload_file(file_or_path):
    if isinstance(file_or_path, str):
        return file_or_path

    if file_or_path and hasattr(file_or_path, 'filename'):
        unique_filename = str(uuid.uuid4()) + '_' + \
            secure_filename(file_or_path.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        file_or_path.save(file_path)
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
        college = request.form['college']

        if file:
            user_id = session['user_id']
            file_path = upload_file(file)

<<<<<<< HEAD
            new_post = Post(file_name=file_name, file_description=file_description,  file_path=file_path, college=college, posted_at=ist_now, user_id=user_id)
=======
            new_post = Post(file_name=file_name, file_description=file_description, file_path=file_path, posted_at=ist_now, user_id=user_id)
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0

            db.session.add(new_post)
            db.session.commit()

            flash('Post created successfully!', 'success')
            return redirect(url_for('dashboard'))

        else:
            flash('Please upload a file.', 'danger')
    current_user = User.query.filter_by(id=session['user_id']).first()
    return render_template('create_post.html', curr_user=current_user)

@app.route('/view_post/<int:post_id>')
def view_post(post_id):
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    post = Post.query.get(post_id)
    file_path = post.file_path.replace("static/", "")
    # print(file_path)
    current_user = User.query.filter_by(id=session['user_id']).first()
<<<<<<< HEAD
    comments = Comment.query.filter_by(post_id=post_id).order_by(desc(Comment.id)).all()
    if post:
        return render_template('view_post.html', post=post, file_path=file_path, curr_user=current_user, comments=comments)
=======
    if post:
        return render_template('view_post.html', post=post, file_path=file_path, curr_user=current_user)
>>>>>>> cb89d8ca93c1c8e05f15145a02dded4664d066c0
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
            filename = str(uuid.uuid4()) + '_' + \
            secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            user.profile_picture = file_path

        user.username = request.form['username']
        user.email = request.form['email']
        db.session.commit()
        flash('Profile updated successfully!', 'success')
        return redirect(url_for('profile'))

    return render_template('profile.html', curr_user=user)

@app.route('/author/<int:user_id>')
def author_profile(user_id):
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
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
            posted_at = ist_now
            new_music = Music(music_link=music_link, music_name=music_name, posted_at=posted_at, user_id=user_id)

            db.session.add(new_music)
            db.session.commit()

            flash('Music Added successfully!', 'success')
            return redirect(url_for('dashboard'))

        else:
            flash('Please upload a Music.', 'danger')
    current_user = User.query.filter_by(id=session['user_id']).first()
    return render_template('study_music.html', curr_user=current_user)

@app.route('/change_password', methods=['GET', 'POST'])
def change_pass():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    user = User.query.filter_by(id=session['user_id']).first()
    if request.method == 'POST':
        prev_pass = request.form['prev_pass']
        new_pass = request.form['new_pass']
        password = request.form['password']
        if user.password == prev_pass:
            if new_pass == password:
                user.password = generate_password_hash(password)
                db.session.commit()
                flash('Password changed successfully!', 'success')
            return redirect(url_for('dashboard'))
    return render_template('change_password.html', curr_user=user)

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        topic = request.form['topic']
        print(topic)
        GOOGLE_API_KEY = env.get("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"You need to provide a detailed premium quality class notes on the following topic. Make sure to add all the important points and sources so that user can search the resources as well. Now generate premium quality notes on the topic {topic}")
        # for chunk in response:
        #     print(chunk.text)
        #     print("_"*80)
        html_content = markdown2.markdown(response.candidates[0].content.parts[0].text)
        current_user = User.query.filter_by(id=session['user_id']).first()
        return render_template('generate_notes.html', result=html_content, curr_user=current_user)
    current_user = User.query.filter_by(id=session['user_id']).first()
    return render_template('generate_notes.html', curr_user = current_user)

@app.route('/jisce')
def jisce():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    jisce_notes = Post.query.filter_by(college='jisce').order_by(desc(Post.id)).all()
    current_user = User.query.filter_by(id=session['user_id']).first()
    post_details = []
    for post in jisce_notes:
        author = post.author
        profile_picture = author.profile_picture
        college = post.college
        post_details.append({'post': post, 'author_profile_picture': profile_picture, 'college': college})
    return render_template('jisce.html', jisce_notes=post_details, curr_user=current_user)

@app.route('/nit')
def nit():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    nit_notes = Post.query.filter_by(college='nit').order_by(desc(Post.id)).all()
    current_user = User.query.filter_by(id=session['user_id']).first()
    post_details = []
    for post in nit_notes:
        author = post.author
        profile_picture = author.profile_picture
        college = post.college
        post_details.append({'post': post, 'author_profile_picture': profile_picture, 'college': college})
    return render_template('nit.html', nit_notes=post_details, curr_user=current_user)

@app.route('/jisu')
def jisu():
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    jisu_notes = Post.query.filter_by(college='jisuni').order_by(desc(Post.id)).all()
    current_user = User.query.filter_by(id=session['user_id']).first()
    post_details = []
    for post in jisu_notes:
        author = post.author
        profile_picture = author.profile_picture
        college = post.college
        post_details.append({'post': post, 'author_profile_picture': profile_picture, 'college': college})
    return render_template('jisu.html', jisu_notes=post_details, curr_user=current_user)

@app.route('/add_comment/<int:post_id>', methods=['GET', 'POST'])
def add_comment(post_id):
    if 'user_id' not in session:
        flash('You need to log in first.', 'danger')
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        comment = request.form['comment']
        user_id = session['user_id']
        commented_at = ist_now
        new_comment = Comment(comment=comment, commented_at=commented_at, user_id=user_id, post_id=post_id)

        db.session.add(new_comment)
        db.session.commit()

        flash('Comment Added successfully!', 'success')
        return redirect(url_for('view_post', post_id=post_id))

@app.route('/generate', methods=['GET', 'POST'])
def generate():
    if request.method == 'POST':
        topic = request.form['topic']
        print(topic)
        GOOGLE_API_KEY = env.get("GOOGLE_API_KEY")
        genai.configure(api_key=GOOGLE_API_KEY)
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(f"You need to provide a detailed premium quality class notes on the following topic. Make sure to add all the important points and sources so that user can search the resources as well. Now generate premium quality notes on the topic {topic}")
        # for chunk in response:
        #     print(chunk.text)
        #     print("_"*80)
        html_content = markdown2.markdown(response.candidates[0].content.parts[0].text)
        current_user = User.query.filter_by(id=session['user_id']).first()
        return render_template('generate_notes.html', result=html_content, curr_user=current_user)
    current_user = User.query.filter_by(id=session['user_id']).first()
    return render_template('generate_notes.html', curr_user = current_user)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6011)