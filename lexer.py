#-------------------------------------------------------------------------------
# Copyright (C) 2018 Gabriel Rodriguez Canal
# Copyright (C) 2018 Marcos V. Conde
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 
# Based on:
# https://gist.github.com/eliben/5797351
#-------------------------------------------------------------------------------


import sys
import re
import os
import time
from statistics import mean 


# REGEX

rules = (
    ('stmt', r'\\n\\t|\\n|\\t'),
    ('other',r'\s+|;'),
    ('Name', r'[a-zA-Z_][\w_]*'),
    ('operator', r'(<=|>=|<<|>>|!=|==|<>|::|<-|@|->|\*\*)|[:=+\-*%/\^<>\(\)&!}{\[\]|,.]'),
    ('number', r'(:?\d*\.)?\d+'),
    ('string', r':?\"+[\w\s\W]+?\"'),
    ('cmt',r':?#+[\w\s\W]+?#'))

regex = re.compile('|'.join(
    "(?P<%s>%s)" % t for t in rules))


class Token():

    def __init__(self, id, value, pos):
        self.id = id
        self.value = value
        self.pos = pos # error handling

    def __repr__(self):
        return "(%s, %s)" % (self.id, self.value)


class TokenError(Exception):
    pass

class CmtError(Exception):
    pass

class StrError(Exception):
    pass



def lexer (program):

    """Generator. Generate instance(Token).See token_list and debugging comments.
    """

    module = Token("Module", "Module", -1)
    
    yield module
    #token_list = [] #only for debugging
    #token_list.append(module) #only for debugging
    
    i = 0

    def error_handling ():
        # !!! modificar, añadir linea y corregir la cadena de salida

        pointer = program[:i+1]+"\n"+("-"*(len(program[:i+1])-1))+"^"
        print (pointer)

        if program[i] == "#" :
            raise CmtError("Comment Error.Start comment at position %d but missing enclose # " % (i+1))
        if program[i] == '"' : 
            raise StrError('String Error.Start string at position %d but missing enclose "' % (i+1))
        else: 
            raise TokenError("Unexpected character at position %d: `%s`" % (i+1, program[i]))


    for t in regex.finditer(program):
       
        pos = t.start()
        
        if pos > i:
            error_handling()

        i = t.end()
        name = t.lastgroup

        if name == "other" or name == "cmt":
            continue
        else:
            id = "%s" % name
            token = Token(id, t.group(0), pos)
        
        yield token 
        #token_list.append(token) #only for debugging

    if i < len(program):
        error_handling()

    end = Token("(end)", "(end)", pos+1)
    
    yield end 
    #token_list.append(end) #only for debugging
    #return token_list #only for debugging


def console ():

    """Interactive console for testing. Must change lexer's code, see debugging comments.
    -- commands:
        exit
        clear
    """

    try:
        while True:

            expr = input (">> ")
            
            if expr == "exit": exit()
            if expr == "clear": 
                os.system('clear')
                console()
            print (lexer(expr))

    except SyntaxError:
        print ("ERROR")
        console()


if "--console" in sys.argv:

    print ("Squanchy PL Lexer Test")
    print ("v1.0\n")
    console()


if "--test" in sys.argv:

    """Benchmark. SQY Lexer vs Python's tokenize module.
    Same code written in SQY and Python: <code.txt> <code_py.txt>
    """
    maxSize = 200000
    difSize = 2000
    iterations = int(maxSize / difSize)
    
    program0 = '+1+1+1+1+1'

    measureSQY = []
    measurePY = []
    program = program0
    for i in range(iterations):
        measureSQY.append([])
        measurePY.append([])

        progfile = open("code_py.txt","w")
        progfile.write(program)
        for j in range(1000):
            #Squanchy
            start = time.time()
            print (lexer(program)) # real result with:  print(lexer(program))
            #lexer(program)
            end = time.time()
            measureSQY[i].append(end-start)

            #Python
            start = time.time()
            os.system("python -m tokenize code_py.txt")
            end = time.time()
            measurePY[i].append(float(end-start))


        program = program0 * (i+1)

    sqy_time = list(map(lambda x: mean(x), measureSQY))
    py_time = list(map(lambda x: mean(x), measurePY))

    # compare times
    print ("sqy time >>",sqy_time)
    print ("py time >>",py_time)
    print ("how better? =", list(map(lambda x,y: float(x/y), py_time, sqy_time)),"times")
    exit()
