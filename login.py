from flask import Flask, render_template, request, redirect, Response, url_for, flash
from flask_login import LoginManager, login_required, UserMixin, login_user, current_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, username, password, id, active=True):
        self.id = id
        self.username = username
        self.password_hash = generate_password_hash(password)
        self.active = active

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class UsersRepository:

    def __init__(self):
        self.users = dict()
        self.users_id_dict = dict()
        self.identifier = 0
    
    def save_user(self, user):
        self.users_id_dict.setdefault(user.id, user)
        self.users.setdefault(user.username, user)
    
    def get_user(self, username):
        return self.users.get(username)
    
    def get_user_by_id(self, userid):
        return self.users_id_dict.get(userid)
    
    def next_index(self):
        self.identifier += 1
        return self.identifier

users_repository = UsersRepository()

@app.route('/')

@app.route('/home')
@login_required
def home():
    return f"<h1>{current_user.username}'s Home</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        registered_user = users_repository.get_user(username)

        if registered_user and registered_user.check_password(password):
            login_user(registered_user)
            return redirect(url_for('home'))
        else:
            flash('Invalid username or password', 'danger')
            return redirect(url_for('login'))

    return render_template('login.html')



@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully', 'success')
    return redirect(url_for('login'))

# handle login failed
@app.errorhandler(401)
def page_not_found(e):
    flash('Login failed. Please try again.', 'danger')
    return redirect(url_for('login'))

# callback to reload the user object        
@login_manager.user_loader
def load_user(userid):
    return users_repository.get_user_by_id(userid)

if __name__ == '__main__':
    app.run(host='172.16.3.53', port=8080, debug=True)