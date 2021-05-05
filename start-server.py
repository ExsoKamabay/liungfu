import http.server
import socketserver

HOST = str('127.0.0.1')
PORT = int(5050)

Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer((HOST, PORT), Handler) as run:
    print(f"server berjalan -> http://{HOST}:{PORT}")
    run.serve_forever()
