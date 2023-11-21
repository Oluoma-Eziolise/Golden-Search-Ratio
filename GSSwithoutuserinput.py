import math
from sympy import diff, symbols
print("[NOTE!!: 2x^2 should be put at 2*x**2, 2x^3 should be put as 2*x**4]")
#function = x^4 - 14*x^3 + 60*x^2 - 70*x
#input("f(x): ")

interval = "0 2"
#input("Interval:     NOTE!!!: seperate the intervals by space and not commas")

theRange = 0.3
#input("Range: ")



#number of iterations that the GSS would run for 
p = 0.38195
otherP = 0.61803


  # split input into a list of strings 
number = interval.split()
    #convert the string to integers 
a0, b0 = map(int, number)
    #test split intervaL

#finding the differenciation of the function



#function that gets range 
#def getRange():
#    print("Range requested: " + theRange)

#function that gets the intervals 
def getInterval():
    print("Interval requested: ", interval)

#to calculate the number of iterations
def numOfIterations():
    try:
        theRange_value = float(theRange)
        if b0-a0 != 0:
            NoIterations = math.log( theRange_value/(b0-a0), p)
            NoIterations = round(NoIterations)
            print("your number of iterations would be ",NoIterations) 
        else: 
            print("thats not a valid one blud")
    except:
        print("enter a valid number as")

#creating a for loop for the number of iterations 
a1 = a0 + p*(b0-a0)
b1 = a0 + (otherP) *(b0 -a0)


print("a1: ", a1,"b1:",b1)

#creating a function for the math function 
def getFunction(x):
    function =  x**4 - 14*x**3 + 60*x**2 - 70*x
    return function


print("Fa1: ", getFunction(a1))
print("Fb1: ", getFunction(b1))


#test out range
#getRange()
#test: interval
getInterval()
numOfIterations()


