#doesn't work as a function for some reason

import sqlite3

def init():

    conn = sqlite3.connect('./DB/db.db') # Warning: This file is created in the current directory
    conn.execute("CREATE TABLE todo (category char(50), theitem char(100),id INTEGER PRIMARY KEY )")
    conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','eggs')")
    conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','milk')")
    conn.execute("INSERT INTO todo (category, theitem) VALUES ('Shopping','bread')")
    conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','snow tires')")
    conn.execute("INSERT INTO todo (category, theitem) VALUES ('Activities','rack lawn')")

    conn.commit()

    c = conn.cursor()
    
    c.execute("SELECT * FROM todo")
    result = c.fetchall()
    c.close()
    return str(result)