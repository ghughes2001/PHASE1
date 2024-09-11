import pandas as pd

class UserInputsToCsv:
    #class variable----these do not change for each new instance of class
    startProgramDisplay = "asdlk;fjlasdk;jflasdkjflaksdjfsaldk;jf;ladskjfla;skdjflkasdjfl;aksdjfasd;lkfjasd;flkjadsf;lkj"
    #constructor, instance vars
    def __init__(self):
        self.lastName =""
        self.firstName=""
        self.classId=""
        self.dataFrame = pd.DataFrame()
    def displayStartOfProgram(self):
        print(self.startProgramDisplay)
        input("\nPress Enter to Continue\n")
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
        print(f"last,first,classID: {self.lastName,self.firstName,self.classId}")
    
    def createDataFrame(self):
        placement = [[self.lastName, self.firstName, self.classId]]
        self.dataFrame = pd.DataFrame(placement)
        
    def exportDataFrame(self):
        fileName = f"{self.LastName}{self.firstName}.csv"
        self.dataFrame.to_csv(fileName)
                    
        
        
if __name__ =="__main__":
    instance = UserInputsToCsv()
    instance.displayStartOfProgram()
    instance.getNamesAndId()
    instance.displayMemberVariables()
    instance.createDataFrame()
    instance.exportDataFrame()

        