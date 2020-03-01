


def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1,var2


def compute():
    go = True
    while go:
        var1,var2 = getInfo() # this makes the loop ask the q's again
        try:
            var3 = int(var1) + int(var2)
            go = False # this ends the loop because correct input was given
        except ValueError as e: 
            print("{}: \n\nYou did not provide a numeric value!".format(e)) # e will show the user's input and the computer's value error message
        except:
            ("\n\nOops, you provided invalid input, program will close now!")
    print("{} + {} = {}".format(var1,var2,var3)) # when the loop is complete this code will run
            


if __name__ == "__main__":
    compute() # this is the function that will be called
