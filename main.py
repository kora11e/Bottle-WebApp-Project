from bottle import run, route, template

@route('/')
def home():
    return '<h>Hello World</h>'

@route('/page1')
def page1():
    return '<h>Hello Here</h>'

@route('/page2')
def page2():
    return '<h>Hello Bear</h>'


#starting the App
if __name__ == '__main__':
    run(debug=True, reloader=True)
