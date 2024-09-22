"""
    Language: Python 3
    IDE: VS Code
    HOW TO RUN: Navigate to where the python project and execute as python {projectname}.py, because python is an interpreted language, an external library is used to "compile" it for an executable.
    Testing was ran with the python command.
    AUTHORS: Rohan Keenoy 
    DATE: 9/21/2024
    DATA STRUCTURES: A pandas dataframe is commonly used in scientific applications, it can be thought of as a N-d array,can have headers, and is structured as the csv is structured. 
    For this project using a dataframe is a no brainer. R has a similar structure. Note: the output rows will show numbers where headers usually are - this does not mean we are saving with headers.
    A dictionary is used to append to rows in a dataframe. This generated per row-entry. 
    EXTERNAL files: Only the log file generated from program A is used.
    External preperation: Because python is an interpreted language a software _____ will be used to generate an executable. 
    
    References are the same as project 2 :
    0.)Regex testing on : https://regex101.com/
    Pandas references for converting a column of a dataframe to int from float because of NaN problems (headers are good for any data because of these things):
    1.)https://stackoverflow.com/questions/21287624/convert-pandas-column-containing-nans-to-dtype-int?page=2&tab=scoredesc
    
    Date time help: 
    Create a time object (used for midnight testing):
    2.) https://stackoverflow.com/questions/12291209/how-to-initialize-time-object-in-python
    
    time conversion for strftime():
    3.) https://www.programiz.com/python-programming/datetime/strftime
    
    added references for time handling (since we didn't think we needed it before):
    4.) https://www.tutorialspoint.com/how-to-find-if-24-hrs-have-passed-between-datetimes-in-python#:~:text=To%20find%20out%20if%2024,and%20use%20if%20for%20comparision.
    5.) https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
"""



import warnings
import pandas as pd
import os
import re
from datetime import datetime
#this one is for testing the midnight requirement
from datetime import time

