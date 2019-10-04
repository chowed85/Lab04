# Source: https://pymotw.com/2/socket/udp.html

import socket, sys, time, json

host = sys.argv[1]
textport = sys.argv[2]

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
port = int(textport)
server_address = (host, port)



i = 1
while 1:

    while(i<11):  
        x = {
        "name": "John",
        "age": 29+i,
        "city": "New York"
        }

# convert into JSON:
        y = json.dumps(x)
        

#    s.sendall(data.encode('utf-8'))
        s.sendto(y.encode('utf-8'), server_address)
        i= i + 1

s.shutdown(1)

