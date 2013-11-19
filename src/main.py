# coding: utf-8

def helloWorld():
    return "Hello World"
    
assert helloWorld() == "Hello World"

def helloYou(name):
    return "Hello " + name

assert helloYou("Itay") == "Hello Itay"

def bottles(num):
    # tempList = range(0,num)
    # tempList.reverse()
    output = ""
    for x in range(1, num)[::-1]:
        output += ("%i bottles of beer on the wall, %i bottles of beer." % (x, x) + 
                   "Take one down, pass it around, %i bottles of beer on the wall...\n" % (x - 1))
    
    return output
    
assert bottles(3) == """2 bottles of beer on the wall, 2 bottles of beer.Take one down, pass it around, 1 bottles of beer on the wall...
1 bottles of beer on the wall, 1 bottles of beer.Take one down, pass it around, 0 bottles of beer on the wall...
"""

def gematria(word):
    mapa = {'a':1, 'b':2, 'c':3} # and so on..
    counter = 0
    for c in word:
        counter += mapa[c]
    return counter

assert gematria("abb") == 5

def palindrome(word):
    return word == word[::-1]
    
assert palindrome("aba") == True
assert palindrome("ima") == False
    
from bottle import route, run, template, view, static_file

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='static')

@route('/')
@view('home')
def index():
    return {}


run(host='localhost', port=8080, reloader=True, debug=True)
