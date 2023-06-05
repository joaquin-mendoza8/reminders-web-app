# server.py - a simple backend server for reminders app 
# that uses HTTP methods to create, read, update, and delete reminders

# python server module
import http.server
import socketserver
import json
import os
import datetime

# creates agnostic path to cwd (allows server to run on any machine)
working_dir = os.path.dirname(os.path.abspath(__file__))

# list of reminders objects
reminders = []

# reminder object structure
class Reminder:
    def __init__(self, title='', body='', due=None):
        self.title = title
        self.description = body
        self.due = due

# handler for HTTP requests
class RequestHandler(http.server.BaseHTTPRequestHandler): # inherits from BaseHTTPRequestHandler

    base = '/api/reminders' # base endpoint for all requests

    # override do_GET method to handle GET requests
    def do_GET(self):
        if self.path == RequestHandler.base + '/index.html': # checks for index.html
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            with open(working_dir + '/index.html', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == RequestHandler.base + '/styles.css': # checks for styles.css
            self.send_response(200)
            self.send_header('Content-Type', 'text/css')
            self.end_headers()
            with open(working_dir + '/styles.css', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == RequestHandler.base + '/script.js': # checks for scripts.js
            self.send_response(200)
            self.send_header('Content-Type', 'text/javascript')
            self.end_headers()
            with open(working_dir + '/script.js', 'rb') as file:
                self.wfile.write(file.read())
        elif self.path == RequestHandler.base: # checks for reminders database
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(reminders), 'utf-8'))
        else: # not found/invalid path
            self.send_response(404) # send 404 status code
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Not Found', 'utf-8'))

    # TODO: override do_POST method to create new reminders
    def do_POST(self):
        if self.path == RequestHandler.base + '/add-reminder':
            content_length = int(self.headers['Content-Length'])
            content = self.rfile.read(content_length)
            content = json.loads(content)
            if 'title' not in content or 'body' not in content:
                self.send_response(400)
                self.send_header('Content-Type', 'text/plain')
                self.end_headers()
                self.wfile.write(bytes('Bad Request', 'utf-8'))
            else:
                reminders.append(self.create_reminder)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(bytes(json.dumps(reminders), 'utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(bytes('Error Adding Reminder', 'utf-8'))

    # create new reminder
    def create_reminder(title, body, due):
        return Reminder(title, body, due)
    
    # TODO: override do_DELETE method to delete reminders

    # TODO: override do_PUT method to update reminders
    
# set up server
PORT = 8080

# start server
with socketserver.TCPServer(('', PORT), RequestHandler) as httpd:   # create an instance of TCPServer
    print("Serving at port", PORT)
    httpd.serve_forever() # server will run forever until interrupted
