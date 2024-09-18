import pandas as pd
import os
class openAppend:
    informMessage = "salkdfjkaldskfj;laksdjflk;asdjf;lkasjdf;lkajsdfl;kjdsfal;kasdjf;lkajsdfl;kj"
    def __init__(self):
        self.df = pd.DataFrame()
        self.fileName = ""
        self.lastName = ""
        self.firstName = ""
        self.classNum = ""
        self.activityCode = ""
        self.date = 0
        self.pplInvolved = 0
        self.notes = ""
        self.startingRow = 0
        self.startTime = 0
        self.endTime = 0
        
        
    def getDataFrame(self):
        validFile = False
        while (validFile == False):
            self.fileName = input("------Please enter the name of the file--------")
            if os.path.exists(self.fileName):
                print("File found, loading")
                validFile = True
            else:
                print("File name does not exist please enter a file name")
        self.df = pd.read_csv(self.fileName, header=None)
    #this function is the data check he talks about, dataframe will return NaN if an elelemnt does not exist, so we check wtih that   
    def dataCheck(self):
        #edge case, checking shape
        if self.df.shape[0] < 2 or self.df.shape[1] < 2:
            print( "Wrong shape")
        #seeing if first 2 cols are populated
        elif pd.isna(self.df.iloc[0,0]) or pd.isna(self.df.iloc[0,1]):
            print("First Row NaNs, incorrect format")
        #checking if second row, first col is populated
        elif pd.isna(self.df.iloc[1,0]):
            print("Class contains NaN, class DNE")
        else:
            self.lastName = self.df.iloc[0, 0]
            self.firstName = self.df.iloc[0,1]
            self.classNum = self.df.iloc[1,0]
            self.printNames()
        
    def printNames(self):
        print(f"last: \n{self.lastName}\n first: \n{self.firstName}\n class:\n{self.classNum}\n")
    def printDf(self):
        print(f"Shape of df is \n {self.df.shape}")
        print(f"DataFrame is:\n{self.df}")
        
    def getStartingRow(self):
        self.startingRow = self.df.shape[0]
        self.startingRow+= 1
        print(f"Starting inputs on row\n{self.startingRow}")
    
    def addDate(self):
        self.date = input("\n Enter a Date, no checking yet:")
    def addActivityCode(self):
        self.activityCode = input("\nEnter an acitvity Code, no checking yet")
    def addNote(self):
        self.notes = input ("\nEnter a note, no checking yet: ")
        
    def addStartTime(self):
        self.startTime = input("\nadd a start time, not checked yet")
    def addEndTime(self):
        self.endTime = input("\nadd an end time, not checked yet")
    
    def addHowMany(self):
        self.pplInvolved = input("\n How many people? not checked yet")
        
        
    def appendToDf(self):
        print(f"Data Frame Before Appending: \n {self.df}\n")
        
        new_row = {
            0: self.date,
            1: self.startTime,
            2: self.endTime,
            3: self.pplInvolved,
            4: self.activityCode,
            5: self.notes
        }
        self.df = self.df._append(new_row, ignore_index=True)
        
        print(f"Dataframe after appending:\n {self.df}\n")
        
        
    def populateDataFrame(self):
        pass
    
    def displayStartOfProgram(self):
        print(self.informMessage)
        input("\n.....Press Enter to Continue....\n")

    


if __name__ == "__main__":
    instance = openAppend()
    instance.displayStartOfProgram()
    instance.getDataFrame()
    instance.dataCheck()
    instance.printDf()
    instance.getStartingRow()
    instance.addActivityCode()
    instance.addHowMany()
    instance.addNote()
    instance.addStartTime()
    instance.addEndTime()
    instance.addDate()
    instance.appendToDf()