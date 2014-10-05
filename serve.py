from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080

class myHandler(BaseHTTPRequestHandler):

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type", "text/html")
		self.end_headers()
		jsStr = "<script src=\"//ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js\"></script>"
		self.wfile.write(jsStr)
		jsStr = "<script type='text/javascript'> navigator.setWebSecurityEnabled(false); console.log('Inside interior script'); $.ajax({method:'POST', url:'172.16.3.13:8080', success: function() {console.log('success')}});</script>"
		self.wfile.write("Hello World")
		self.wfile.write(jsStr)
		return 0

	def do_POST(self):
		print "Got post request"



try:
	server = HTTPServer(('',PORT_NUMBER), myHandler)
	print "Server started"

	server.serve_forever();
except Exception, e:
	raise
