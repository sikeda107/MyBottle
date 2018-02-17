from bottle import route, run, template


@route('/')
def root():
    return "route"


@route('/hello')
def hello():
    return "Hello World!"


@route('/hello/<name:re:[a-z]+')
def greet(name):
    return template('Hello {{name}}, how are you?', name=name)


run(host='localhost', port=8080, debug=True)
