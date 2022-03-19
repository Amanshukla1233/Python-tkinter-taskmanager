

import sqlite3

# database
# Create a database or connect to one
conn=sqlite3.connect('address.db')

def show():
    query = 'SELECT * FROM todo;'
    return conn.execute(query)

# insert data calling function
def insertdata(task):
    query = "INSERT INTO todo(task) VALUES (?);"
    conn.execute(query,(task,))
    conn.commit()

def deletedatai(taskid):
    query = "DELETE FROM  todo   WHERE id=?;"

    conn.execute(query,(taskid,))
    conn.commit()
def deletebytask(taskval):
    query = "DELETE FROM  todo   WHERE task=?;"
    conn.execute(query, (taskval,))
    conn.commit()

def updatedata1(taskid,newtask):
    query="UPDATE todo SET task=? where id =?;"
    conn.execute(query,(newtask,taskid))
    conn.commit()
conn.execute('''  CREATE TABLE IF NOT EXISTS todo(
    id INTEGER PRIMARY  KEY,
    task TEXT NOT NULL
    );''')
print("database connected")


