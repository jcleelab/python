import socket
import six

HOST = ''  
PORT = 8899

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


data2 =''
data3 =''
data4 =''
data5 =''
data6 =''

while True:

    data1 = client_socket.recv(128)
    data2 = repr(data1)
    data3 = data1.hex()
    #data3 = data3[12:]
    j=0
    for i in range(int(len(data3)/2)) :
        data4 = data4 +' 0X'+ data3[i*2:i*2+2]
                    
    print(data4)
    data5 = data5 + ','+ data4
    data4=''
    if len(data5)>4096: 
        break
    else:
        continue
 
client_socket.close() 
