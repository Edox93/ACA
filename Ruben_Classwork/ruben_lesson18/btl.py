from bottle import route, run, request


@route('/')
def index():
    return """<form method='POST' action='/calc'>
                <input name='x' />
                <input name='y' />
                <input type=submit />
              </form>"""


@route('/calc', method='POST')
def login():
    x = int(request.forms.get('x'))
    y = int(request.forms.get('y'))

    z = x + y

    return """<p>Result: {}</p>""".format(z)


run(host='localhost', port=8080)
