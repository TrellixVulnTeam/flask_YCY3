from pycricbuzz import Cricbuzz
c = Cricbuzz()
matches = c.matches()
for match in matches:
	#print (match)
	if(match['mchstate'] != 'nextlive'):
		#match1= (c.livescore(match['id']))
		print (c.commentary(match['id']))
		#
		#print (c.scorecard(match['id']))
	
		
		"""
		if 'batting' in match1.keys():
		
			a=(match1['batting']['score'])[0]
			#print(match1['batting']['team'],a['runs'],'/',a['wickets'] ,'in',a['overs'])

			#print('==')
			#print(match1['batting'])
			#print((match1['batting']['batsman'])[0])
			break"""