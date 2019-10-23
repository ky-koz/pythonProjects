#
# Python:   3.8.0
#
# Author:   Kyla M. Kozole
#
# Purpose:  The Tech Academy- Python Course, creating our first program together.
#           Demonstrating how to pass variables from function to function
#           while producing a functional game.
#
#           Remember, function_name(variable) _means that we pass in the variable
#           return variable_means that we are returning the variable to
#           back to the calling function.


def start():
    print("Hello, {}!".format(get_name()))

def get_name():
    name = input("What is your name? ")
    return name





    



if __name__ == "__main__":
    start()
