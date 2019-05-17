from http.server import HTTPServer, BaseHTTPRequestHandler


class OurRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()

        response = b''
        if self.path == '/':
            response = b'<h1>Welcome to our website!</h1>'
        elif self.path == '/login':
            response = b'Enter your credentials!'

        self.wfile.write(response)


httpd = HTTPServer(('127.0.0.1', 8080), OurRequestHandler)
httpd.serve_forever()
