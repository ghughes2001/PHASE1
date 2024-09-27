"""
    Language: Python 3
    IDE: VS Code
    HOW TO RUN: Navigate to where the python project and execute as python {projectname}.py, because python is an interpreted language, an external library is used to "compile" it for an executable.
    So you can either run the script or click on the executable. It was produced with a library called pyinstaller and ran with this command:
    python c:.users.rohan.appdata.local.packages.pythonsoftwarefoundation.python.3.12_qbz5n2kfra8p0.localcache.local-packages.python312.site-packages.pyinstaller. --onefile {project1,2,3}.py
    Where the periods are forward slashes. (unicode parsing problem if leaving path in multi line comment)
    AUTHORS: Rohan Keenoy 
    DATA STRUCTURES: A pandas dataframe is commonly used in scientific applications, it can be thought of as a N-d array,can have headers, and is structured as the csv is structured. 
    For this project using a dataframe is a no brainer. R has a similar structure. 
    A dictionary is used to append to rows in a dataframe. This generated per row-entry. 
    EXTERNAL files: Only the log file generated from program A is used.
    External preperation: Because python is an interpreted language a software _____ will be used to generate an executable. 
    
    References:
    This program is pretty easy/self explanatory for those who regularly work with csv data, no references were needed.
"""

import pandas as pd
import os
#time here is used for waiting at the end of program for executable
import time
class UserInputsToCsv:
    #class variable----these do not change for each new instance of class
    startProgramDisplay = "-------------------------------------------------------------------------------------------------------------------------------\nWelcome to software A! \nThis program is for creating a .csv for tracking time spent in the course. \nThe user, when prompted, will create a csv with the last name, firstname, and course number in it.\n That CSV is stored in the same directory as this program.\n ------------------------------------------------------------------------------------------------------------------------------- "
    #constructor, instance vars
    def __init__(self):
        self.lastName =""
        self.firstName=""
        self.classId=""
        self.dataFrame = pd.DataFrame()
    #displays the message for start of program
    def displayStartOfProgram(self):
        print(self.startProgramDisplay)
        input("\n.....Press Enter to Continue....\n")
    #gets name and ID
    def getNamesAndId(self):
        self.lastName = input("Enter your last name: ")
        self.firstName = input("Enter your first name: ")
        self.classId = input("Enter class ID: ")
        if (self.classId != "CS 4500"):
            isClassId = False
            while (isClassId == False):
                self.classId = input("Please enter a class ID (CS 4500): ")
                if self.classId == "CS 4500":
                    isClassId = True
    #used for making sure member vars are proper
    def displayMemberVariables(self):
        #print(f"last,first,classID: {self.lastName,self.firstName,self.classId}")
        pass
    #creates the data frame, adds last name, first on row 1, classID on row 2.
    def createDataFrame(self):
    
        placement = [self.lastName, self.firstName], [self.classId]
        self.dataFrame = pd.DataFrame(placement)
    #exports to current directory  
    def exportDataFrame(self):
        fileName = f"{self.lastName}{self.firstName}Log.csv"
        self.dataFrame.to_csv(fileName,index=False,header=False)
        print("-------------------------------------------------------------------------------------------------------------------------------\n")
        print(f"CSV created with {self.lastName,self.firstName} and is in the directory of the program.\n It is called {fileName} and is located at {os.getcwd()}. \n Thank you for using our csv setup tool :)")
        print("\n-------------------------------------------------------------------------------------------------------------------------------" )          
        
#main driver       
if __name__ =="__main__":
    instance = UserInputsToCsv()
    instance.displayStartOfProgram()
    instance.getNamesAndId()
    instance.displayMemberVariables()
    instance.createDataFrame()
    instance.exportDataFrame()
    
    #I put this here so the file doesn't immidetaly close in the executable. 
    endIt = input("\nPress enter to end the program. (program will immediatly exit without this in here)")    
    if endIt:
        print("Enter pressed == thank you!")
        time.sleep()

        