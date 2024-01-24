from bottle import run, route, template, static_file, request, redirect, post, error, abort
import sqlite3, json, requests


@route("/static/<filename>")
def static(filename):
    return static_file(filename, root="./static")

@error(404)
def error404(error):
    return template('./views/error.tpl')

@error(405)
def error405(error):
    return template('./views/error.tpl')

@route('./author')
@route('./author/')
def authors():
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
            Name: Karol Rochalski
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
    #conn = sqlite3.connect('./DB/db.db')
    #conn.execute("CREATE TABLE todo (category char(50), theitem char(100),id INTEGER PRIMARY KEY )")
    #conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','eggs')")
    #conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','milk')")
    #conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','bread')")
    #conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','snow tires')")
    #conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','rack lawn')")

    #conn.commit()

    c = conn.cursor()
    html = "<h1>To do List</h1> <p>Build row-by-row in Python</p>\n"
    
    c.execute("SELECT * FROM todo")
    result = c.fetchall()

    colnames = [description[0] for description in c.description]
    numcol = len(colnames)

    output = template('./views/database.tpl', rows=result, headings=colnames, numcol=numcol)
    return output

@route('/database/new/', method='post')
@route('/database/new', method='post')
def new_item():
    print('New Post:', request.body.read())
    theitem = request.forms.get('newcategory')

    if theitem != '':

        conn = sqlite3.connect('./DB/db.db')
        c = conn.cursor()
        c.execute('INSERT INTO todo (category, theitem) VALUES (?, ?)', (newcategory, theitem))
        conn.commit()
        c.close()

    redirect('/database')

@route('/database/delete', method='post')
@route('/database/delete/', method='post')
def delete_item():
    print('Delete:', request.body.read())
    theid = request.forms.get('delitem').strip()
    print('theid: ', theid)

    conn = sqlite3.connect('./DB/db.db')
    c = conn.cursor()
    sqlstr = "DELETE FROM todo WHERE id=" + str(theid)
    print(sqlstr)
    c.execute(sqlstr)
    conn.commit()
    c.close()

    redirect('/database')

@route('/csv')
@route('/csv/')
def csv():
    return template('./views/csv.tpl')

#@route('/jsondata')
#@route('/jsondata/')
#def jsonReader():
#    return template('./views/json.tpl')

@route('/authors/')
@route('/authors')
def author():
    return template('./views/authors.tpl')

@route('/snake/')
@route('/snake')
def snake():
    return template('./views/snake.tpl')

@route('/reroute')
@route('/reroute/')
def home():
    return template('./views/reroute.tpl')



#starting the App
if __name__ == '__main__':
    run(debug=True, reloader=True)
