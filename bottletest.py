from bottle import route, run

@route('/hello/:name')
def index(name='Bob'):
    return '<b>Hello %s!</b>' % name

run(host='localhost', port=8080)
