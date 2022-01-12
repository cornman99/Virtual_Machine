from os import curdir
from os.path import join as pjoin

from http.server import BaseHTTPRequestHandler, HTTPServer

class StoreHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/json')
        self.end_headers()
        self.wfile.write("group2 sending from the server".encode())
        path = '/group2_servervol/sent.txt'
        f = open(path, 'w')
        f.write("group2 sending from the server")
        f.close()        
                
server = HTTPServer(('', 8080), StoreHandler)
server.serve_forever()

