"""
    Language: Python 3
    IDE: VS Code
    HOW TO RUN: Navigate to where the python project and execute as python {projectname}.py, because python is an interpreted language, an external library is used to "compile" it for an executable.
    Testing was ran with the python command.
    AUTHORS: Rohan Keenoy 
    DATE: 9/21/2024
    DATA STRUCTURES: A pandas dataframe is commonly used in scientific applications, it can be thought of as a N-d array,can have headers, and is structured as the csv is structured. 
    For this project using a dataframe is a no brainer. R has a similar structure. 
    A dictionary is used to append to rows in a dataframe. This generated per row-entry. 
    EXTERNAL files: Only the log file generated from program A is used.
    External preperation: Because python is an interpreted language a software _____ will be used to generate an executable. 
    
    References:
    0.)Regex testing on : https://regex101.com/
    Pandas references for converting a column of a dataframe to int from float because of NaN problems (headers are good for any data because of these things):
    1.)https://stackoverflow.com/questions/21287624/convert-pandas-column-containing-nans-to-dtype-int?page=2&tab=scoredesc
    
    Date time help: 
    Create a time object (used for midnight testing):
    2.) https://stackoverflow.com/questions/12291209/how-to-initialize-time-object-in-python
    
    time conversion for strftime():
    3.) https://www.programiz.com/python-programming/datetime/strftime
"""


import pandas as pd
import os
import re
from datetime import datetime
#this one is for testing the midnight requirement
from datetime import time

