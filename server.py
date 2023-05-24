# server.py - a simple backend server for reminders app 
# that uses HTTP methods to create, read, update, and delete reminders

# python server module
import http.server
import socketserver
import json

# list of reminders objects
reminders = []

# handler for HTTP requests
class RequestHandler(http.server.BaseHTTPRequestHandler): # inherits from BaseHTTPRequestHandler

    # TODO: figure out how to replace absolute paths with relative paths
    
    # override do_GET method to handle GET requests
    def do_GET(self):
        if self.path == '/api/reminders/index.html': # checks for index.html
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open('/Users/joaquinmendoza/VSCode_Projects/CS-210/programs/web/index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/api/reminders/styles.css': # checks for styles.css
            self.send_response(200)
            self.send_header('Content-Type', 'text/css')
            self.end_headers()
            with open('/Users/joaquinmendoza/VSCode_Projects/CS-210/programs/web/styles.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == '/api/reminders/script.js': # checks for scripts.js
            self.send_response(200)
            self.send_header('Content-Type', 'text/javascript')
            self.end_headers()
            with open('/Users/joaquinmendoza/VSCode_Projects/CS-210/programs/web/script.js', 'rb') as file:
                self.wfile.write(file.read())
        else: # checks other paths
            if self.path == 'api/reminders':
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(reminders), 'utf-8'))
            else: # not found
                self.send_response(404) # send 404 status code
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(bytes('Not Found', 'utf-8'))

    # TODO: override do_POST method to create new reminders

    # TODO: override do_DELETE method to delete reminders

    # TODO: override do_PUT method to update reminders
    
# set up server
PORT = 8080

# start server
with socketserver.TCPServer(('', PORT), RequestHandler) as httpd:   # create an instance of TCPServer
    print("Serving at port", PORT)
    httpd.serve_forever() # server will run forever until interrupted
