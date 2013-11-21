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
    mapa = {'a':1, 'b':2, 'c':3}  # and so on..
    counter = 0
    for c in word:
        counter += mapa[c]
    return counter

assert gematria("abb") == 5

def palindrome(word):
    return word == word[::-1]
    
assert palindrome("aba") == True
assert palindrome("ima") == False
    

def multiplication(n):
    return [[x * y for x in range(1, n + 1)] for y in range(1, n + 1)]

assert multiplication(3) == [[1, 2, 3], [2, 4, 6], [3, 6, 9]]

def letterCount(word):
    dic = {}
    for x in word:
        dic[x] = dic.get(x, 0) + 1
        
    return dic

assert letterCount("abbcccdddd") == {'a':1, 'b':2, 'c':3, 'd':4}

def palindromes(text):
    return [x for x in text.split() if palindrome(x)]

assert palindromes("aba bittib blabla") == ['aba', 'bittib']

def mostCommonWord(text):
    dic = {}
    for word in text.split():
        dic[word] = dic.get(word, 0) + 1

    return max(dic, key=dic.get)

assert mostCommonWord("Toady is my first day with Python. Python is just a great programming language") == "is"

def htmlList(text, ordered):
    if ordered: 
        html = "<ol>" 
    else: 
        html = "<ul>"
    for line in text.split('\n'):
        html += "<li>%s</li>" % line
    if ordered: 
        html += "</ol>" 
    else: 
        html += "</ul>"   
    return html

assert htmlList("a\nb\nc\n", True) == "<ol><li>a</li><li>b</li><li>c</li><li></li></ol>"



from bottle import route, run, template, view, static_file

@route('/static/<path:path>')
def callback(path):
    return static_file(path, root='static')

@route('/')
@view('home')
def index():
    return {}


run(host='localhost', port=8080, reloader=True, debug=True)
