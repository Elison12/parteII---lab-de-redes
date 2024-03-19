from http.server import HTTPServer, SimpleHTTPRequestHandler

diretorio = ''

endereco = ('', 8080)
servidor = HTTPServer(endereco, SimpleHTTPRequestHandler)

servidor.serve_forever()