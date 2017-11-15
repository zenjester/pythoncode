#bottTodo.py - bottle framework todo app
#andyp 12.11.12

import sqlite3
from bottle import route, run

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result=c.fetchall()
    return str(result)

run()
