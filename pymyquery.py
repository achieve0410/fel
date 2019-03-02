import pymysql

## connect to MySQL
conn = pymysql.Connect(host='192.168.0.5', user='wh', password='root',
                    db='driving_score', charset='utf8')

## Create Cursor
curs = conn.cursor()

## execute SQL query
sql = "select * from data;"
curs.execute(sql)

## Fetch data
rows = curs.fetchall()
#print(rows)
#print(rows[0])
print(rows[0][0])

## disconnect to MySQL
conn.close()