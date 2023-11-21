import math
from sympy import diff, symbols

# Prompt for user input and provide a note about the correct syntax
print("[NOTE!!: 2x^2 should be put at 2*x**2, 2x^3 should be put as 2*x**4]")

# Get the mathematical expression from the user
function = input("f(x): ")

# Define the variable symbolically
x = symbols('x')

# Convert the user input into a SymPy expression
f = eval(function)  # Be cautious about using eval, ensure user input is safe
dfdx = diff(f, x)

# Get the interval from the user
interval = input("Interval:     NOTE!!!: separate the intervals by space and not commas")

# Get the range from the user
theRange = input("Range: ")

# Constants for the Golden Section Search
p = 0.38195
otherP = 0.61803

# Split input into a list of strings
number = interval.split()
# Convert the string to integers
firstInterval, secondInterval = map(int, number)

# Function that prints the interval
def getInterval():
    print("start interval : ", interval)

# Function to calculate the number of iterations for Golden Section Search
def numOfIterations():
    try:
        theRange_value = float(theRange)
        if secondInterval - firstInterval != 0:
            NoIterations = math.log(theRange_value / (secondInterval - firstInterval), otherP)
            NoIterations = round(NoIterations)
            return NoIterations
        else:
            print("That's not a valid one blud")
    except ValueError:
        print("Enter a valid number.")

# Function to calculate the math function for a given x
def getFunction(x):
    return f.subs('x', x)

# Test: interval
getInterval()
numOfIterations()

# Golden Section Search iterations
for i in range(1, numOfIterations() + 1):
    a = firstInterval + 0.38195 * (secondInterval - firstInterval)
    b = firstInterval + 0.61803 * (secondInterval - firstInterval)
    print("a", i, ": ", a, "      b", i, ":", b)

    print("F(a", i, "): ", getFunction(a))
    print("F(b", i, "): ", getFunction(b))

    # Compare function values and update the interval
    if getFunction(a) < getFunction(b):
        firstInterval = firstInterval
        secondInterval = b
        print(i, "th interval: [", firstInterval, " , ", secondInterval, "]")
    else:
        firstInterval = a
        secondInterval = secondInterval
        print(i, "th interval: [", firstInterval, " , ", secondInterval, "]")
