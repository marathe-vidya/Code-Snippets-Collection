import socket		 	 # Import socket module

SERVER = "192.168.0.170"  # "127.0.0.1" -> Use localhost address when server and client are on same machine.
PORT = 8080  # Port number on which server is listening for request.

# Create a socket object.
# family = AF_INET for the IPv4 protocols, type = SOCK_STREAM for connection oriented TCP protocol.
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((SERVER, PORT))   # Connect to remote address specified (server)
    while True:
        equation = input("Enter a quadratic equation (Ex: 10x^2+25-15) or Q to quit: ")
        client.send(equation.encode())      # Encodes string to given encoding ( default = 'utf-8')
        # Receive up to 2048 bytes
        result = client.recv(2048).decode()     # Decode converts bytes to string object.
        if result == "Quit":
            print("Closing connection..")
            break
        else:
            print("Answer:", result)
    client.close()     # Close the socket.

except (IndexError, ValueError):
    print("Wrong IP Address OR Port number")
