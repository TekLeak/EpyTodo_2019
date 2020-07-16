from app import app, models
from flask import *

# User management

def user_register(conn):
    result = {}
    username = request.form['username']
    password = request.form['password']
    if not username.isalnum():
        result['error'] = "internal error"
    else:
        if models.user_exist(conn, username):
            result['error'] = "account already exists"
        else:
            models.create_user(conn, username, password)
            result['result'] = "account created"
    print(result)
    return redirect(url_for('route_index'))

def signin(conn):
    result = {}
    username = request.form['username']
    password = request.form['password']
    if not models.user_exist(conn, username):
        result['error'] = "login or password does not match"
        print(result)
        return redirect(url_for('route_index'))
    elif not models.check_pass(conn, username, password):
        result['error'] = "login or password does not match"
        print(result)
        return redirect(url_for('route_index'))
    else:
        session['username'] = username
        result['result'] = "signin successful"
        print(result)
        return redirect(url_for('route_user'))
    return redirect(url_for('route_index'))

def signout():
    result = {}
    session.pop('username', None)
    result['result'] = "signout successful"
    print(result)
    return redirect(url_for('route_index'))

# Task management -----------------------------------

def task_create(conn):
    result = {}
    title = request.form['title']
    start = request.form['start']
    end = request.form['end']
    status = request.form['status']
    if session['username']:
        if models.create_task(conn, title, start, end, status):
            result['result'] = "new task added"
            print(result)
            return redirect(url_for('route_user_tasks'))
        else:
            print("JEANNE")
            result['error'] = "internal error"
            print(result)
            return redirect(url_for('route_user'))
    else:
        result['error'] = "internal error"
        print(result)
        return redirect(url_for('route_user'))

def task_update():
    return

def task_delete():
    return

def get_task():
    return

def get_all_tasks():
    return    
