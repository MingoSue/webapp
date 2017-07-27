import yate
import athletemodel
import cgi

import cgitb
cgitb.enable()

print(yate.start_response('text/html'))
print(yate.do_form('add_timing_data.py', ['athlete_name'], \
                   ['TimeValue'], text='Send'))

