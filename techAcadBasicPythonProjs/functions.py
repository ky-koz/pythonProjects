
mySentence = 'loves the color'

colorList = ['red', 'blue', 'green', 'pink', 'teal', 'black']

def colorFunction(name):
    lst = []
    for i in colorList:
        msg = "{0} {1} {2}".format(name,mySentence,i)
        lst.append(msg)
    return lst

 

lst = colorFunction('Ky')
for i in lst:
    print(i)

