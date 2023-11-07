Johnson Meitei9:55 AM
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Sample data for tasks
tasks = []

@app.route('/service_1', methods=['GET', 'POST'])
def manage_tasks():
    if request.method == 'GET':
        # Return a list of tasks
        return jsonify({'tasks': tasks})
    elif request.method == 'POST':
        # Create a new task
        data = request.get_json()
        task = {
            'id': len(tasks) + 1,
            'title': data['title'],
            'done': F
d branch working_branch duu-wxik-usr
