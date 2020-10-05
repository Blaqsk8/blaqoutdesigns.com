!/usr/etc/python3

import cgi
import mysql.connector as conn

def htmlTop():
    print("""Content-type: text/html\n\n
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="utf-8" />
                    <title>My server-side template</title>
                </head>
                <body>""")
                
def htmlTail():
    print("""</body>
        </html>""")

def connectDB():
    db = conn.connect(host='localhost', user='brob', passwd='!@2002NiM2597!@', db='oxissi')
    cusor = db.cursor()
    return db, cursor
             
        
def createPersonList():
    #create blank list
    people = []
    #add people to the list
    people.append(["Adam","Fool"])
    people.append(["Sue","Wes"])
    people.append(["Jack","Frost"])
    people.append(["Beck","Ola"])
    people.append(["John","Snoe"])
    return people

def insertPeople(db, cursor, people):
    for each in people:
        sql = "insert into person(firstname, lastname) values('{0}', '{1}')".format(each[0], each[1])
        cursor.execute(sql)
    db.commit()
    
#main program
if __name__ == "__main__":
    try:
        htmlTop()
        db, cursor = connectDB()
        people = createPersonList()
        insertPeople(db, cursor, people)
        htmlTail()
    except:
        cgi.print_exception()
