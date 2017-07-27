import cgi
import sqlite3
import yate

import cgitb
cgitb.enable()
# 纯文本发回给等待的web浏览器
print(yate.start_response('text/plain'))

# 将页面输入的数据转换为一个字典
form_data = cgi.FieldStorage()

the_name = form_data['athlete_name'].value
the_time = form_data['TimeValue'].value

connection = sqlite3.connect('coachdata.sqlite')

cursor = connection.cursor()
cursor.execute("""SELECT id FROM athletes WHERE name=?""", (the_name,))
the_id = cursor.fetchone()[0]

cursor.execute("""INSERT INTO timing_data (athlete_id, value) VALUES (?, ?)""",\
               (the_id, the_time))
connection.commit()
connection.close()

print('OK.')
