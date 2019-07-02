from flask import Flask ,render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://user:@10.237.89.240/rtpa'
app = Flask(__name__)
db=SQLAlchemy(app)

class ticket(db.Model):
   
   id=db.Column('id', db.Integer, primary_key = True), 
   incident_no=db.Column('incident_no', db.String(255)), 
   tittle=db.Column('tittle', db.String(255)), 
   service=db.Column('service', db.String(255)), 
   country=db.Column('country', db.String(255)),
   city=db.Column('city', db.String(255)),
   type=db.Column('type', db.String(255)), 
   impact=db.Column('impact', db.String(255)), 
   status=db.Column('status', db.String(255)),

def __init__(self, id, incident_no, tittle,service,country,city,impact,status):
   self.id = id
   self.incident_no = incident_no
   self.tittle = tittle
   self.service = service
   self.country = country
   self.city = city
   self.type = type
   self.impact = impact
   self.status = status
   
db.create_all()
@app.route('/')
def hello_world():
   return ('Hello %s!' % name)

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/rtpa')
def rtpa():
	
	
	return render_template('dashboard.html', tickets = ticket.query.all())




if __name__ == '__main__':
   app.run(debug = True)


