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
#-------------------------------------------------------------------------------


import sys
import re
import os



# old pattern 
# pattern = r"\s*(?:(<=|>=|::|<-|\W)|(\d+(?:\.\d*)?)|\".*\")|([a-zA-Z]\w*)"


rules = (
    ('sep', r'\s+'),
    ('name', r'[a-z][\w_]*'),
    ('operator', r'(<=|>=|<<|>>|::|<-|\*\*)|[:=+\-*%/\^<>\(\)&!,\[\]|]'),
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



class InvalidToken(Exception):
        pass

def lexer (program):

    """Genera los tokens de <program>. Almacena los tokens en <token_list>
    """

    token_list = []

    i = 0 # position

    def error_handling ():

        error_position = i+1
        pointer = ("-"*(i+3))+"^"
        print (pointer)
        raise SyntaxError("Unexpected character at position %d: `%s`" % (i+1, program[i]))

    for m in regex.finditer(program):
       
        pos = m.start()
        
        if pos > i:
            error_handling()

        i = m.end()
        name = m.lastgroup

        if name == "sep": # ojo los \n\t ...
            continue
        else:
            id = "<%s>" % name
            t = Token(id, m.group(0), pos)
        
        token_list.append(t)

    if i < len(program):
        error_handling()

    print (token_list)



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
        lexer(expr)


if "--console" in sys.argv:
    console()

if "--sample" in sys.argv:
    lexer ('a+b*4+"hola"-10/5')

