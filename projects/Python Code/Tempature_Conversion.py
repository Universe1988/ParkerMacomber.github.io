#Parker
#Macomber
#Date: October 12th, 2022
#Description: This program shows tchniques of defining functions, parameterpassing and function invocation

def fahrenToCel(fahren):
    result=(fahren-32)*(5.0/9.0);
    return result

def fahrenTOCelList(fahrenList):
    for i in range(len(fahrenList)):
        fahren=fahrenList[i]
        celsius=(fahren-32)*(5.0/9.0)
        fahrenList[i]=round(celsius,2)

def main():
    fval=float(input("please enter temperature in Fahrenheite: "))
    cval=fahrenToCel(fval)
    print("equivalent temperature in Celsius is {0:0.2f}".format(cval))
               
    fahrenheiteList=[]
    for i in range(5):
        fahren=float(input("Enter temperature in Fahrenheit: "))
        fahrenheiteList.append(fahren)

    fahrenTOCelList(fahrenheiteList)
    print("The converted temperature list")
    print(fahrenheiteList)
