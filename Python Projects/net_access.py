'''
import urllib2
def main():
    # open a connection to a URL using urllib2
    webUrl = urllib.urlopen("https://www.youtube.com/user/guru99com")

    # get the result code and print it
    print("result code: " + str(webUrl.getcode()))

    # read the data from the URL and print it
    data = webUrl.read()
    print(data)


if(__name__ == "__main__"):
    main()
 '''

import socket
s = socket.socket()         
host = socket.gethostname() 
port = 12345
s.bind((host, port))

s.listen(5)
while True:
   c, addr = s.accept()
   print('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()