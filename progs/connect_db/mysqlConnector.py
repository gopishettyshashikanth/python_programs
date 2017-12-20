import mysql.connector

db = mysql.connector.connect(user='root', password='123456aA',
                              host='127.0.0.1',
                              database='shashi')
cursor = db.cursor()
#sql = "SELECT * FROM EMPLOYEE"
cursor.execute("""SELECT * FROM EMPLOYEE""")
results = cursor.fetchall()
print results
db.close()