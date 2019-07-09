from flask import Flask ,render_template,jsonify, request
import sqlalchemy as db
from pycricbuzz import Cricbuzz

app = Flask(__name__)
import timeago, datetime

now = datetime.datetime.now() 
#ss
date = datetime.datetime.now()
print (timeago.format(date, now)) # will print 3 minutes ago
import time
import datetime
	



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
	

	dict_result={}
	for i in ResultSet1:
		dict_result[i[1]]=int(i[0])
		print(dict_result)



    
	#if(matches[1]['mchstate'] != 'nextlive'):
		#match1= (c.livescore(matches[1]['id']))
		#print (c.commentary(match['id']))
		#
		#print (c.scorecard(match['id']))
		#print(match1)



		
	

	

			


	return render_template('rtpa.html',aa=aa,current_time=current_time,timeago=timeago,dict_result=dict_result, reload = time.time())


@app.route("/api/calc")
def add():
    a = int(request.args.get('a', 0))
    b = int(request.args.get('b', 0))
    div = 'na'
    if b != 0:
        div = a/b
    return jsonify({
        "a"        :  a,
        "b"        :  b,
        "add"      :  a+b,
        "multiply" :  a*b,
        "subtract" :  a-b,
        "divide"   :  div,
    })




@app.route("/api/match")
def cric():
	c = Cricbuzz()
	matches = c.matches()
	match=matches[2]
	if True:
		print(match)
		if(match['mchstate'] != 'nextlive'):
			match1= (c.livescore(match['id']))
			
			if 'batting' in match1.keys():
				a=(match1['batting']['score'])[0]
				team=match1['batting']['team']
				run=a['runs']
				wickets=a['wickets']
				overs=a['overs']
				score=team +"  :   "+run+' / '+wickets +' in  '+ overs
				bats=(match1['batting']['batsman'])[0]
				batsman=(bats['name']),' : ',(bats['runs']),' in ',(bats['balls']),' balls'
				print(match1['batting']['team'],a['runs'],' / ',a['wickets'] ,'in',a['overs'])
				#break
				return jsonify({
"batsman":batsman,
"score": score,
"team"        :  team,
"run"      :  run,
"wickets" :  wickets,
"overs" :  overs,
"time":datetime.datetime.now(),

    })
			else:
				temp='India VS NZ'
				return jsonify({
"batsman":temp,
"score":temp ,
"team"        :  temp,
"run"      :  temp,
"wickets" :  temp,
"overs" :  temp,
"time":datetime.datetime.now(),


  })


if __name__ == '__main__':
   app.run(port= 5003)


