import math
from sympy import diff, symbols, cos, tan,sin
print("[NOTE!!: 2x^2 should be put at 2*x**2, 2x^3 should be put as 2*x**4]")

# Get the mathematical expression from the user
function = input("f(x): ")
# Define the variable symbolically
x = symbols('x')
# Convert the user input into a SymPy expression
f = eval(function)
dfdx = diff(f,x)
interval = input("Interval:     NOTE!!!: seperate the intervals by space and not commas")

theRange = input("Range: ")



#number of iterations that the GSS would run for 
p = 0.38195
otherP = 0.61803


  # split input into a list of strings 
number = interval.split()
    #convert the string to integers 
firstInterval, secondInterval = map(int, number)
    #test split intervaL

#finding the differenciation of the function



#function that gets range 
#def getRange():
#    print("Range requested: " + theRange)

#function that gets the intervals 
def getInterval():
    print("start interval : ", interval)

#to calculate the number of iterations
def numOfIterations():
    try:
        theRange_value = float(theRange)
#        print("range: ", theRange_value)
#        print("secondIn", secondInterval)
 #       print("firstint", firstInterval)
#        print("otherP", otherP)
        if secondInterval-firstInterval != 0:
            NoIterations = math.log( theRange_value/(secondInterval-firstInterval), otherP)
            NoIterations = round(NoIterations)
            return NoIterations
            print("your number of iterations would be ",NoIterations) 
        else: 
            print("thats not a valid one blud")
    except:
        print("enter a valid number as")





#creating a function for the math function 
def getFunction(x):
    return f.subs('x', x)

#test: interval
getInterval()
numOfIterations()

for i in range(1, numOfIterations()+ 1):
    a= firstInterval + 0.38195 * (secondInterval - firstInterval)
    b = firstInterval + 0.61803 * (secondInterval - firstInterval)
    print("a", i, ": ", a, "      b", i, ":", b)

    print("F(a",i,"): ", getFunction(a))
    print("F(b",i,"): ", getFunction(b))

    #else if 
    if getFunction(a) < getFunction(b):
        firstInterval = firstInterval
        secondInterval = b
        print(i, "th interval: [", firstInterval," , ", secondInterval,"]")
    else:
        firstInterval = a
        secondInterval = secondInterval
        print(i, "th interval: [", firstInterval," , ", secondInterval,"]")
        


    



#if fa1< fb1 then fb1 becomes the new b1 interval will firstInterval, b1
#if getFunction(a1)<getFunction(b1):
   # print("interval: [", firstInterval, ", ", secondInterval,"]")
  #  secondInterval = b1

#test out range
#getRange()
