from pycricbuzz import Cricbuzz
c = Cricbuzz()
matches = c.matches()
for match in matches:
	#print (match)
	if(match['mchstate'] != 'nextlive'):
		match1= (c.livescore(match['id']))
		#print (c.commentary(match['id']))
		#
		#print (c.scorecard(match['id']))
		print(match1)
		break