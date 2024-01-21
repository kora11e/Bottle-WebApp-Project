from bottle import run, route, template, static_file
import connector


@route("/static/<filename>")
def static(filename):
    return static_file(filename, root="./static")

@route('./author')
@route('./author/')
def authors(author = 'Karol Rochalski'):
    return template('''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Contact information</title>
    <link rel="stylesheet" href="./styles/style.css">
    <link rel="icon" href="./favicon.ico" type="image/x-icon">
  </head>
  <body>
    <main>
        <h1>Contact section</h1>  
    </main>
    <div>
        <div>
            Name: {author}
        </div>
        <div>
            Phone Number: 516 8222 086
        </div>
        <div>
            <p><a href="mailto:k.rochalski@student.uw.edu.pl">Send email</a></p>
        </div>
    </div>
  </body>
</html>
            ''' , )


@route('/')
def home():
    return template('./views/main.tpl')

@route('/database/')
@route('/database')
def todo_list():
    connector.init()

@route('/authors/')
@route('/authors')
def author():
    return template('./views/authors.tpl')

@route('/snake/')
@route('/snake')
def author():
    return template('./views/snake.tpl')

@route('/reroute')
@route('/reroute/')
def home():
    return template('./views/reroute.tpl')



#starting the App
if __name__ == '__main__':
    run(debug=True, reloader=True)
