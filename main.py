from bottle import run, route, template
import controlMethods, alchemy

@route('./styles.style.css')
def stylization():
    return static_file('./styles.style.css', root='static')

@route('/')
def home():
    return '<h>Hello World</h>'


@route('/dataset1/')
@route('/dataset1')
def page1():
    return '<h>Hello Here</h>'


@route('/dataset2/')
@route('/dataset2')
def page1():
    return template()


@route('/author/')
@route('/author')
def author():
    return template('./views/authors.tpl')


#starting the App
if __name__ == '__main__':
    run(debug=True, reloader=True)
