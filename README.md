# TodoApp
# 📝 Flask Todo App with Authentication

A simple, mobile-friendly Todo web application built using **Flask**, with user registration, login, logout, and personal task management.

## 🌟 Features

- User Registration & Login (with password hashing)
- Individual Todo lists for each user
- Add, Delete, and Toggle task status
- Mobile-first responsive UI with CSS styling
- Protected routes with Flask-Login
- SQLite database with SQLAlchemy ORM

---

## 🚀 Demo

> 📷 Add a screenshot here  
> ![Screenshot](screenshots/homepage.png)

---

## 📁 Project Structure

todo-flask-app/
│
├── app.py # Main Flask app
├── model.py # Database models
├── /templates # HTML templates
│ ├── login.html
│ ├── register.html
│ └── index.html
├── /static
│ └── style.css # Styling for all pages
└── README.md

yaml
Copy
Edit

---

## 🔧 Setup Instructions

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/todo-flask-app.git
cd todo-flask-app
Create and activate a virtual environment

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate
Install dependencies

bash
Copy
Edit
pip install Flask Flask-Login Flask-SQLAlchemy Werkzeug
Run the application

bash
Copy
Edit
python app.py
Visit the app

Go to http://127.0.0.1:5000 in your browser.

🛠 Tech Stack
Technology	Purpose
Flask	Web framework
SQLAlchemy	ORM (Object Relational Mapper)
Flask-Login	User session management
Jinja2	HTML templating
SQLite	Lightweight DB
HTML/CSS	Frontend UI

🧠 Code Explanation
🔐 Authentication
User model implements UserMixin from Flask-Login

Passwords are hashed using werkzeug.security

Auth routes:

/register: New user registration

/login: User login

/logout: Ends user session

✅ Todo Functionality
Each todo is linked to a user_id

add, delete, and toggle handled via routes

Tasks are filtered per user:
Todo.query.filter_by(user_id=current_user.id).all()

🎨 Styling
style.css is written for responsiveness (mobile-first)

Clean layout with shadows, gradients, and spacing

Form elements are styled consistently across all pages

📷 Screenshots
Page	Screenshot
Login	
Register	
Todo Page	

Add screenshots in the /screenshots folder and update paths above

📝 License
This project is licensed under the MIT License.

💡 Future Improvements
Dark mode toggle 🌙

Edit tasks ✏️

Due dates & reminders ⏰

API endpoints (for mobile clients) 📱

🤝 Contributing
Feel free to fork, open issues, or make PRs. Contributions are welcome!