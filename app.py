from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_user, logout_user, login_required, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from model import db, User, Todo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todos.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Set up Flask-Login
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Home Page - Shows Todos (if logged in)
@app.route('/')
@login_required
def home():
    todos = Todo.query.filter_by(user_id=current_user.id).all()
    return render_template('index.html', todos=todos)

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username already exists.')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password)
        user = User(username=username, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. Please log in.')
        return redirect(url_for('login'))
    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user and check_password_hash(user.password, request.form['password']):
            login_user(user)
            return redirect(url_for('home'))
        flash('Invalid credentials.')
    return render_template('login.html')

# Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

# Add Todo
@app.route('/todos', methods=['POST'])
@login_required
def add_todo():
    task = request.form.get('task')
    if task:
        new_todo = Todo(task=task, user_id=current_user.id)
        db.session.add(new_todo)
        db.session.commit()
    return redirect(url_for('home'))

# Toggle Todo Status
@app.route('/todos/toggle/<int:id>', methods=['POST'])
@login_required
def toggle_todo(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        return "Unauthorized", 403
    todo.status = 'Completed' if todo.status == 'Not Completed' else 'Not Completed'
    db.session.commit()
    return redirect(url_for('home'))

# Delete Todo
@app.route('/todos/delete/<int:id>', methods=['POST'])
@login_required
def delete_todo(id):
    todo = Todo.query.get_or_404(id)
    if todo.user_id != current_user.id:
        return "Unauthorized", 403
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for('home'))

# Create database before the first request


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
