import os
from flask  import Flask
from flask import render_template
from form import NameForm
from flask_migrate import Migrate
from models.User import db


#primeiro servidor
app= Flask(__name__)

#importar configuraçoes do config.py
app.config.from_object('config')

#para inicializar o banco de dados e migraçoes
db.init_app(app)
migrate=Migrate(app,db)

#flask db init



#flask db migrate


#flask db upgrade





#GET POST renderizar
@app.route('/',methods=['GET','POST'])
def index(name=None):
   
     name=None
     form=NameForm()
     if form.validate_on_submit():
         name=form.name.data
         form.name.data=" "
         
     return render_template('index.html',name=name,form=form)

#if __name__=='__main__':
    #app.run(debug=True,port=5000)
    