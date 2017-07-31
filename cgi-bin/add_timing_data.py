import cgi
import pymysql
import yate
import cgitb
cgitb.enable()
# 纯文本发回给等待的web浏览器
# print(yate.start_response('text/plain'))
print(yate.start_response('text/html'))
# 将页面输入的数据转换为一个字典
form_data = cgi.FieldStorage()

try:
    the_name = form_data['athlete_name'].value
    the_time = form_data['TimeValue'].value

    connection = pymysql.connect(host="localhost",port=3306,user="root", \
                                 passwd="root",db="test",charset="utf8")

    cursor = connection.cursor()
    cursor.execute("""SELECT id FROM athletes WHERE name=%s""",(the_name))
    the_id = cursor.fetchone()[0]

    cursor.execute("""INSERT INTO timing_data (athlete_id, value) VALUES (%s, %s)""",\
                   (the_id, the_time))
    connection.commit()
    connection.close()
    print('OK.')

except KeyError as kerr:
    print(str(kerr) + ' error: must input name and time value!')
print(yate.include_footer({'Home':'/index.html',\
                           'Selecte another athlete':'generate_list.py'}))
