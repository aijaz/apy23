# Python 3 server example
from http.server import BaseHTTPRequestHandler, HTTPServer

hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path.endswith(".png") or self.path.endswith(".jpg"):
            self.send_response(200)
            if self.path.endswith(".png"):
                self.send_header("Content-type", "img/png")
            else:
                self.send_header("Content-type", "img/jpeg")
            self.end_headers()
            components = self.path.split("/")
            filename = components[-1]
            file_contents = load_binary(filename)
            self.wfile.write(file_contents)
            # do something with load_binary
            return

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>https://pythonbasics.org</title></head>", "utf-8"))
        self.wfile.write(bytes("<p>Request: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>This is an example web server.</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


def load_binary(filename):
    with open(filename, 'rb') as file_handle:
        return file_handle.read()


if __name__ == "__main__":
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass
