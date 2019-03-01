import pymysql

## connect to MySQL
conn = pymysql.Connect(host='localhost', user='root', password='6chldnjsgy!@',
                    db='driving_score', charset='utf8')

## Create Cursor
curs = conn.cursor()

## execute SQL query
sql = "SHOW Tables"
curs.execute(sql)

## Fetch data
rows = curs.fetchall()
print(rows)
#print(rows[0])

## disconnect to MySQL
conn.close()