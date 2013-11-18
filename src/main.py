def helloWorld():
    return "Hello World"
    
def helloYou(name):
    return "Hello " + name

def bottles(num):
    #tempList = range(0,num)
    #tempList.reverse()
    output = ""
    for x in range(1,num)[::-1]:
        output += (" %i bottles of beer on the wall, %i bottles of beer." %(x,x) +
                   "Take one down, pass it around, %i bottles of beer on the wall...\n" %(x-1))
    
    return output
    
assert helloWorld() == "Hello World"
assert helloYou("Itay") == "Hello Itay"

#assert bottles(2) =

print bottles(3)
