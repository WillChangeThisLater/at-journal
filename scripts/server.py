#!/usr/bin/env python3
"""
Simple HTTP Server for Appalachian Trail Updates
"""

import http.server
import socketserver
import os
import urllib.parse
import posixpath

PORT = 8080
# Base directory for static files
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class TrailHandler(http.server.BaseHTTPRequestHandler):
    protocol_version = 'HTTP/1.0'
    
    def log_message(self, format, *args):
        # Log to stderr but keep it clean
        print(f'{self.address_string()} - {format % args}', file=self.stderr)
    
    def do_GET(self):
        parsed_path = urllib.parse.urlparse(self.path)
        path = posixpath.unquote(parsed_path.path)
        
        # Handle root
        if path == '/' or path == '/index.html':
            self.serve_index()
            return
        
        # Handle posts directory
        if path.startswith('/posts/'):
            subpath = path[7:]  # Remove '/posts/' prefix
            if subpath.endswith('.html'):
                self.serve_html_file(subpath)
                return
            if os.path.isdir(os.path.join(BASE_DIR, 'posts', subpath)):
                self.serve_directory(subpath)
                return
        
        # Handle HTML files
        if path.endswith('.html'):
            self.serve_html_file(path)
            return
        
        # Handle directory listings
        if os.path.isdir(os.path.join(BASE_DIR, 'web', path)):
            self.serve_directory(path)
            return
        
        # Return 404 for unknown paths
        self.send_error(404, 'Page not found')
    
    def serve_index(self):
        """Serve the main index page"""
        self.serve_html_file('index.html')
    
    def serve_html_file(self, path):
        """Serve an HTML file"""
        full_path = os.path.join(BASE_DIR, 'web', path)
        
        if os.path.isfile(full_path):
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            with open(full_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, 'File not found')
    
    def serve_directory(self, path):
        """Serve directory listing"""
        full_path = os.path.join(BASE_DIR, 'web', path)
        
        if os.path.isdir(full_path):
            files = sorted(os.listdir(full_path))
            
            self.send_response(200)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.end_headers()
            
            html = '''<!DOCTYPE html>
<html>
<head><meta charset="UTF-8"><title>Directory: {path}</title>
<style>body{font-family:monospace;line-height:1.6;max-width:800px;margin:0 auto;padding:20px}.file{padding:5px;border-bottom:1px solid #ccc}</style>
</head>
<body>
<h1>Directory: {path}</h1>
'''
            for filename in files:
                filepath = os.path.join(full_path, filename)
                link = filename if os.path.isfile(filepath) else filename + '/'
                html += f'<div class="file"><a href="{link}">{filename}</a></div>\n'
            
            html += '''</body>
</html>'''
            
            self.wfile.write(html.encode('utf-8'))
        else:
            self.send_error(404, 'Directory not found')
    
    def format_gopher_listing(self, content):
        """Format Gopher content nicely for HTML display"""
        lines = content.strip().split('\n')
        html = '<pre>'
        for line in lines:
            html += line + '\n'
        html += '</pre>'
        return html


if __name__ == '__main__':
    print(f'Starting HTTP server on port {PORT}')
    print(f'Access via: http://localhost:{PORT}')
    print()
    
    with socketserver.TCPServer(("", PORT), TrailHandler) as httpd:
        try:
            print('Serving at http://localhost:8080')
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")
