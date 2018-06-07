import socket
import threading
import json
from api import WAVUtil
from http.server import BaseHTTPRequestHandler, HTTPServer

def getJSON(jsonInBytes):
    jsonObject = ""

    try:
        jsonObject = json.loads(jsonInBytes)
    except ValueError:
        print("JSON recebido é inválido.")
        return None

    return jsonObject


def getMainSocket():
    host = socket.gethostname()
    # host = '127.0.0.1'
    port = 8080

    print("Hostname: " + host)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    host_port = (host, port)

    # Vincula o host e a porta ao socket criado
    sock.bind(host_port)

    # Numero maximo de coxecoes aceitas antes de recusar
    sock.listen(5)

    return host_port, sock
    

class Handler(BaseHTTPRequestHandler):

    def set_sucess_header(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()

    def do_GET(self):
        print("Entrou GET")
        print(self.path)

        if self.path == '/':
            self.set_sucess_header()
            self.wfile.write(bytes("<html><body><h1>Oláaaaaaa</h1></body></html>", "utf-8"))
            return

        if self.path == '/error':
            # 404: Codigo padrao de resposta para o erro 'Object Not Found'
            self.send_error(404, "Object not found.")
            return

    def do_POST(self):
        print("Entrou POST")
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        jsonObject = getJSON(data)
        print("Conteúdo recebido: " + str(jsonObject))

        if self.path == '/pomodoroSound':
            self.set_sucess_header()
            self.wfile.write(bytes("<html><body><h1>Teste Sound POST OK</h1></body></html>", "utf-8"))
            return
            # bytesSound = jsonObject['bytes_sound']
            # taskName = jsonObject['task_name']
            # pomodoroId = jsonObject['pomodoro_id']
            # soundName = pomodoroId + "." + taskName
            # wavFile = WAVUtil.bytesToWAV(bytesSound, soundName)


class Thread(threading.Thread):

    def __init__(self, host_port, sock):
        threading.Thread.__init__(self)
        self.host_port = host_port
        self.sock = sock
        
        self.daemon = True
        self.start()

    def run(self):
        print("aqui 1")
        httpd = HTTPServer(self.host_port, Handler, False)
        httpd.socket = self.sock
        httpd.server_bind = self.server_close = lambda self: None
        print("aqui 2")
        httpd.serve_forever()
        print("aqui 3")


print(__name__)
if __name__ == '__main__':
    host_port, sock = getMainSocket()
    Thread(host_port, sock)
