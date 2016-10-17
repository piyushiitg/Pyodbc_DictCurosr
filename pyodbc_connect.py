import pyodbc

result = []
connStr = "DRIVER={FreeTDS};SERVER=%s;PORT=%s;UID=%s;PWD=%s;TDS_VERSION=7.2;timeout=%s;Trusted_Connection=no;UseNTLMv2=yes;" \
                    % (<server_ip>, str(<server_port>), <username'>, "<passwd>", <time_out>)

dbconn = pyodbc.connect(connStr, timeout=10)
cursor = dbconn.cursor()
cursor.execute(query)

#Fetch all the columns from cursor        
columns = [column[0] for column in cursor.description]
for row in cursor.fetchall():
    x = dict(zip(columns, row))
    results.append(x)

cursor.close()
dbconn.close()

######################## Output ###################

>>> python pyodbc_connect.py --query "select 1 as cnt"
[{"cnt": 1}]
