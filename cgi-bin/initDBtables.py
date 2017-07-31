import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', \
                             password='root', db='test', charset='utf8')
cursor = connection.cursor()

import glob
import athletemodel
data_file = glob.glob("../data/*.txt")
athletes = athletemodel.put_to_store(data_file)

for each_ath in athletes:
    name = athletes[each_ath].name
    dob = athletes[each_ath].dob

    cursor.execute("""INSERT INTO athletes (name, dob) VALUES (?, ?)""",
                   (name, dob))
    connection.commit()

    cursor.execute("""SELECT id FROM athletes WHERE name=? AND dob=?""",
                   (name, dob))
    the_current_id = cursor.fetchone()[0]
    for each_time in athletes[each_ath].clean_data:
        cursor.execute("""INSERT INTO timing_data (athlete_id, value)
                       VALUES (?, ?)""", (the_current_id, each_time))
    connection.commit()

connection.close()
