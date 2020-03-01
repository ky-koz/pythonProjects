

def getName(name = ""):
    name = askName(name)
    print("Thank you, welcome {}!".format(name))


def askName(nombre):
    go = True
    while go:
        if nombre == "":
            nombre = input("Please enter your name:\n>>> ")
            if nombre != "":
                go = False
                
    return nombre


if __name__ == '__main__':
    getName()
