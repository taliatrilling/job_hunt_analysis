import psycopg2

try:
	connection = psycopg2.connect("dbname='jobs' user='taliatrilling' host='localhost'")
except:
	print "Fail"

current = connection.cursor()

def get_companies_dict(curr):
	"""
	Get dictionary of companies applied to and corresponding primary keys
	"""
	curr.execute("""SELECT * FROM application""")
	rows = curr.fetchall()
	companies = {}
	for row in rows:
		companies[row[0]] = row[1]
	return companies

def get_entries(curr, query_of_interest, companies_applied_to):
	""" 
	Get list of companies for a certain category of entries
	"""

	curr.execute("""SELECT * FROM """ + query_of_interest)
	rows = curr.fetchall()
	entries = [companies_applied_to[row[0]] for row in rows]
	return entries

companies = get_companies_dict(current)

first_screens = get_entries(current, 'first_screen', companies)

code_challenges = get_entries(current, 'code_challenge', companies)

onsites = get_entries(current, 'onsite', companies)

tech_screens = get_entries(current, 'technical_screen', companies)

offers = get_entries(current, 'offer', companies)
