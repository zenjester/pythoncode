from bottle import static_file,route,run

@route('/staticfiles/<filename>')
def server_static(filename):
	    return static_file(filename, root='./staticfiles/')

run(host='localhost', port=8888, debug=True)
