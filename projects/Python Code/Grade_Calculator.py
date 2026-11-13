#Author: Parker Macomber
def calculate_mean (score1, score2, score3):
    mean = (score1 + score2 + score3) /3
    return mean

def find_letter_grade (mean):

    if mean > 100:
      letter_grade = 'Undefined'  
    elif mean >= 90:
        letter_grade = 'A'
    elif mean >= 80:
        letter_grade = 'B'
    elif mean >= 70:
        letter_grade = 'C'
    elif mean >= 60:
        letter_grade = 'D'
    elif mean >= 0:
        letter_grade = 'F'
    else:
        letter_grade = 'Undefined'

    return letter_grade

def main():
    
    print ('This program will calculate the mean of three test grades and')
    print ('convert the mean into a letter grade')
    print ('=============================================================')

    # Use tr/except block to catch errors
    try:
        score1 = int (input ('Enter score 1: '))
        score2 = int (input ('Enter score 2: '))
        score3 = int (input ('Enter score 3: '))

        mean = calculate_mean (score1, score2, score3)

        letter_grade = find_letter_grade (mean)

        print ('Your mean score is {0:0.3f}'.format (mean))

        print ('Your letter grade is:', letter_grade)

    except ValueError as err:
        print ('One of you score is non-numerical')
        print ('Please try again with correct scores')

    except:
        print('unkown error')
