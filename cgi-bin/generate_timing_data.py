import athletemodel
import yate
import cgi

# 以下两行启用Python的CGI跟踪技术
# import cgitb 
# cgitb.enable()
athletes = athletemodel.get_from_store()

# 获取所有表单数据，并放在一个字典中
form_data = cgi.FieldStorage()

athlete_name = form_data['which_athlete'].value

print(yate.start_response())
print(yate.include_header("Coach Kelly's Timing Data"))
print(yate.header('Athlete: ' + athlete_name +
                  'DOB: ' + athletes[athlete_name].dob + '.'))
print(yate.para('The top times for this athlete are:'))
print(yate.u_list(athletes[athlete_name].top3))
print(yate.include_footer({'Home':'/index.html',
                           'Selecte another athlete':'generate_list.py'}))
