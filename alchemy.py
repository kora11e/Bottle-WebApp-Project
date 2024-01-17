import sqlite3, bottle_sqlite

conn = sqlite3.connect('./DB/games-features.csv')

c = conn.cursor()


conn.close()

def method1():
    c.execute()
    conn.commit()

def method2():
    c.execute()
    conn.commit()

def method3():
    c.execute()
    conn.commit()

def method4():
    c.execute()
    conn.commit()