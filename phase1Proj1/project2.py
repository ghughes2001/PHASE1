import pandas as pd
import os
import re
from datetime import datetime
#this one is for testing the midnight requirement
from datetime import time
class openAppend:
    informMessage = "salkdfjkaldskfj;laksdjflk;asdjf;lkasjdf;lkajsdfl;kjdsfal;kasdjf;lkajsdfl;kj"
    def __init__(self):
        self.df = pd.DataFrame()
        self.fileName = ""
        self.lastName = ""
        self.firstName = ""
        self.classNum = ""
        self.activityCode = ""
        self.date = ""
        self.pplInvolved = 0
        self.notes = ""
        self.startingRow = 0
        self.startTime = 0
        self.endTime = 0
        self.doesSpanMidnight = False
        
        
    def getDataFrame(self):
        validFile = []
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
        #self.date = input("\n Enter a Date, no checking yet:")
        self.data = ""
    def display(self):
        print("--------------ACTIVITY CODE--------------")
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
            self.activityCode = input("\n--------------------Enter an activity code for what you're working on--------------------\n")
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
                    print("Syelected 6: Working on designs")
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

                
    def addNote(self):
        isEntered = False
        if self.activityCode == "D":
            while isEntered == False:
                self.notes = input("\nYou entered other as an activity, please enter a note less than 80 chars\n")
                #cannot be an empty null string and must be less than 80 chars
                if len(self.notes) < 80 and len(self.notes) != 0:
                    if "," not in self.notes:
                        isEntered = True
                        print(f"Note input{self.notes} accepted.")
                    else:
                        print("!!!!-----Comma found in notes, please try again!")
                else:
                    print("!!!!-----Notes bound exceeded > 80 or entered a null string.. Please enter a valid note.  User must enter a note for an other activity selection.")
        else:
            while isEntered == False:
                self.notes = input("User selected something different than other.\n This means it is optional to include a notes portion\nPlease Enter a note less than 80 chars or just click enter.")
                if len(self.notes) < 80:
                    if "," not in self.notes:
                        isEntered = True
                        print(f"Note input{self.notes} accepted.")
                    else:
                        print("!!!!-----Comma in notes, please try again!")
                else:
                    print("!!!!-----Len is over 80 chars, please try again!")
                    
    
    def fixTimesUp(time):
        return time.strftime("%H:%M")
    
    def spanMidnight(self):
        if self.endTime < self.startTime:
            self.doesSpanMidnight = True
            beforeMidnight = {
                0: self.date,
                1: self.startTime,
                2: "23:59",
                3: self.pplInvolved,
                4: self.activityCode,
                5: self.notes
            }
            
            self.df = self.df._append(beforeMidnight, ignore_index=True)
            print(f"Dataframe after appending:\n {self.df}\n")
            afterMidnight = {
                0: self.date,
                1: "00:00",
                2: self.endTime,
                3: self.pplInvolved,
                4: self.activityCode,
                5: self.notes
            }
            self.df = self.df._append(afterMidnight, ignore_index=True)
            print(f"Dataframe after appending:\n {self.df}\n")
            
    def addTime(self):
        hasUserFinished = False
        startingTime = datetime.now().time()
        #uncomment this to test midnight requirement
        #startingTime= time(23,50)
        startingTime = openAppend.fixTimesUp(startingTime)
        while(hasUserFinished==False):
            userInput = input(f"\n-----------------------------------------------\nCurrent start time for log is {startingTime}\n Please press enter to finish activity.")
            nextUserInput = input(f"Are you finished logging for activity that started at {startingTime} If yes please select: Y,y,Yes,yes. If no please select N,n,No,no")
            if nextUserInput == "Yes" or nextUserInput == "Y" or nextUserInput =="y" or nextUserInput == "yes":
                print(f"Yes was selected to finish activity that started at {startingTime}")
                self.startTime= startingTime
                self.addEndTime()        
                hasUserFinished = True
            elif nextUserInput == "No" or nextUserInput == "N" or nextUserInput =="n" or nextUserInput == "no":
                print(f"No was selected to finish activity that started at {startingTime}.") 
            else:
                print("User input is unrecognized.")
            
    def addEndTime(self):
        #uncomment this to log midnight requirement
        #self.endTime = time(0,39)
        self.endTime = datetime.now().time()
        self.endTime = startingTime = openAppend.fixTimesUp(self.endTime)
        print(f"\n -----------------------------------------------\n End time successfully logged as {self.endTime}")
       

    
    def addHowMany(self):
        isEntered = False
        while(isEntered == False):
            print("------------------------------------------------")
            self.pplInvolved = input("\n How many people were involved in the activity? Select a positive integer <= 50: \n")
            try:
                num = int(self.pplInvolved)
                if 0 < num <= 50:
                    self.pplInvolved = int(num)
                    isEntered = True
                    print(f"\nYou entered: {self.pplInvolved} for people involved\n")
                else:
                    print("The number must be between 1 and 50. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a positive integer.")
        
        
    def appendToDf(self):
        print(f"Data Frame Before Appending: \n {self.df}\n")
        self.spanMidnight()
        if self.doesSpanMidnight == False:
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
        
    def saveDf(self):
        #It is necessary to remove NaNs before saving for formating
        #converts the how many people to ints
        #data cleaning
        self.df = self.df.fillna("")  
        self.df[3] = pd.to_numeric(self.df[3])
        self.df[3] = self.df[3].fillna(0).astype(int)
        
        print(self.df)
        fileName = f"{self.lastName}{self.firstName}Log.csv"
        self.df.to_csv(fileName,index=False,header=False)
        print("-------------------------------------------------------------------------------------------------------------------------------\n")
        print(f"CSV created with {self.lastName,self.firstName} and is in the directory of the program.\n It is called {fileName} and is located at {os.getcwd()}. \n Thank you for using our csv setup tool :)")
        print("\n-------------------------------------------------------------------------------------------------------------------------------" )           


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
    instance.addTime()
    instance.addEndTime()
    instance.addDate()
    instance.appendToDf()
    instance.saveDf()