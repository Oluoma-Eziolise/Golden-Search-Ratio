import math
print("f(x)= ")
function = input()
print("Interval:     NOTE!!!: seperate the intervals by space and not commas")
interval = input()
print("Range: ")
theRange = input()



#number of iterations that the GSS would run for 
iterationNUmber = 0.61803


  # split input into a list of strings 
number = interval.split()
    #convert the string to integers 
x,y = map(int, number)
    #test split intervaL

  
#function that gets range 
def getRange():
    print("Range requested: " + theRange)

#function that gets the intervals 
def getInterval():
    print("Interval requested: ", interval)

#to calculate the number of iterations
def numOfIterations():
    try:
        theRange_value = float(theRange)
        if y-x != 0:
            NoIterations = math.log( theRange_value/(y-x), iterationNUmber)
            NoIterations = round(NoIterations)
            print("your number of iterations would be ",NoIterations) 
        else: 
            print("thats not a valid one blud")
    except:
        print("enter a valid number as")
    

#test out range
getRange()
#test: interval
getInterval()
numOfIterations()
