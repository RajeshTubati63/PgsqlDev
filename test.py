from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://unvudchhuunmvx:32b9ad464a9bc98dc04e83971e387d038ea09c73c71638d54201353a5dce45bf@ec2-54-243-38-139.compute-1.amazonaws.com:5432/d13gantqlb4dv2'
db = SQLAlchemy(app)


class Property(db.Model):
    __tablename__ = "Property"
    id = db.Column('id',db.Integer, primary_key = True)
    name = db.Column('name',db.Text)
    
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return '<title {}'.format(self.name)
    
@app.route('/')
def index():
    return '<h1> Hello pgsql</h1>'

if __name__ == "__main__":
    app.run(debug=True)