import socket       # Import socket module
import threading    # threading for implementing multithreaded server
import math

def evaluate(eqn):
    a = b = c = 0
    eqn = eqn.split("+")
    elements = []
    for elem in eqn:
        temp = elem.split("-")
        for i in temp:
            elements.append(i.strip())

    for elem in elements:
        if "x^2" in elem:
            elem = elem.replace('x^2', '')
            a = float(elem)
        elif "x" in elem:
            elem = elem.replace('x', '')
            b = float(elem)
        else:
            c = float(elem)
    return findRoots(a, b, c)


def findRoots(a, b, c):
    # If a is 0, then equation is
    # not quadratic, but linear
    if a == 0:
        print("Invalid")
        return -1
    d = b * b - 4 * a * c
    sqrt_val = math.sqrt(abs(d))

    if d > 0:
        return ("Roots are real and different : {} and {}".format(((-b + sqrt_val) / (2 * a)),
                                                                 ((-b - sqrt_val) / (2 * a))))
    elif d == 0:
        return ("Roots are real and same : {}".format((-b / (2 * a))))

    else:  # d<0
        temp = str(-b/(2 * a))
        return ("Roots are complex :{} and {}".format(temp +" +i"+str(sqrt_val), temp +"-i"+str(sqrt_val)))
                                                    
class ClientThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.cSocket = clientsocket
        self.cAddress = clientAddress
        print("New client added: {}".format(clientAddress))

    def run(self):
        while True:
            try:
                # Receive up to 1024 bytes from a peer
                equation = self.cSocket.recv(2048).decode()  # Decode converts bytes to string object.
                if equation in ["Q", "q"]:
                    self.cSocket.send("Quit".encode())   # Encodes string to given encoding ( default = 'utf-8')
                    break
                else:
                    print("Equation received :", equation)
                    result = evaluate(equation)     # Evaluate result.
                    self.cSocket.send(str(result).encode())  # Send result to client.
            except Exception as exc:
                message = "Error : {}".format(exc)
                self.cSocket.send(message.encode())      # Send error message to client if exception occurs.

HOST = "192.168.0.170"  # LOCALHOST = "127.0.0.1" -> Use if running on local machine.
PORT = 8080     # Standard port for TCP request. But any privileged port can be used > 1023

# Create socket object.
# AF_INET -> IPV4 address, SOCK_STREAM - Connection oriented TCP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Set socket options
# SOL_SOCKET -> Request applies to socket layer, SO_REUSEADDR -> Local socket address can be reused.
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((HOST, PORT))
print("Server started")
print("Waiting for client request..")
while True:
    server.listen(5)
    print("Server is up and running")
    clientsock, clientAddress = server.accept()     # Establish connection with client.
    newthread = ClientThread(clientAddress, clientsock)
    newthread.start()       # Start a new client thread.
