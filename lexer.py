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


rules = (

    ('stmt', r'\\n\\t|\\n|\\t'),
    ('other',r'\s+|,|;'),
    ('Name', r'[a-zA-Z_][\w_]*'),
    ('operator', r'(<=|>=|<<|>>|!=|<>|::|<-|\*\*)|[:=+\-*%/\^<>\(\)&!}{\[\]|]'),
    ('number', r'(:?\d*\.)?\d+'),
    ('string', r':?\"+\w+\"')
)


regex = re.compile('|'.join(
    "(?P<%s>%s)" % t for t in rules))


class Token():

    def __init__(self, id, value, pos):
        self.id = id
        self.value = value
        self.pos = pos # error handling

    def __repr__(self):
        return "(%s, %s)" % (self.id, self.value)


def lexer (program):

    """Return token list of <program>
    """

    token_list = []

    module = Token("Module", "Module", -1)
    token_list.append(module) 
    i = 0 # position

    def error_handling ():
        # !!! modificar, añadir linea y corregir la cadena de salida
        error_position = i+1
        pointer = program+"\n"+("-"*(i))+"^"
        print (pointer)
        raise SyntaxError("Unexpected character at position %d: `%s`" % (i+1, program[i]))

    for m in regex.finditer(program):
       
        pos = m.start()
        
        if pos > i:
            error_handling()

        i = m.end()
        name = m.lastgroup

        if name == "other":
            continue

        elif name == "stmt":
            id = "%s" % name
            token = Token(id, m.group(0), pos)
        else:
            id = "%s" % name
            token = Token(id, m.group(0), pos)
        
        token_list.append(token)
        # yield token


    if i < len(program):
        error_handling()


    end = Token("(end)", "(end)", pos+1)
    token_list.append(end)
    return token_list



def console ():

    """Interactive console for testing.
    -- commands:
        exit
        clear
    """

    print ("Squanchy PL Lexer Test")
    print ("v1.0\n")
    
    while True:

        expr = input (">> ")
        
        if expr == "exit": exit()
        if expr == "clear": 
            os.system('clear')
            console()
        print (lexer(expr))


if "--console" in sys.argv:
    console()


if "--test" in sys.argv:

    """Benchmark. SQY Lexer vs Python's tokenize module.
    Same code written in SQY and Python: <code.txt> <code_py.txt>
    """

    program = open("code.txt").read()
    program = program.replace("\n","\\n") # !!! mirar si se puede cambiar
    program = program.replace("\t","\\t")

    measure = []
    for i in range(1000):
        start = time.time()
        lexer(program) # real result with print (lexer(program))
        end = time.time()
        measure.append(end-start)

    start = time.time()
    os.system("python -m tokenize code_py.txt")
    end = time.time()

    sqy_time = mean(measure)
    py_time = float(end-start)

    # compare times
    print ("sqy time >>",sqy_time)
    print ("py time >>",py_time)
    print ("how better? =",float(py_time/sqy_time),"times")
    exit()


if "--txt" in sys.argv:

    """Test lexer with input.txt
    """
    f = open("code.txt")
    program = f.read()
    f.close()
    program = program.replace("\n","\\n")
    program = program.replace("\t","\\t")
    print (program,"\n",lexer (program),"\n")


def main ():
    expr = input (">> ")
    tl = lexer (expr)
    print (tl,"\n")
    for token in tl:
        print (token,"\tid:",token.id,"\tval:",token.value,"\tpos:",token.pos)


if __name__ == "__main__":
    main()

    
