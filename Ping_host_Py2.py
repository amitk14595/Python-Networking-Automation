#Script for pinging multiple hosts created by Amit Kumar

#os and time are supported modules for ping and sleep time

import os
import time

#Fetching ip address listed in text file

with open('host.txt') as file:
    result = file.read()
    result = result.splitlines()
    #print (result)

#pinging multiple ip address listed in text file

    for ip in result:
        os.system('cls')     
        print('Pinging now:', ip)
        print('_'*60)
        response = os.system('ping -n 3 {}'.format(ip))

        #print (response)

        if response == 0:
            ping_status= "Host UP"
        else:
            ping_status= "Host Down"
        print('_'*60)

#Saving output in text file 
        with open('outfile.txt', 'a') as outfile:
            sep = ("-")
            status = outfile.writelines(ping_status + sep + str(ip) + "\n")
            outfile.writelines("\n")
        time.sleep(3)

#Created by Amit Kumar
