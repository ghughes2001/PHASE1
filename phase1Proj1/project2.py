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
        self.lastEntry = 0
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
        
    def getLastEntry(self):
        self.lastEntry = self.df.iloc[-1]
        print(f"last entry on row\n{self.lastEntry}")
    
    def addDate():
        pass
    def addActivityCode():
        pass
    def addNote():
        pass
    def appendToDf():
        pass
        
        
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
    instance.getLastEntry()