import os
import sys
import time

def clearscreen():
    
    os.system('cls' if os.name == 'nt' else 'clear') #clears screen
    
    return 0
    
def getmainmenu(string):
    
    print("1: Input array") #printing main menu
    print("2: Input file")
    print("3: Index array")
    print("4: Wordcount in array")
    print("5: Clear array")
    print("6: Exit program")
    print()
    print("Your current array is: ", string)
    print()
    
def getarray(array):
    
    clearscreen()
    
    if array != 0:
        print("Please clear array")
        time.sleep(5)
        return 0
    
    else:
        array = input("Please enter statement: ").split() #converts user input string into an array
        return array
    
def getfile(array):
    
    clearscreen()
    
    if array != 0:
        print("Please clear array")
        time.sleep(5)
        return 0
    
    else:
        Userfile = input("Please enter file name followed by .txt (example.txt): ")
        with open(Userfile, "r", encoding="utf-8") as file: #Reads User's file and "encoding=utf-8" ensures all characters are the same among all OS
            array = file.read().split() #converts file as a string into an array
        return array
    
def getindex(array):
    
    clearscreen()
    
    index = int(input("Enter number for index: "))
    j = 0
    
    item = array[index - 1] #Finding what word is at the given index
    
    print("The item at index ", index, " is: ", item)
    time.sleep(3)
    
    return 0
    
def getwordcount(array):
    
    clearscreen()
    
    word = input("Enter the word you would like to be counted (No Spaces): ")
    
    j = 0
    wc = 0
    
    length = len(array)
    
    while j < length: #looping through to catch each occurene of the word in the array
        
        print("Occurs at index: ")
        if array[j] == word:
            print( j, ", ")
            wc = wc + 1
            j = j + 1
        else:
            j = j + 1
            
    print("There are ", wc, " iterations of the word ", word, " in your text.")
    time.sleep(3)
    
    return 0
    
def main():
    
    i = 1   #initiating variables
    array = 0
    string = "No array inserted"
    
    while i == 1:    #looping for indication that user has ended program
        
        clearscreen() #clears screen for simplicity
        
        getmainmenu(string)   #calling main menu and getting users input
        userinput = int(input("Input: "))
        

        
        if userinput == 1:   #User input 1 gets array input from user
            array = getarray(array)
            string = " ".join(array)  
            
        elif userinput == 2: #User input 2 gets a file from user
            array = getfile(array)
            string = " ".join(array)
            
        elif userinput == 3: #User input 3 finds the index of an array
            getindex(array)
            
        elif userinput == 4: #User input 4 gets word count
            getwordcount(array)
        
        elif userinput == 5: #User input 5 clears array
            array = 0
            string = "Cleared"
            
        elif userinput == 6: #User input 6 exits the system
            i = 0
            
        else:
            print("Put in valid input") #error checking for valid user input
            time.sleep(5)
    
    clearscreen()
    sys.exit(0) #exit
main()
    
