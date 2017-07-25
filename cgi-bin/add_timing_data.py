import os
import cgi
import time
import sys
import yate

# 纯文本发回给等待的web浏览器
print(yate.start_response('text/plain'))

# 查询3个环境变量
addr = os.environ['REMOTE_ADDR']
host = os.environ['REMOTE_HOST']
method = os.environ['REQUEST_METHOD']

# 返回24个字符的字符串，当前时间
cur_time = time.asctime(time.localtime())

# 在标准错误输出上显示查询的数据
print(host + ', ' + addr + ', ' + cur_time + ': ' + method + ': ', \
      end='', file=sys.stderr)

# 将页面输入的数据转换为一个字典
form = cgi.FieldStorage()

for each_form_item in form.keys():
    print(each_form_item + '->' + form[each_form_item].value, \
          end='', file=sys.stderr)
    
print(file=sys.stderr)
print('OK.')
