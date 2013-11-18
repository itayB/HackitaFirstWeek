def helloWorld():
    return "Hello World"
    
assert helloWorld() == "Hello World"

def helloYou(name):
    return "Hello " + name

assert helloYou("Itay") == "Hello Itay"

def bottles(num):
    #tempList = range(0,num)
    #tempList.reverse()
    output = ""
    for x in range(1,num)[::-1]:
        output += ("%i bottles of beer on the wall, %i bottles of beer." %(x,x) +
                   "Take one down, pass it around, %i bottles of beer on the wall...\n" %(x-1))
    
    return output
    
assert bottles(3) ==  """2 bottles of beer on the wall, 2 bottles of beer.Take one down, pass it around, 1 bottles of beer on the wall...
1 bottles of beer on the wall, 1 bottles of beer.Take one down, pass it around, 0 bottles of beer on the wall...
"""
