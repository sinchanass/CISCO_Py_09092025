from flask_sqlalchemy import SQLAlchemy
db=SQLAlchemy
class Employee(db.Model):
    __tablename__="employees"
    id=db.Column(db.Integer,primary_key = True)
    name=db.Column(db.String(255),nullable=False)
    age=db.Column(db.Integer,nullable=False)
    salary=db.column(db.Boolean,nullable=False)

    def __repr__(self):
        return f'[id={self.id,name={self.name},age={self,age},salary={self.salary}}]'
    def to_dict(self):
        return{'id':self.id,'name':self.name}