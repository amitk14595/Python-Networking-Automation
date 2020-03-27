import os
import time

with open('host.txt') as file:
    result = file.read()
    result = result.splitlines()
    print (result)

    for ip in result:

        os.system('cls')     
        print('Pinging now:', ip)
        print('_'*60)
        response = os.system('ping -n 5 {}'.format(ip))
        print (response)
        if response==0:
            ping_status= "Host UP"
        else:
            ping_status= "Host Down"

        print('_'*60)
        with open('outfile.txt', 'a') as outfile:
            sep = ("-")
            status = outfile.writelines(ping_status + sep + str(ip) + "\n")
            outfile.writelines("_"*60)
        time.sleep(5)
