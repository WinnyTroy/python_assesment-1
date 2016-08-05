# Question:
# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Hints:
# Use __init__ method to construct some parameters

# Solution:

class InputOutString(object):
    def __init__(self, input_str):
        self.input = input_str

    def getString(self):
        str = input("")

    def printString(self):
        return self.getString()

user = input("")
cl = InputOutString(user)
cl.printString()