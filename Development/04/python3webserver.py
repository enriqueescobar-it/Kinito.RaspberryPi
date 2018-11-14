import http.server


PORT= 8089
Handler = http.server.CGIHTTPRequestHandler
httpd = http.server.HTTPServer(("",PORT),Handler)
print("server started")
httpd.serve_forever()
