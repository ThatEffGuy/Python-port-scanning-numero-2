#import sockets module
import socket

#import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#target
target = input(' what IP address do you want to scan?: ')

#getting the IP address by using gethostbyname function

t_IP = socket.gethostbyname(target)
print("starting can on host:", t_IP)

def port_scan(port):
    try:
        s.connect((t_IP, port))
        return True
    except:
        return False

port = int(input("enter the port number to be scanned: "))

if port_scan(port):
    print('Port', port, 'is open')
else:
    print("port", port, "is closed")
