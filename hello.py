from bottle import route, run

@route('')
@route('/hello/<name>')
def great(name='stranger'):
    return template('Hello {{name}}, how are you?',name =name
    )

run(host='localhost',port=8080,debug=True)
