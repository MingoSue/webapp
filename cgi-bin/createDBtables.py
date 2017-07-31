import pymysql

connection = pymysql.connect(host="localhost",port=3306,user="root", \
                             passwd="root",db="test",charset="utf8")
cursor = connection.cursor()
cursor.execute('DROP TABLE IF EXISTS timing_data')
cursor.execute("""CREATE TABLE timing_data (
               id int primary key auto_increment not null,
               athlete_id INTEGER NOT NULL,
               value TEXT NOT NULL,
               FOREIGN KEY (athlete_id) REFERENCES athletes(id))""")

connection.commit()
connection.close()
