#Name: Jose Melquiades Escobar

def main ():
    #Prompts the user to enter 5 test scores
    score1 = int (input ('Please Enter Test Score 1: ' ))
    score2 = int (input ('Please Enter Test Score 2: ' ))
    score3 = int (input ('Please Enter Test Score 3: ' ))
    score4 = int (input ('Please Enter Test Score 4: ' ))
    score5 = int (input ('Please Enter Test Score 5: ' ))

    #call func to find average score
    averageTestScore = getAverage(score1, score2, score3, score4, score5)

    #call func to determine the letter grades
    letter1 = getLetterGrade (score1)
    letter2 = getLetterGrade (score2)
    letter3 = getLetterGrade (score3)
    letter4 = getLetterGrade (score4)
    letter5 = getLetterGrade (score5)
    letter6 = getLetterGrade (averageTestScore)

    #cal func to display resutls
    showScores(score1, score2, score3, score4, score5, letter1, letter2, letter3, letter4, letter5, averageTestScore, letter6)




#Define a function to calculate the average score:
#this should accept 5 test scores as argument and return the avg
def getAverage(test1, test2, test3, test4, test5):
    averageScore = (test1 + test2 + test3 + test4 + test5)/ 5
    return (averageScore)

#Define a function to determine the letter grade:
#this should accept a test score as argument and return a letter grade
def getLetterGrade (numScore):
    if numScore >= 90:
        letterScore = 'A'
    elif numScore >= 80 and numScore <= 89:
        letterScore = 'B'
    elif numScore >= 70 and numScore <= 79:
        letterScore = 'C'
    elif numScore >= 60 and numScore <= 69:
        letterScore = 'D'
    else:
        letterScore = 'F'
    return (letterScore)

#Define a function to display the results
def showScores (num1, num2, num3, num4, num5, let1, let2, let3, let4, let5, AvgScore, let6):
    print ('')
    print ('score \t numeric grade letter grade')
    print ('-----------------------------------')
    print ('score 1:', format (num1, '.1f'), '\t', let1)
    print ('score 2:', format (num2, '.1f'), '\t', let2)
    print ('score 3:', format (num3, '.1f'), '\t', let3)
    print ('score 4:', format (num4, '.1f'), '\t', let4)
    print ('score 5:', format (num5, '.1f'), '\t', let5)
    print ('-----------------------------------')
    print ('Average score:', AvgScore, '\t', let6)
    


main()
