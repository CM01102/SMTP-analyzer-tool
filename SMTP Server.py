#From socket module import the required structure and constants
from socket import AF_INET, SOCK_STREAM, socket
#Import library for Mac address
import uuid
#Import library for IP address
import json 

if __name__ == '__main__':
   print("Application started")
   #Creating a TCP/IP socket
   s = socket(AF_INET,SOCK_STREAM)
   print('TCP socket created')
   #Binding the TCP/IP socket to loopback address and port 8877
   s.bind(('127.0.0.1',8877))
   print('Socket is bound to %s:%d' % s.getsockname())
   #Put socket into listening state
   backlog = 0 #Waiting queue size, 0 means no queue
   s.listen(backlog)
   print('Socket %s:%d is in listening state' % s.getsockname())
   #Creating sockets to accept sent data
   client_socket,client_addr = s.accept()
   print('New client connected from %s:%d'% client_addr)
   print ('Local end-point socket bound on: %s:%d'%client_socket.getsockname())
   #Extracting the MAC address 
   print('Mac address: ',hex(uuid.getnode()))
   #Extracting the IP address
   data = r'{"code":"0","msg":"ok","obj":[{"port":"44139","ip":"113.73.67.60"}],"errno":0,"data":[null]}'
   ip = json.loads(data)['obj'][0]['ip']
   print('IP Address: ',ip)
   
   #Server is ready to send and receive
   client_socket.send("220- Service ready".encode())
   
   #Server receives and checks the delivered message
   Msg = client_socket.recv(1024).decode("utf-8")
   if Msg != 'HELO': 
       print("HELO command not received")
   else: 
       print(Msg)
   #Requested command complete
       client_socket.send("250- OK".encode())
   
   Msg1 = client_socket.recv(1024).decode("utf-8")
   if Msg1 != 'MAIL FROM:<bob@gmail.com>':
       print("Sender mail not received")
   else:
       print(Msg1)
       client_socket.send("250- OK".encode())
   
   Msg2 = client_socket.recv(1024).decode("utf-8")
   if Msg2 != "RCPT TO:<alice@gmail.com>":
       print("Recipient mail not received")
   else:
       print(Msg2)
       client_socket.send("250- OK".encode())
   
   Msg3 = client_socket.recv(1024).decode("utf-8")
   if Msg3 != "DATA":
       print("DATA command not received")
   else:
       print(Msg3)
       client_socket.send("354- Start mail input".encode())
   
   Msg4 = client_socket.recv(1024).decode("utf-8")
   if Msg4 != "Subject: SMTP analyzer tool": 
       print("Subject not received")
   else: 
       print(Msg4)
       client_socket.send("250- OK".encode())
       
   Msg5 = client_socket.recv(1024).decode("utf-8")
   if Msg5 != "Email content: Code": 
       print("Email content not received")
   else: 
       print(Msg5)
       client_socket.send("250- OK".encode())
       
   Msg6 = client_socket.recv(1024).decode("utf-8")
   if Msg6 != "<CRLF>.<CRLF>": 
       print("Msg6 not received")
   else: 
       print(Msg6)
       client_socket.send("250- OK".encode())
       
   Msg7 = client_socket.recv(1024).decode("utf-8")
   if Msg7 != "QUIT":
       print("Msg7 not received")
   else: 
       print(Msg7)
       client_socket.send("221- Connection closed".encode())
  
   #Wait for user input before terminating application
   input('Press enter to terminate...')
   client_socket.close()
   s.close()
   print('Closed the client socket')
   print('Terminating...')