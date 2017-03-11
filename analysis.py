import psycopg2

try:
	connection = psycopg2.connect("dbname='jobs' user='taliatrilling' host='localhost'")
except:
	print "Fail"

current = connection.cursor()
current.execute("""SELECT * FROM application""")
rows = current.fetchall()
for row in rows:
	print " ", row[1]