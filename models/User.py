from flask_sqlalchemy import SQLAlchemy

#instaciação do  banco
db= SQLAlchemy()

class User(db.Model):
    __tablename__='user'
    id=db.Column(db.Integer,primary_key=True)
    name= db.Column(db.String(30))
    age= db.Column(db.String(30))
    adress=db.Column(db.String(120))
    
 #objeto que sera transformado em json 
 
    def serialize(self):
        #chamar modo chave:valor
        return{
            'id':self.id,
            'name':self.name,
            'age':self.age,
            'adress':self.adress
        }
        