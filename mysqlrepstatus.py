#!usr/bin/env python3
import pymysql, smtptlib

db_host = ''
db_user = ''
db_password = ''
 
connection = pymysql.connect(db_host, db_user, db_password)
cursor = connection.cursor(pymysql.cursors.DictCursor)
cursor.execute("SHOW SLAVE STATUS")
rows = cursor.fetchall()

Slave_IO_Running = rows[0]['Slave_IO_Running']
Slave_SQL_Running = rows[0]['Slave_SQL_Running']
 
if Slave_IO_Running != "Yes" or Slave_SQL_Running != "Yes":
    print("Replication is not running")
    print(rows[0]['Last_Error'])
else:
    print("Replication is running")
 
connection.close()