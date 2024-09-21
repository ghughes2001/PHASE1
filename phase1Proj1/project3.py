import pandas as pd
import os
import re

class prog3():
    informMessage = "blah blah blah project C"
    def __init__(self):
        self.df = pd.DataFrame()
        self.fileName = ""
        self.lastName = ""
        self.firstName = ""
        self.startTime = 0
        self.endTime = 0
        self.activityCode = ""
        self.date = ""
        self.pplInvolved = 0
        self.notes = ""
        self.startingRow = 0
        
        
        
    def getStartingRow(self):
        self.startingRow = self.df.shape[0]
        self.startingRow+= 1
        
    #This function crawls files in the directory. The file must have 2 captial letters and "Log.csv" . I coppied my code from project 2. 
    def getDataFrame(self):
        validFile = []
        #reference 0
        regPat = r'^[A-Z][a-z]+[A-Z][a-z]+Log\.csv$'
        #regPat = r'^[A-Z][a-z]+Log\.csv$'
        count=0
        for file in os.listdir():
            if re.match(regPat,file):
                count +=1
                validFile.append(file)
                
        if count > 1:
            print("several files contain Log.csv, exiting.....")
            exit()
        elif count <1 :
            print("No file containing Log.csv found, exiting......")
            exit()
        else:
            print("Loading CSV.....")
            self.fileName = validFile[0]
            try:
                self.df = pd.read_csv(self.fileName, header=None)
            except:
                print("No data in csv")
                exit()
    #this function is the data check he talks about, dataframe will return NaN if an elelemnt does not exist, so we check wtih that   
    #This is from program B, I took my code over to this program as well.
    def dataCheck(self):
        #edge case, checking shape
        if self.df.shape[0] < 2 or self.df.shape[1] < 2:
            print( "Wrong shape")
            exit()
        #seeing if first 2 cols are populated
        elif pd.isna(self.df.iloc[0,0]) or pd.isna(self.df.iloc[0,1]):
            print("First Row NaNs, incorrect format")
            exit()
        #checking if second row, first col is populated
        elif pd.isna(self.df.iloc[1,0]):
            print("Class contains NaN, class DNE")
            exit()
        else:
            self.lastName = self.df.iloc[0, 0]
            self.firstName = self.df.iloc[0,1]
            self.classNum = self.df.iloc[1,0]
            self.printNames()
    
    def printNames(self):
        isUsersFile = False
        while(isUsersFile==False):
            selection = input(f"Continue with file found in directory with First name: {self.firstName} Last Name: {self.lastName} and class ID: {self.classNum}? If yes, type Y,y,Yes, yes and press enter. If no, type N,n, No and press enter.\n")
            if selection == "Yes" or selection == "Y" or selection == "yes" or selection == "y":
                isUsersFile = True
            else:
                print("--------------------------------------------Since this is not your file, program is exiting.--------------------------------------------")
                exit()
    
    def display(self):
        print("--------------------------------------------ACTIVITY CODES--------------------------------------------")
        print("0 --> Reading Canvas site or textbook\n")
        print("1 --> Studying using a practice quiz\n")
        print("2 --> Taking a scoring quiz\n")
        print("3 --> Participating in a Canvas discussion\n")
        print("4 --> Meeting with your team\n")
        print("5 --> Working on documentation\n")
        print("6 --> Working on designs\n")
        print("7 --> Programming\n")
        print("8 --> Working on a test plan or doing testing\n")
        print("9 --> Studying for the final exam\n")
        print("A --> Conferring with the instructor\n")
        print("B --> Working on a mini-lecture video or reading\n")
        print("C --> Viewing a video or website that is not a mini-lecture\n")
        print("D --> Other If you are doing something that does not fit any of the other categories (explain in notes)\n")
        
    def addActivityCode(self):
        isEntered = False
        while not isEntered:
            self.display()
            self.activityCode = input("\n--------------------------------------------Enter an activity code for what you're working on--------------------------------------------\n")
            match self.activityCode:
                case "0":
                    print("Selected 0: Reading Canvas site or textbook")
                    isEntered = True
                case "1":
                    print("Selected 1: Studying using a practice quiz")
                    isEntered = True
                case "2":
                    print("Selected 2: Taking a scoring quiz")
                    isEntered = True
                case "3":
                    print("Syelected 3: Participating in a Canvas discussion")
                    isEntered = True
                case "4":
                    print("Selected 4: Meeting with your team")
                    isEntered = True
                case "5":
                    print("Selected 5: Working on documentation")
                    isEntered = True
                case "6":
                    print("Selected 6: Working on designs")
                    isEntered = True
                case "7":
                    print("Selected 7: Programming")
                    isEntered = True
                case "8":
                    print("Selected 8: Working on a test plan or doing testing")
                    isEntered = True
                case "9":
                    print("Selected 9: Studying for the final exam")
                    isEntered = True
                case "A":
                    print("Selected A: Conferring with the instructor")
                    isEntered = True
                case "B":
                    print("Selected B: Working on a mini-lecture video or reading")
                    isEntered = True
                case "C":
                    print("Selected C: Viewing a video or website that is not a mini-lecture")
                    isEntered = True
                case "D":
                    print("Selected D: Other (explain in notes)")
                    isEntered = True
                case _:
                    print("!!!!-----Please enter a valid code.-----!!!!")
        
        
        
        
        
        
        
#driver code
if __name__ == "__main__":
    instance3 = prog3()
    instance3.getDataFrame()
    instance3.dataCheck()
    instance3.addActivityCode()
    
    
