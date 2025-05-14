from flask import Flask, jsonify, render_template, request

app = Flask(__name__)  # Create the Flask application

# This list stores our todos in memory (not saved permanently)
todos = []

# Route: Get all todos (GET request)
@app.route('/todos', methods=['GET'])
def get_todos():
    return render_template("index.html", todos=todos)

# Route: Add a new todo (POST request)

@app.route('/todos', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    status = request.form.get('status', 'Not Completed')
    todos.append({"task": task, "status": status})
    return render_template("index.html", todos=todos)

@app.route('/todos/toggle/<int:index>', methods=['POST'])
def toggle_status(index):
    if 0 <= index < len(todos):
        current_status = todos[index]['status']
        todos[index]['status'] = 'Completed' if current_status == 'Not Completed' else 'Not Completed'
    return render_template("index.html", todos=todos)
@app.route('/todos/<int:index>', methods=['POST'])  # Must be POST here
def delete_todo(index):
    if 0 <= index < len(todos):
        todos.pop(index)
    return render_template("index.html", todos=todos)

@app.route('/')
def home():
    return render_template('index.html', todos=todos)

# Start the Flask server
if __name__ == '__main__':
    app.run(debug=True)
