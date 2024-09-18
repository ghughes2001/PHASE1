import pandas as pd
import os
class UserInputsToCsv:
    #class variable----these do not change for each new instance of class
    startProgramDisplay = "-------------------------------------------------------------------------------------------------------------------------------\nThis program is for creating a .csv for tracking time spent in the course. \nThe user, when prompted, will create a csv with the last name, firstname, and course number in it.\n That CSV is stored in the same directory as this program.\n ------------------------------------------------------------------------------------------------------------------------------- "
    #constructor, instance vars
    def __init__(self):
        self.lastName =""
        self.firstName=""
        self.classId=""
        self.dataFrame = pd.DataFrame()
    def displayStartOfProgram(self):
        print(self.startProgramDisplay)
        input("\n.....Press Enter to Continue....\n")
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
        
    def displayMemberVariables(self):
        #print(f"last,first,classID: {self.lastName,self.firstName,self.classId}")
        pass
    
    def createDataFrame(self):
        placement = [self.lastName, self.firstName], [self.classId]
        self.dataFrame = pd.DataFrame(placement)
        
    def exportDataFrame(self):
        fileName = f"{self.lastName}{self.firstName}Log.csv"
        self.dataFrame.to_csv(fileName,index=False,header=False)
        print("-------------------------------------------------------------------------------------------------------------------------------\n")
        print(f"CSV created with {self.lastName,self.firstName} and is in the directory of the program.\n It is called {fileName} and is located at {os.getcwd()}. \n Thank you for using our csv setup tool :)")
        print("\n-------------------------------------------------------------------------------------------------------------------------------" )          
        
        
if __name__ =="__main__":
    instance = UserInputsToCsv()
    instance.displayStartOfProgram()
    instance.getNamesAndId()
    instance.displayMemberVariables()
    instance.createDataFrame()
    instance.exportDataFrame()

        