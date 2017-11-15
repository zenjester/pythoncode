from bottle import *

@route('/hello')
def hello():
	return "hello World"
@route('/hello/<name>')
def greet(name='Stranger'):
	return template('Hello {{name}}, how are you?', name=name)
	
run(host='localhost', port=8888)
