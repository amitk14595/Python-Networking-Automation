
# Python program to validate an Ip addess created by Amit Kumar


import socket   # socket module provides support for port scanning
import re       # re module provides support for regular expressions

# Make a regular expression for validating an Ip-address

regex = '''^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)\.( 
			25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)'''
	
# Define a function for validate an Ip addess 

def check(Ip): 

	# pass the regular expression 
	# and the string in search() method 
	if(re.search(regex, Ip)): 
		print("Valid Ip address") 
		
	else: 
		print("Invalid Ip address") 
	

# Driver Code 

if __name__ == '__main__' : 
	
	# Enter the Ip address 
	Ip = raw_input ("Enter an IP Address:")
	
	# calling run function 
	check(Ip)

#List for storing port numbers 

port_list = [20,80,8080,445,23,21,22,1700]

#Scanning Port Numbers in the List

for port in port_list:
    data = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result= data.connect_ex((Ip, port))

    if result == 0:
        print('-' * 80)
        print('Port: ', port, 'Open')
        print('-' * 80)
    else:
        print('port: ', port, 'Closed')

#Created by Amit Kumar
