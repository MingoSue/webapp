import yate
import athletemodel
import cgi

import cgitb
cgitb.enable()

print(yate.start_response('text/html'))
print(yate.do_form('add_timing_data.py', ['athlete_name'], \
                   ['TimeValue'], text='Send'))

print(yate.include_footer({'Home':'/index.html',\
                           'Selecte another athlete':'generate_list.py'}))
