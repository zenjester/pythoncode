#helloW.py standard hello world in bottle
#andyp 12.12.13

from bottle import route, run

@route('/hello')
def hello():
        return "Hello World!"

run(host='localhost', port=8080, debug=True)
