import athletemodel
import yate
import cgi

# 以下两行启用Python的CGI跟踪技术
import cgitb 
cgitb.enable()

# 获取所有表单数据，并放在一个字典中
form_data = cgi.FieldStorage()

athlete_name = form_data['which_athlete'].value

athlete = athletemodel.get_athlete_from_id(athlete_name)

print(yate.start_response())
print(yate.include_header("NUAC's Timing Data"))
print(yate.header('Athlete: ' + athlete['Name'] +
                  ' DOB: ' + athlete['DOB'] + '.'))
print(yate.para('The top times for this athlete are:'))
print(yate.u_list(athlete['top3']))
print(yate.para('The entire set of timing data is: ' + str(athlete['data']) \
                + '(duplicates removed).'))
print(yate.include_footer({'Home':'/index.html',\
                           'Selecte another athlete':'generate_list.py', \
                           'Add time data':'test_form.py'}))
