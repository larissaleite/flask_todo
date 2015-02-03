#!flask/bin/python
from flask import Flask, jsonify, abort, request, make_response, url_for, render_template
 
app = Flask(__name__, static_url_path = "")

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web', 
        'done': False
    }
]

def make_public_task(task):
    new_task = {}
    for field in task:
        if field == 'id':
            new_task['uri'] = url_for('get_task', task_id = task['id'], _external = True)
        else:
            new_task[field] = task[field]
    return new_task
 
@app.route('/todo/api/v1.0/tasks', methods = ['GET'])
def get_tasks():
    return jsonify( { 'tasks': map(make_public_task, tasks) } )
 
@app.route('/todo/api/v1.0/tasks/<int:task_id>', methods = ['GET'])
def get_task(task_id):
    task = filter(lambda t: t['id'] == task_id, tasks)
    #if len(task) == 0:
    #    abort(404)
    return jsonify( { 'task': make_public_task(task[0]) } )
 
@app.route('/todo/api/v1.0/tasks', methods = ['POST'])
def create_task():
    #if not request.json or not 'title' in request.json:
    #    abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify( { 'tasks': map(make_public_task, tasks) } )

#static files
@app.route('/tasks', methods = ['GET'])
def show_page():
    return app.send_static_file('index.html')
    
if __name__ == '__main__':
    app.run(debug = True)