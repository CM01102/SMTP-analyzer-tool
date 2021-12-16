#From socket module import the required structure and constants
from socket import AF_INET, SOCK_STREAM, socket
#Import library for MAC address
import uuid
#Import library for IP address
import json

if __name__ == '__main__':
   print("Application started")
   s = socket(AF_INET,SOCK_STREAM)
   print('TCP socket created')
   #No binding needed for clients, OS will bind the socket automatically
   #When connect is issued 
   server_address =('127.0.0.1',8877)
   #Connecting...
   s.connect(server_address)
   print('Socket connected to %s:%d' % s.getpeername())
   print ('Local end-point is bound to %s:%d'%s.getsockname())
   #Extracting the MAC address
   print('Mac address: ',hex(uuid.getnode()))
   #Extracting the IP address
   data = r'{"code":"0","msg":"ok","obj":[{"port":"44139","ip":"113.73.67.60"}],"errno":0,"data":[null]}'
   ip = json.loads(data)['obj'][0]['ip']
   print('IP Address: ',ip)
  
   message = s.recv(1024).decode("utf-8")
   if message[:3] != '220' :
       print ('220 reply not received')
   else: 
       print (message)
   #Helo command starts the SMTP session conversation
   heloCommand = 'HELO'
   s.send(heloCommand.encode())
   
   message1 = s.recv(1024).decode("utf-8")
   if message1[:3] != '250' :
       print ('250 reply not received')
   else:
       print (message1)
   #Command initiates a mail transfer
   mailfromCommand = 'MAIL FROM:<bob@gmail.com>'
   s.send(mailfromCommand.encode())

   message2 = s.recv(1024).decode("utf-8")
   if message2[:3] != '250' :
       print ('250 reply not received')
   else: 
       print (message2)
   #Command specifies the replient
   rcptToCommand = 'RCPT TO:<alice@gmail.com>'
   s.send(rcptToCommand.encode())
   
   message3 = s.recv(1024).decode("utf-8")
   if message3[:3] != '250' :
       print ('250 reply not received')
   else:
       print (message3)
   #Command transfers the mail data
   dataCommand = 'DATaA'
   s.send(dataCommand.encode())
   
   #Sending mail subject to the server 
   message4 = s.recv(1024).decode("utf-8")
   if message4[:3] != '354' :
       print ('354 reply not received')
   else:
       print (message4)
   subject = "Subject: SMTP analyzer tool"
   s.send(subject.encode())

   #Sending mail content to the server
   message5 = s.recv(1024).decode("utf-8")
   if message5[:3] != '250' :
       print ('250 reply not received')
   else:
       print (message5)
   body = "Email content: Code"
   s.send(body.encode())
   
   message6 = s.recv(1024).decode("utf-8")
   if message6[:3] != '250' :
       print ('250 reply not received')
   else:
       print (message6)
   #Termination sequence 
   endCommand = "<CRLF>.<CRLF>"
   s.send(endCommand.encode())
       
   message7 = s.recv(1024).decode("utf-8")
   if message7[:3] != '250' :
       print ('250 reply not received')
   else:
       print (message7)
   #Command sends termination request 
   quitCommand = "QUIT"
   s.send(quitCommand.encode())
   
   message8 = s.recv(1024).decode("utf-8")
   if message8[:3] != '221' :
       print ('221 reply not received')
   else:
       print (message8)
  
   #Wait for user input before terminating application
   input('Press enter to terminate...')
   s.close()
   print('Terminating...')