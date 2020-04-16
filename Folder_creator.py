#Script for creating multiple folder at one click just by using names in the given file. Created by Amit Kumar

#Importing os and time module for supporting script
import os
import time

#Taking path as an Input that where user wish to create folder
path = raw_input("Enter the path where you want to create folders: ")

#Function for creating folders by using name inside the text file 
def createFolders(DIR):
    ''' This function creates folders '''
    #Taking name of the text file from user
    with open(raw_input(str("Please enter the file name you wish to open (For Ex- name.txt):" )),"r") as x:
        for line in x:
            line = line.strip().split()
            filename = "_".join([i for i in line])
            print "Creating folder: " + filename 
            os.mkdir(DIR + filename)

if __name__ == '__main__':
    DIR = path + str('\ ')
    createFolders(DIR)
    
