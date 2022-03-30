# Instructions:

# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.

promptAge = input("What is your age?")
age= int(promptAge)

days = (90 * 365) - (age * 365)
weeks = (90 * 52) - (age * 52)
months = (90 * 12) - (age * 12)

print(f"You have {days} days left, {weeks} weeks left, and {months} months left.")

