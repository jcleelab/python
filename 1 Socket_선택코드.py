import socket

HOST = ''  
PORT = 8899

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))


data2 =''
data3 =''
data4 =''
data5 =''

while True:

    data1 = client_socket.recv(128)
    data2 = repr(data1)
    data3 = data1.hex()
    data3 = data3[12:]

    Ed=''
    for i in range(int(len(data3)/2)) :
        Ed = data3[i*2:i*2+12]
        if (Ed[0:2] == '00') and (Ed[2:10] =='00000000') and (Ed[10:12] != '00') and len(Ed[10:12])>1:

            data3 = data3.replace(Ed,'')

    DD=''
    for i in range(int(len(data3)/2)) :
        DD = data3[i*2:i*2+2]
        if  DD =='2e' or DD =='11' or DD =='a1' or DD =='b0':
            #print('\033[38;5;'+data4[3:5]+'m'+',0X'+ DD + data4 + '\033[0m')
            if data4[3:5]=='40' and DD=='11':
            #if data4[3:5]=='40':
            #if DD =='a1' or DD =='b0':

                print('\033[38;5;'+data4[3:5]+'m'+',0X'+ DD + data4 + '\033[0m')

            data5 = data5 + ','+ data4
            data4=''
        else:
            data4 = data4 +' 0X'+ DD


    if len(data5)>256: 
        break
    else:
        continue

f = open('helloClient.txt', 'w')
f.write(repr(data5))
f.close()   
client_socket.close() 