class openAppend:
    informMessage = "--------------------------------------------\n Welcome to Software B! \n The objective of this software is to read in a csv file, parse it.\n It allows you to add a new entry with an activity code, people involved, and lets users start and stop a clock for their time log, while maintaing project requirements and edge cases. \n  --------------------------------------------"
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
        
    #This function crawls files in the directory. The file must have 2 captial letters and "Log.csv" 
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
        print(f"last: \n{self.lastName}\n first: \n{self.firstName}\n class:\n{self.classNum}\n")
    #displays DF
    def printDf(self):
        print(f"Shape of df is \n {self.df.shape}")
        print(f"DataFrame is:\n{self.df}")
    #gets the last entered row so we know where to start appending to
    def getStartingRow(self):
        self.startingRow = self.df.shape[0]
        self.startingRow+= 1
        #print(f"Starting inputs on row\n{self.startingRow}")
    
    #this function is for adding date
    def addDate(self):
        #self.date = input("\n Enter a Date, no checking yet:")
        self.data = ""
    #fucntion for displaying activity code functions
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
    #this does case handling for activity code and input validation
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
                    print("Selected 3: Participating in a Canvas discussion")
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

    #this code adds the note to a class variable while forcing user to enter a note if D(other) is selected of at least one char      
    def addNote(self):
        isEntered = False
        if self.activityCode == "D":
            while isEntered == False:
                self.notes = input("\n--------------------------------------------\nYou entered other as an activity, please enter a note less than 80 chars\n--------------------------------------------\n")
                #cannot be an empty null string and must be less than 80 chars
                if len(self.notes) < 80 and len(self.notes) != 0:
                    if "," not in self.notes:
                        isEntered = True
                        print(f"\n--------------------------------------------\nNote input: {self.notes} accepted.")
                    else:
                        print("!!!!--------------------------------------------Comma found in notes, please try again!")
                else:
                    print("!!!!--------------------------------------------Notes bound exceeded > 80 or entered a null string.. Please enter a valid note.  User must enter a note for an other activity selection.")
        else:
            while isEntered == False:
                self.notes = input("\n--------------------------------------------\nUser selected something different than other.\n This means it is optional to include a notes portion\nPlease Enter a note less than 80 chars or just click enter.\n--------------------------------------------\n")
                if len(self.notes) < 80:
                    if "," not in self.notes:
                        isEntered = True
                        print(f"Note input{self.notes} accepted.")
                    else:
                        print("!!!!--------------------------------------------Comma in notes, please try again!")
                else:
                    print("!!!!--------------------------------------------Len is over 80 chars, please try again!")
                    
    #converts time to proper the format
    def fixTimesUp(time):
        #refernece #3
        return time.strftime("%H:%M")
    #this is the appending to dataframe if it is midnight
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
            print(f"The added row in the csv is {self.df.tail(1)}")
    #this is the main time function        
    def addTime(self):
        hasUserFinished = False
        
        startingTime = datetime.now().time()
        #uncomment this to test midnight requirement
        #reference 2
        #startingTime= time(23,50)
        startingTime = openAppend.fixTimesUp(startingTime)
        while(hasUserFinished==False):
            userInput = input(f"\n--------------------------------------------\nCurrent start time for log is {startingTime}\n Please press enter to finish activity.\n")
            nextUserInput = input(f"Are you finished logging for activity {self.activityCode} that started at {startingTime} If yes please select: Y,y,Yes,yes. If no please select N,n,No,no\n")
            if nextUserInput == "Yes" or nextUserInput == "Y" or nextUserInput =="y" or nextUserInput == "yes":
                print(f"\n--------------------------------------------\nYes was selected to finish activity that started at {startingTime}\n--------------------------------------------\n")
                self.startTime= startingTime
                self.addEndTime()        
                hasUserFinished = True
                print(f"\n -----------------------------------------------\n End time for activity {self.activityCode} successfully logged as {self.endTime}")
            elif nextUserInput == "No" or nextUserInput == "N" or nextUserInput =="n" or nextUserInput == "no":
                print(f"No was selected to finish activity {self.activityCode} that started at {startingTime}.") 
            else:
                print("User input is unrecognized.")
    #i had an endTime function so decided to put it here anyways   
    def addEndTime(self):
        #uncomment this to log midnight requirement
        #reference 2
        #self.endTime = time(0,39)
        self.endTime = datetime.now().time()
        self.endTime = startingTime = openAppend.fixTimesUp(self.endTime)
        

    #how many people, also does valdiation
    def addHowMany(self):
        isEntered = False
        while(isEntered == False):
            print("--------------------------------------------")
            self.pplInvolved = input("\n How many people were involved in the activity? Select a positive integer <= 50: \n--------------------------------------------\n")
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
        
    #regular appending function 
    def appendToDf(self):
        #print(f"Data Frame Before Appending: \n {self.df}\n")
        self.spanMidnight()
        if self.doesSpanMidnight == False:
            newRow = {
                0: self.date,
                1: self.startTime,
                2: self.endTime,
                3: self.pplInvolved,
                4: self.activityCode,
                5: self.notes
            }
            self.df = self.df._append(newRow, ignore_index=True)
        
            #print(f"Dataframe after appending new row:\n {self.df.tail(1)}\n")
        
        
    def populateDataFrame(self):
        pass
    #prints the informMessage variable at the start of the program
    def displayStartOfProgram(self):
        print(self.informMessage)
        input("\n.....Press Enter to Continue....\n")
    #saves the DF and appends     
    def saveDf(self):
        #It is necessary to remove NaNs before saving for formating
        #converts the how many people to ints
        #data cleaning if its needed
        try:
            self.df = self.df.fillna("")  
            #reference 1
            self.df[3] = pd.to_numeric(self.df[3], errors='coerce')  
            self.df[3] = self.df[3].fillna(0).astype(int)
            self.df.loc[0:1, 3] = self.df.loc[0:1, 3].replace(0, "",errors = "ignore")
        except Exception:
            pass
        
        print(f"The added row in the csv is: \n {self.df.tail(1)}")
        fileName = f"{self.lastName}{self.firstName}Log.csv"
        self.df.to_csv(fileName,index=False,header=False)
        print("--------------------------------------------\n")
        print(f"An activity for activity # {self.activityCode} was logged with a start time of {self.startTime}, end time of {self.endTime} and had {self.pplInvolved} involved")
        print(f"CSV appended for {self.lastName,self.firstName} and is in the directory of the program.\n It is called {fileName} and is located at {os.getcwd()}. \n Thank you for using our csv setup tool :)")
        print("\n--------------------------------------------" )
               

#driver code
if __name__ == "__main__":
    instance = openAppend()
    instance.displayStartOfProgram()
    instance.getDataFrame()
    instance.getStartingRow()
    instance.dataCheck()
    instance.printDf()
    instance.addActivityCode()
    instance.addHowMany()
    instance.addNote()
    instance.addTime()
    instance.addEndTime()
    instance.addDate()
    instance.appendToDf()
    instance.saveDf()