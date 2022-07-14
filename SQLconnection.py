import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="vaibhav", password="1234", database="school")
if mydb.is_connected():
    print("success")

sql_stmt = "select * from students"
myCursor = mydb.cursor()      # cursor is used to access data, can be imagined as a pointer which points to the data
myCursor.execute(sql_stmt)          # execute any sql statement here
records = myCursor.fetchall()       # to store data in records, or fetchone to fetch first record
print()
print
for i in records:
    print(i[0], i[1])
    print(i)