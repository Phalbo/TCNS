#!/usr/bin/env python3
"""
Server HTTP locale semplice per vedere l'anteprima dell'HTML
Avvia un server sulla porta 8000
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        url = f"http://localhost:{PORT}/index.html"
        print(f"\n{'='*60}")
        print(f"Server avviato su: {url}")
        print(f"{'='*60}")
        print("\nPremi CTRL+C per fermare il server\n")
        
        # Apri automaticamente il browser
        webbrowser.open(url)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\nServer fermato.")

if __name__ == "__main__":
    main()
