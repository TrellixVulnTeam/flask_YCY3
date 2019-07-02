from flask import Flask ,render_template
import sqlalchemy as db
app = Flask(__name__)
import timeago, datetime

now = datetime.datetime.now() 

date = datetime.datetime.now()
print (timeago.format(date, now)) # will print 3 minutes ago
	



@app.route('/')
def show_all():
	current_time=datetime.datetime.now()
	from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String,func,select
	engine = create_engine('mysql+pymysql://user:@10.237.89.240/rtpa', echo = False)
	connection = engine.connect()
	metadata = db.MetaData()
	ticket = db.Table('ticket', metadata, autoload=True, autoload_with=engine)
	query=db.select([ticket]).where(ticket.columns.status == 'Open')
	ResultProxy = connection.execute(query)
	aa = ResultProxy.fetchall()
	return render_template('dashboardnew.html',aa=aa,current_time=current_time,timeago=timeago)




if __name__ == '__main__':
   app.run(host= '0.0.0.0')


