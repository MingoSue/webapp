# 用Python构建一个web服务器必须有这五行代码


# 导入http服务器和CGI模块
from http.server import HTTPServer, CGIHTTPRequestHandler

# 指定一个端口
port = 8080

# 创建一个http服务器
httpd = HTTPServer(('', port), CGIHTTPRequestHandler)

# 显示一条友好的消息，并启动服务器
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

