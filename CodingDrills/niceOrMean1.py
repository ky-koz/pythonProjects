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
    print(get_number()) # this built-in fn will call the second fn

    def get_number():
        number = 12 #variable name
        return number



'''
return will output the value back to whatever is calling it
print will output text directly to the screen
'''

    



if __name__ == "__main__":
    start()
