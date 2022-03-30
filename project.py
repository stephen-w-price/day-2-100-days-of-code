# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.

# Each person should pay (150.00 / 5) * 1.12 = 33.6

# Format the result to 2 decimal places = 33.60

# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
import math
bill = float(input("How much was the bill? "))

howManyPeople = int(input("How many people are paying? "))

tipPerc = float(input("How much tip percentage would you like to give? ")) / 100 
tipCalc = int(math.ceil(bill / howManyPeople) * tipPerc)
print(tipCalc)
print(f"This is the tip {tipCalc}.")