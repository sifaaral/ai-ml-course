from flask import Flask, render_template, request,redirect,url_for
import mysql.connector

app =Flask(__name__)

db = mysql.connector.connect(
    host = 'localhost',
    user ='root',
    password ='',
    database ='yapay_zeka'

)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/kayitol',methods =['POST'])
def kayitol():
    if request.method=='POST':
        name=request.form['name']
        name=request.form['email']
        name=request.form['password']

        cursor=db. cursor()
        cursor.execute('insert into kullanici_bilgisi (name,email,password) values (%s,%s,%s)',(name,email,password))
        db.commit()
        db.close()
        return redirect(url_for('index'))
    
cursor=db.cursor()
name="ahmet"
email='ahmet@ahmet'
password="56778"
user_id=1

cursor.execute('update kullanici_bilgileri ser name=%s, email=%s, password=%s where id=%s ',(name,email,password,user_id)) 
db.commit
db.close



cursor.execute('delete from  kullanici_bilgileri where id=%s ',(user_id)) 
db.commit
db.close

if __name__ =='__main__':
        app.run(debug=True)