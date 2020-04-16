#Script for getting ip address of given Domain name or Hostname

#socket, validators and time are supported modules for validating and getting ip
import socket
import validators
import time
from datetime import datetime

#Storing date and time value in variable
dateTimeObj = datetime.now()
day= str(dateTimeObj.day)
month= str(dateTimeObj.month)
year= str(dateTimeObj.year)
hour= str(dateTimeObj.hour)
minute= str(dateTimeObj.minute)


#continiously validating an entered user input and producing output
while True:
    dom = raw_input('Enter Domain Name: ')
    result = validators.domain(dom)
    if result == True:
        print 'Valid Domain'
    else:
        print 'Invalid Domain'
        break
    print 'IP Address of ', dom , 'is' , socket.gethostbyname(dom)
    print ("-" * 80 )

#saving output in an external file
    with open('domainIP.txt', 'a') as output:
            sep = (" ")
            status = output.writelines("IP Address of " + dom + sep + "is: " + socket.gethostbyname(dom) + "\n")
            output.writelines('Date: ' + day + '/' + month + '/' + year + ' ' + 'Time: ' + hour + ':' + minute)
            output.writelines("-" * 80 + "\n")
            time.sleep(2)
        
#Created by Amit Kumar
