from flask import Flask,request
import sqlite3
app =Flask(__name__)
@app.get('/')
def func():
  con=sqlite3.Connection("C:/Users/trc/Desktop/night skill/Aadhya/data.db")
  curs=con.cursor()
  curs.execute("select * from student")
  data=curs.fetchall()
  con.commit()
  con.close()
  return f'{data}'

@app.post('/h')
def world():
  con=sqlite3.Connection("C:/Users/trc/Desktop/night skill/Aadhya/data.db")
  curs=con.cursor()
  data= request.get_json()
  name=data["name"]
  rollno=data["rollno"]
  mark=data["mark"]
  detail=(name,rollno,mark)
  curs.execute("create table if not exists student(name varchar(50),rollno int,mark int)")
  curs.execute("insert into student values(?,?,?)",detail)
  con.commit()
  con.close()
  print(data)
  return f'<h1><center>The data we got is {data}</center></h1>'

@app.patch("/upd")
def up():
   data =request.get_json()
   update(data)
   return("Updated")
def update(data):
   con=sqlite3.Connection("C:/Users/trc/Desktop/night skill/Aadhya/data.db")
   query = f'update student set rollno ="{data["rollno"]}" where name ="{data["name"]}"'
   cur=con.cursor()
   cur.execute(query)
   con.commit()

app.run(debug=True)