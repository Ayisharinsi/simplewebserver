from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
<head>
<title>Sofware companies</title>
</head>
<table align="center" border="2" cellspacing="2" cellpadding="3">
<caption>Top Five Revenue Generating Software Companies</caption>
<tr>
   <th>RANK</th>
   <th>NAME</th>
   <th>REVENU</th>
   <th>PRICE</th>
   <th>COUNTRY</th>
</tr>
<tr>
   <td>1</td>
   <td>Apple</td>
   <td>$385.70 B</td>
   <td>$172.75</td>
   <td>USA</td>
</tr>
<tr>
   <td>2</td>
   <td>Alphabet(Google)</td>
   <td>$307.39 B</td>
   <td>$138.94</td>
   <td>USA</td>
</tr>
<tr>
   <td>3</td>
   <td>Microsoft</td>
   <td>$227.58 B</td>
   <td>0.42%</td>
   <td>USA</td>
</tr>
<tr>
   <td>4</td>
   <td>IBM</td>
   <td>$61.85 B </td>
   <td>$191.73</td>
   <td>USA</td>
</tr>
<tr>
   <td>5</td>
   <td>Oracle</td>
   <td>$51.62 B</td>
   <td>$114.13</td>
   <td>USA</td>
</tr>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()