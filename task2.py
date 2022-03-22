@app.patch("/upd")
def update():
    data=request.get_json;
    updates(data)
    return("updated");
    def updates(data)
    query=f'update students set name="{data["name"]}"where rollno="{data["rollno"]}"';
    cur=con.cursor()
    cur.execute(query)
    con.commit()


      
   from flask import Flask,request
import sqlite3
app =Flask(__name__)
@app.get('/')
def hello():
   
   return f'<h1><center>Student database</center></h1>'
@app.post('/h')
def world():
   con=sqlite3.Connection("C:/Users/trc/Desktop/night skill/Aadhya/data.db")
   curs=con.cursor()
   data= request.get_json()
   name=data["Name"]
   rollno=data["Rollno"]
   mark=data["Mark"]
   detail=(name,rollno,mark)
   curs.execute("create table if not exists student(name varchar(50),rollno varchar(40),mark int)")
   curs.execute("insert into student values(?,?,?)",detail)
   con.commit()
   con.close()
   print(data)

  
   


@app.patch("/upd")
def update():
    data=request.get_json;
    updates(data)
    return("updated");
def updates(data)
    query=f'update students set name="{data["name"]}"where rollno="{data["rollno"]}"';
    cur=con.cursor()
    cur.execute(query)
    con.commit()

app.run(debug = True)






@app.delete("/delete/<rollno>")
def deletes(rollno):
   delete(rollno)
   return("Deleted")
def delete(rollno):
   con=sqlite3.Connection("C:/Users/trc/Desktop/New folder/sharmi/data.db")
   query=f'delete from student where rollno="{rollno}"'
   cur= con.cursor()
   cur.execute(query)
   con.commit()

app.run(debug = True)




"C:/Users/trc/Desktop/night skill/Aadhya/data.db"




@app.delete("/delete/<rollno>")
def deletes(rollno):
    delete(rollno)
    return("Deleted")
def delete(rollno):
    con=sqlite3.Connection("C:/Users/trc/Desktop/night skill/Aadhya/data.db")
query=f'delete from student where rollno="{rollno}"'
cur= con.cursor()
cur.execute(query)
con.commit()

app.run(debug = True)
