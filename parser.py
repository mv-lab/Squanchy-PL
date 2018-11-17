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


#  More information:
#  * http://en.wikipedia.org/wiki/Vaughan_Pratt (Original Inventor)
#  * http://en.wikipedia.org/wiki/Pratt_parser (Alias name)
#  * https://eli.thegreenplace.net/2010/01/02/top-down-operator-precedence-parsing
#  * http://effbot.org/zone/simple-top-down-parsing.htm 
#  * http://javascript.crockford.com/tdop/tdop.html
#  * https://gist.github.com/panesofglass/956563

#-------------------------------------------------------------------------------


import sys
import re


class const_token:
    def __init__(self, value):
        self.value = value

    def nud(self):
        return self

    def __repr__(self):
        return "(Const %s)" % self.value

class operator_add:
    lbp = 10; name = "Add"

    def nud(self):
        self.izquierda = parse(100)
        self.name = "UnaryAdd"
        return self

    def led(self, left):
        self.izquierda = left
        self.derecha = parse(10)
        return self

    def __repr__(self):
        if (self.name == "UnaryAdd"):
            return "(%s %s)" % (self.name,self.izquierda)
        else:
            return "(%s %s, %s)" % (self.name,self.izquierda,self.derecha)

class operator_sub:

    lbp = 10; name = "Sub"
    def nud(self):
        self.izquierda = parse(100)
        self.name = "UnarySub"
        return self

    def led(self, left):
        self.izquierda = left
        self.derecha = parse(10)
        return self

    def __repr__(self):
        if (self.name == "UnarySub"):
            return "(%s %s)" % (self.name,self.izquierda)
        else:
            return "(%s %s, %s)" % (self.name,self.izquierda,self.derecha)

class operator_mul:

    lbp = 20
    def led(self, left):
        self.izquierda = left
        self.derecha = parse(20)
        return self

    def __repr__(self):
        return "(Mul %s , %s)" % (self.izquierda, self.derecha)

class operator_div:
    lbp = 20
    def led(self, left):
        self.izquierda = left
        self.derecha = parse(20)
        return self
    def __repr__(self):
        return "(Div %s , %s)" % (self.izquierda, self.derecha)

class operator_power:
    lbp = 30
    def led(self, left):
        self.izquierda = left
        self.derecha = parse(30-1)
        return self
    def __repr__(self):
        return "(Power %s , %s)" % (self.izquierda, self.derecha)

class operator_mod:
    lbp = 30
    def led(self, left):
        self.izquierda = left
        self.derecha = parse(30-1)
        return self
    def __repr__(self):
        return "(Mod %s , %s)" % (self.izquierda, self.derecha)


class end_token:
    lbp = 0


def tokenize(program):
    regex = r'\w+|[+/*-^<>%(|)]|"<-"|"and"|"or"|"not"|\".\"'

    for token in re.findall(regex, program):
        if token.isnumeric():
            yield const_token(int(token))
        elif token == "+":
            yield operator_add()
        elif token == "-":
            yield operator_sub()
        elif token == "*":
            yield operator_mul()
        elif token == "/":
            yield operator_div()
        elif token == "^":
                yield operator_power()
        elif token == "%":
                yield operator_mod()
        else:
            raise SyntaxError("unknown token: %r" % token)
    yield end_token()


def parse(rbp=0):

    """
    Pratt parser implementation.
    See "Top Down Operator Precedence" (section 3: Implementation, pág 47)

    rbp = valor del lado de derecho de la expresion
    lbp = valor del lado izquierdo de la expresion 
    ta = token actual
    """

    global token
    ta = token
    token = next()
    left = ta.nud()

    while rbp < token.lbp:
        ta = token
        token = next()
        left = ta.led(left)
    return left


def test(program):

    global token, next
    # creo el generador tokenize(program)
    # next será el metodo next del generador

    next = tokenize(program).__next__ 
    #tokenize(program)
    token = next()
    tree = parse()
    print (program, "->", tree )


test("+1")
test("-1+1")
test("1+2+3")
test("1+2*3")
test("1*2+3")
test("2/4+1*3")
test("1+2*3+4/2-1")
test ("10%2*10%4+7")
test("3+2^5*2")



# Sample:
# test("1+2*3+4/2-1")
# (Sub (Add (Add (Const 1) (Mul (Const 2) (Const 3))) (Div (Const 4) (Const 2))) (Const 1))
# Python 2.x
#>>> import compiler 
#>>> compiler.parse("1+2*3+4/2-1", "eval")
# Expression(Sub((Add((Add((Const(1), Mul((Const(2), Const(3))))), Div((Const(4), Const(2))))), Const(1))))
