#encoding:utf-8
import socket
import sys

def get_constants(prefix):
    return dict((getattr(socket,n),n)
                for n in dir(socket)
                if n.startswith(prefix)
                )

families=get_constants('AF_')
types=get_constants('SOCK_')
protocols=get_constants('IPPROTO_')

#简易连接服务器，省去TCP/IP客户多个步骤
sock=socket.create_connection(('localhost',10000))

print >>sys.stderr,'Family :',families[sock.family]
print >>sys.stderr,'Type :',types[sock.type]
print >>sys.stderr,'Protocol :',protocols[sock.proto]
print >>sys.stderr

try:
        #send data
        message='This is the message.It will be repeated/'
        print >>sys.stderr,'sending "%s"' %message
        sock.sendall(message)

        #look for the response
        amount_received=0
        amount_expected=len(message)

        while amount_received<amount_expected:
            data=sock.recv(16)
            amount_received+=len(data)
            print >>sys.stderr,'received "%s"' %data

finally:
        print >>sys.stderr,'closing socket'
        sock.close()
