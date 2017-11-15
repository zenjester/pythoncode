#staticH.py - Haiku
#12.12.13 Haiku code

from bottle import static_file,route,run

@route('/staticfiles/<filename>')
def server_static(filename):
	    return static_file(filename, root='./staticfiles/')

run(host='localhost', port=8118, debug=True)
