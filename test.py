from flask import Flask,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
 
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rajesh:rajesh@localhost/mhipocdb'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://unvudchhuunmvx:32b9ad464a9bc98dc04e83971e387d038ea09c73c71638d54201353a5dce45bf@ec2-54-243-38-139.compute-1.amazonaws.com:5432/d13gantqlb4dv2'
db = SQLAlchemy(app)


class Room(db.Model):
    __tablename__ = "Room"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, nullable = False)
    location = db.Column(db.String, nullable = False)
     
    def __init__(self,name,location):
        self.name = name
        self.location = location
    
    def __repr__(self):
        return '<title {}'.format(self.name)
    
    
@app.route('/newproperty', methods = ['GET','POST'])
def addNewProperty():
    if(request.method == 'POST'):
        newItem  = Room(name = request.form['name'],location = request.form['location'] )
        db.session.add(newItem)
        db.session.commit()
        return redirect(url_for('getPropertynames'))
    else:
        return render_template('addnewproperty.html')

@app.route('/')    
def getPropertynames():
    properties = db.session.query(Room).all()
    return render_template('index.html',properties = properties)
    


if __name__ == "__main__":
    app.debug = True
    app.run(host = '0.0.0.0', port = 8080)