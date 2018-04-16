import socket
import re
urllink=input('Input the URL:')
mysock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=re.findall('^http://(.+)/',urllink)
print(host)
hosts=host[0]
mysock.connect((hosts,80))
urls=string('GET',urllink,'HTTP/1.0\r\n\r\n')
cmd=urls.encode()
mysock.send(cmd)
while True:
    data=mysock.recv(512)
    if(len(data)<1):break
    print(data.decode())
mysock.close()
