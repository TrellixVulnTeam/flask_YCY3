from flask import Flask ,render_template
import sqlalchemy as db
app = Flask(__name__)
import timeago, datetime

now = datetime.datetime.now() 
#ss
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

	query1='SELECT COUNT("stype"),stype FROM ticket WHERE status="Open" GROUP BY stype;'

	ResultProxy1 = connection.execute(query1)
	ResultSet1 = ResultProxy1.fetchall()
	print(ResultSet1)
	'''try:
		print(ResultSet[0][0])
	except:
		ResultSet=[('',), ('',), ('',)]'''
	dict_result={}
	for i in ResultSet1:
		dict_result[i[1]]=int(i[0])
		print(dict_result)
	


	return render_template('rtpa.html',aa=aa,current_time=current_time,timeago=timeago,dict_result=dict_result)




if __name__ == '__main__':
   app.run(host= '0.0.0.0')


