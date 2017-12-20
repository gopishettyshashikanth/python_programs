import psycopg2

db = psycopg2.connect(host="localhost",database="shashi", user="postgres", password="123456aA")
cursor = db.cursor()
cursor.execute("""SELECT * FROM COMPANY""")
results = cursor.fetchall()
print results
db.close()