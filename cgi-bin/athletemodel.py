import pymysql

db = 'test'

def get_names_from_store():
    connection = pymysql.connect(host="localhost",port=3306,user="root", \
                             passwd="root",db="test",charset="utf8")
    cursor = connection.cursor()
    results = cursor.execute("""SELECT name FROM athletes""")
    response = [row[0] for row in results.fetchall()]
    connection.close()
    return(response)

def get_namesID_from_store():
    connection = pymysql.connect(host="localhost",port=3306,user="root", \
                             passwd="root",db="test",charset="utf8")
    cursor = connection.cursor()
    cursor.execute("""SELECT name, id FROM athletes""")
    response = cursor.fetchall()
    connection.close()
    return(response)

def get_athlete_from_id(athlete_id):
    connection = pymysql.connect(host="localhost",port=3306,user="root", \
                             passwd="root",db="test",charset="utf8")
    cursor = connection.cursor()

    cursor.execute("""SELECT name, dob FROM athletes WHERE id=%s""",(athlete_id))
    (name, dob) = cursor.fetchone()

    cursor.execute("""SELECT value FROM timing_data WHERE athlete_id=%s""",(athlete_id))

    data = [row[0] for row in cursor.fetchall()]

    response = {'Name': name,
                'DOB': dob,
                'data': data,
                'top3': data[0:3]}
    connection.close()
    return(response)
