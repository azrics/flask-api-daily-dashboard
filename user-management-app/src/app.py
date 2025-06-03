from flask import Flask, render_template, redirect, url_for, request, session
from models import User, db, init_db  # Import db and init_db
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Ensure the instance folder exists
instance_path = os.path.join(os.path.dirname(__file__), '..', 'instance')
os.makedirs(instance_path, exist_ok=True)

# Set the database path inside the instance folder
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.abspath(os.path.join(instance_path, 'users.db'))}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

init_db(app)

@app.before_request
def create_tables():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        user = User(username=username, email=email)
        user.set_password(password)
        user.save()
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.authenticate(username, password)
        if user:
            session['user_id'] = user.id
            return redirect(url_for('dashboard'))
        else:
            return render_template('login.html', error="Invalid credentials")
    return render_template('login.html')

@app.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        user_id = session.get('user_id')
        user = User.get_by_id(user_id)
        if user:
            user.set_password(new_password)
            user.save()
            return redirect(url_for('dashboard'))
        else:
            return redirect(url_for('login'))
    return render_template('reset_password.html')

@app.route('/dashboard')
def dashboard():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    user = User.get_by_id(user_id)
    return render_template('dashboard.html', user=user)

@app.route('/update_profile', methods=['GET', 'POST'])
def update_profile():
    user_id = session.get('user_id')
    if not user_id:
        return redirect(url_for('login'))
    user = User.get_by_id(user_id)
    if request.method == 'POST':
        user.username = request.form['username']
        user.email = request.form['email']
        user.save()
        return redirect(url_for('dashboard'))
    return render_template('update_profile.html', user=user)

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)