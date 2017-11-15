#helloBot3.py template functions
#andyp 12.12.13

from bottle import *

@route('/test')
def test():
	return template('test.tpl')
	
@route('/hello/<name>')
def hello(name='sid'):
    return template('helloWorld.tpl', name=name)
	
run(host='localhost', port=8818)
