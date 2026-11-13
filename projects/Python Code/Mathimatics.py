#Parker
#Macomber
#Function Name: readdata
#Description: Reads a set of numbers from an input file.
#Parameter: file_name-Name of the input file.
#Returns list of numbers.
import math
def readdata(file_name):
    infile=open(file_name, "r")
    infileList=[]
    for line in infile:
        infileList.append(int(line.strip('\n')))

    infile.close()
    return infileList

def compute_sum(file_name):
    my_list=readdata(file_name)
    compute_sum=sum(my_list)
    return compute_sum

def compute_mean(file_name):
    my_list=readdata(file_name)
    compute_mean=sum(my_list)/len(my_list)
    return compute_mean

def compute_sd(file_name):
    my_list=readdata(file_name)
    mean=compute_mean(file_name)
    Sum=0
    for i in my_list:
        Sum +=(i-mean)**2
    compute_sd=math.sqrt(Sum/(len(my_list)-1))
    
    return compute_sd

def write_result(file_name, compute_sum, compute_mean, compute_sd):
    outfile=open(file_name, "w")
    print("Sum is: ","{:.2f}".format(compute_sum), file=outfile)
    print("Mean is ","{:.2f}".format(compute_mean), file=outfile)
    print("Standard Deviation: ",round(compute_sd,2), file=outfile)
    outfile.close()
    return outfile

def main():
    inputfile=input("What is the input file? ")
    outputfile=input("What is the output file? ")
    Sum=compute_sum(inputfile)
    mean=compute_mean(inputfile)
    sd=compute_sd(inputfile)
    result=write_result(outputfile, Sum, mean, sd)
    print(result)
