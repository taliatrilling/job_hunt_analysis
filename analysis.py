import psycopg2

try:
	connection = psycopg2.connect("dbname='jobs' user='taliatrilling' host='localhost'")
except:
	print "Fail"

current = connection.cursor()

current.execute("""SELECT * FROM application""")
rows = current.fetchall()
companies = {}
for row in rows:
	companies[row[0]] = row[1]
# companies = [row[1] for row in rows]

current.execute("""SELECT * FROM first_screen""")
rows = current.fetchall()
screens = [companies[row[0]] for row in rows]

print screens