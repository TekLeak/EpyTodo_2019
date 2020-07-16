from app import app, connection, controller
from flask import Flask, render_template, request
from datetime import date

conn = connection.getConnection(app)

@app.route('/', methods = ['GET'])
@app.route('/index', methods = ['GET'])
def route_index () :
    return render_template ("index.html")

@app.route('/register', methods = ['POST'])
def route_register() :
    return controller.user_register(conn)

@app.route('/signin', methods = ['POST'])
def route_signin() :
    return controller.signin(conn)

@app.route('/signout', methods = ['POST'])
def route_signout() :
    return controller.signout()

@app.route('/user', methods = ['GET'])
def route_user() :
    return render_template("profil.html")

@app.route('/user/task', methods = ['GET'])
def route_user_tasks() :
    return render_template("profil_task.html")

@app.route('/user/task/<int:task_id>', methods = ['GET', 'POST'])
def route_manage_task(task_id) :
    if request.method == 'GET':
        return ("One task")
    if request.method == 'POST':
        return ("Update")

@app.route('/user/task/add', methods = ['POST'])
def route_create_task() :
    return controller.task_create(conn)

@app.route('/user/task/del/<int:task_id>', methods = ['POST'])
def route_del_task(task_id) :
    return ("Delete this task")