class prog3():
    informMessage = "--------------------------------------------\n Welcome to Software C! \n The objective of this software is to read in a csv file, parse it.\n It allows you to add a new entry with an activity code, people involved, and lets users manually enter their time log, while maintaing project requirements and edge cases. It allows for multiple entries\n  --------------------------------------------"
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
        self.doesSpanMidnight = False
        self.Date1 = 0
        self.Date2 = 0
    #prints start of program
    def displayStartOfProgram(self):
        print(self.informMessage)
        input("\n.....Press Enter to Continue....\n")   
    #gets starting row from csv for data checking
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
    #took from my project B  , add how many ppl invovled
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
    #prints the name and file information of what was found
    def printNames(self):
        isUsersFile = False
        while(isUsersFile==False):
            selection = input(f"Continue with file found in directory with First name: {self.firstName} Last Name: {self.lastName} and class ID: {self.classNum}? If yes, type Y,y,Yes, yes and press enter. If no, type N,n, No and press enter.\n")
            if selection == "Yes" or selection == "Y" or selection == "yes" or selection == "y":
                isUsersFile = True
            elif selection == "No" or selection == "N" or selection == "n":
                print("--------------------------------------------Since this is not your file, program is exiting.--------------------------------------------")
                exit()
            else:
                print("User input not reconized, please try again!")
    #display for activities, took from my project B
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
    # activity code logic, took from my project B
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
                    
    #this code adds the note to a class variable while forcing user to enter a note if D(other) is selected of at least one char. From my project B
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
    #was going to use this but didnt
    def fixTimesUp(time):
        #refernece #3
        return time.strftime("%H:%M")
    #different appending for midnight, from project B
    def spanMidnight(self):
        if self.endTime < self.startTime:
            self.doesSpanMidnight = True
            beforeMidnight = {
                0: self.Date1,
                1: self.startTime,
                2: "23:59",
                3: self.pplInvolved,
                4: self.activityCode,
                5: self.notes
            }
            
            self.df = self.df._append(beforeMidnight, ignore_index=True)
            #print(f"Dataframe after appending:\n {self.df}\n")
            afterMidnight = {
                0: self.Date2,
                1: "00:00",
                2: self.endTime,
                3: self.pplInvolved,
                4: self.activityCode,
                5: self.notes
            }
            self.df = self.df._append(afterMidnight, ignore_index=True)
            #print(f"Dataframe after appending:\n {self.df}\n")
    #https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes
    #checks user input for time and will assign actual time vars
    def userTimeCheck(self,time,endStart):
        if endStart == "start":
            try:
                self.startTime = datetime.strptime(time,"%m/%d/%Y %H:%M")
                return True
            except:
                print("Unable to parse that time, try again")
        elif endStart =="end":
            try:
                self.endTime = datetime.strptime(time,"%m/%d/%Y %H:%M")
                return True
            except:
                print("Unable to parse that time, try again")
        else:
            print("Unable to parse that time, try again")
    #starts the time inputs, gets datetime, took from my project B
    def addStartTime(self):
        hasUserFinished = False
        #startingTime = datetime.now().time()
        #uncomment this to test midnight requirement
        #reference 2
        #startingTime= time(23,50)
        #startingTime = openAppend.fixTimesUp(startingTime)
        while(hasUserFinished==False):
            #https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime reference 5
            userInput = input(f"\n--------------------------------------------\nPlease enter a STARTING time for the activity {self.activityCode} \n Use datetime format: MM/dd/yyyy HH:mm \n")
            formatCorrect = self.userTimeCheck(userInput,"start")
            if formatCorrect:
                hasUserFinished = True
                print(f"Date time {self.startTime} has been accepted.")
                self.getEndTime()
            else:
                print("input could not be processed, try again!")
    #continued from addStartTime, added some logic and function calls for multiple date handling. INSPIRED from project B
    def getEndTime(self):
        hasUserFinished = False
        #startingTime = datetime.now().time()
        #uncomment this to test midnight requirement
        #reference 2
        #startingTime= time(23,50)
        #startingTime = openAppend.fixTimesUp(startingTime)
        while(hasUserFinished==False):
            #https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime
            userInput = input(f"\n--------------------------------------------\nPlease enter a ENDING time for the activity {self.activityCode} \n Use datetime format: MM/dd/yyyy HH:mm \n")
            formatCorrect = self.userTimeCheck(userInput,"end")
            if formatCorrect:
                hasUserFinished = True
                print(f"Date time {self.endTime} has been accepted.")
                self.timeInputValidation()
            else:
                print("input could not be processed, try again!")
                
    
    #time conversions for midnight check
    def getTimesGetDates(self):
        try:
            self.Date1 = self.startTime.strftime("%m/%d/%Y")
            self.Date2 = self.endTime.strftime("%m/%d/%Y")
            self.startTime = self.startTime.strftime("%H:%M")
            self.endTime = self.endTime.strftime("%H:%M")
        except:
            #print("Problem parsing times")
            pass
    #case when it isn't midnight, from project B
    def appendToDf(self):
        #print(f"Data Frame Before Appending: \n {self.df}\n")
        self.spanMidnight()
        if self.doesSpanMidnight == False:
            new_row = {
                0: self.Date1,
                1: self.startTime,
                2: self.endTime,
                3: self.pplInvolved,
                4: self.activityCode,
                5: self.notes
            }
            self.df = self.df._append(new_row, ignore_index=True)
    #time validation for project C requirements
    def timeInputValidation(self):
        #print("in time input validation")
        areYouSure = False
        #case for testing 24 hours
        #https://www.tutorialspoint.com/how-to-find-if-24-hrs-have-passed-between-datetimes-in-python#:~:text=To%20find%20out%20if%2024,and%20use%20if%20for%20comparision. reference 4
        if (self.endTime - self.startTime).total_seconds() > 86400:
            print("That exceeds 24 hours, get some sleep! Or try to input again!")
            self.addStartTime()
        elif (self.endTime - self.startTime).total_seconds() > 14400:
            while areYouSure == False:
                yesOrNo = input(f"Are you sure you have been working for/over 4 hours (240 minutes) on activity code {self.activityCode}? If yes, type Y,y,Yes, yes and press enter. If no, type N,n, No and press enter.\n")
                if yesOrNo == "Yes" or yesOrNo == "Y" or yesOrNo == "yes" or yesOrNo == "y":
                    print(f"\nYou are working hard on Activity {self.activityCode}!\n")
                    areYouSure = True
                    
                elif yesOrNo == "No" or yesOrNo == "n" or yesOrNo == "N":
                    #breaks out of a nested loop, oops it has to go through this code anyways again
                    areYouSure = True
                    self.addStartTime()
                else:
                    print("Input not reconized, try again!")
        else:
            #print("...validating midnight requirements")
            pass
        self.getTimesGetDates()
        self.appendToDf()
        self.saveDf()
                    
    #actually saves the new rows
    def saveDf(self):
        #It is necessary to remove NaNs before saving for formating
        #converts the how many people to ints
        #data cleaning
        try:
            #was getting a future warning for a data type issue since floats in a cloumn were not allowed
            #this might be a problem on newer pandas
            warnings.simplefilter(action="ignore",category=FutureWarning)
            #remove nans
            self.df = self.df.fillna("")  
            #reference 1
            #make this column numeric and not float
            self.df[3] = pd.to_numeric(self.df[3])  
            self.df[3] = self.df[3].fillna(0).astype(int)
            self.df.loc[0:1, 3] = self.df.loc[0:1, 3].replace(0, "")
        except Exception:
            #print("couldn't clean data") 
            pass
        
        #print(f"The added row in the csv is {self.df.tail(1)}")
        self.fileName = f"{self.lastName}{self.firstName}Log.csv"
        self.df.to_csv(self.fileName,index=False,header=False)
        print("--------------------------------------------\n")
        print(f"A record for activity # {self.activityCode} was logged with a start time of {self.startTime}, end time of {self.endTime} on starting date {self.Date1} and ending date {self.Date2} that had {self.pplInvolved} people involved")
        #print(f"CSV appended for {self.lastName,self.firstName} and is in the directory of the program.\n It is called {fileName} and is located at {os.getcwd()}. \n ")
        #print("\n--------------------------------------------" )
    #sees if we continue making records
    def continueLoop(self,newRows):
        doALoop = False
        while doALoop == False:
            userOption = input("Would you like to continue and manually enter another entry? If yes, type Y,y,Yes, yes and press enter. If no, type N,n, No and press enter.\n")
            if userOption == "Yes" or userOption == "Y" or userOption == "yes" or userOption == "y":
                newRows+=1
                return True, newRows
            elif userOption == "No" or userOption == "N" or userOption == "n":
                newRows+=1
                return False, newRows
            else:
                print("Did not reconize user option. Try again!")
    #class driver, changed it up since we needed to possibly add more than one record   
    def driver(self):
        doALoop = True
        newRows = 0
        self.displayStartOfProgram()
        self.getDataFrame()
        self.getStartingRow()
        self.dataCheck()
        while doALoop:
            self.addActivityCode()
            self.addHowMany()
            self.addNote()
            self.addStartTime()
            if self.doesSpanMidnight == True:
                newRows+=1
            doALoop, newRows = self.continueLoop(newRows)
            self.doesSpanMidnight = False
        print("\n--------------------------------------------" )
        #print("how many new rows? ",newRows)
        print(f"The added row(s) in the csv is \n{self.df.tail(newRows)}")
        print(f"CSV appended for {self.lastName,self.firstName} and is in the directory of the program.\n It is called {self.fileName} and is located at {os.getcwd()}. \n ")
        print("\n--------------------------------------------" )
            
        
        
        
        
#getting started with the class
if __name__ == "__main__":
    instance3 = prog3()
    instance3.driver()
    
    
