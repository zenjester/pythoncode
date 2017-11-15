from bottle import *

@route('/hello')
@route('/test')
def test():
	return template('test.tpl')
	
@route('/hello/<name>')
def hello(name='World'):
    return template('helloWorld.tpl', name=name)
	
run(host='localhost', port=8888)
