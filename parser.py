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


# symbol: constans, operators, ids, keywords
# symbol_table = {symbol : symbol_class}
# ej) {Const symbolConstant,
#       + symbolAdd,
#       - symbolSub,
#       * symbolMul,
#       / symbolDiv,
#       ^ symbolPower,
#       % symbolMod,
#       (end) symbolConstant
#       }

symbol_table = {}

names = {"+":"Add","-":"Sub","*":"Mul","/":"Div",
        "^":"Power","%":"Mod"}


def symbol(id, bp=0):

    """Crea una clase para el token dado su id y bp, solo si es necesario,
     si ya existe una clase no se hace nada.

    Parámetros:
    id -- identificador, simbolo
    bp -- binding power

    Return:
    Clase_base -- Clase de ese símbolo. Clase_base es una proto-clase, un modelo.
            Por ejemplo si el token es "+" base será la clase del token +
            o lo que es lo mismo la clase del operador Add, si el token fuera *
            sería la clase operatorMul. Por ello se cambia el nombre de la clase.
    """

    try:
        Clase_base = symbol_table[id]
    except KeyError:

        class Clase_base:

            def __init__ (self):
                self.value = None
                self.id = id

            def led (self,left):
                self.first = left
                if self.id in ["^","%"]:
                    self.second = parse(bp-1)
                else:
                    self.second = parse(bp)
                return self

            def __repr__(self):
                if self.value:
                    return "(Const %s)" % self.value
                else:
                    return "(%s %s, %s)" % (names[self.id], self.first, self.second)
        
        try:
            Clase_base.__name__ = "symbol" + names[id]
        except KeyError:
            Clase_base.__name__ = "symbolConstant"

        Clase_base.lbp = bp
        symbol_table[id] = Clase_base

    return Clase_base


symbol("Const")
symbol("+", 10); symbol("-", 10)
symbol("*", 20); symbol("/", 20)
symbol("^", 30); symbol("%",30)
symbol("(end)")


# nud method -> constants, + , -

def prefix(id, bp):
    """
    UnarySub(-1) y UnaryAdd(+1)
    """
    def nud(self):
        self.first = parse(bp)
        self.second = None
        return self
    symbol(id).nud = nud

prefix("+", 100); prefix("-", 100)
symbol("Const").nud = lambda self: self


def tokenize(program):

    """Obtiene los tokens de un trozo de código.
    Ver regex.

    clase_token: Clase del token. Ver estructura de symbol_table. Cada token tiene asociado una clase
    en symbol_table, las constantes tienen la clase symbolConst, el operador + tiene symbolAdd ...
    
    atomo = instancia de la clase del token. Si el token es "+" atomo será una instancia de la clase
    correspondiente a ese token que es operatorAdd.
    """

    regex = r'\w+|[+/*-^<>%(|)]|"<-"|"and"|"or"|"not"|\".\"'

    for token in re.findall(regex, program):
        if token.isnumeric():
            clase_token = symbol_table["Const"]
            atomo = clase_token()
            atomo.value = token
            yield atomo
        else:
            clase_token = symbol_table[token]
            atomo = clase_token()
            if not clase_token:
                raise SyntaxError("Unknown token: %r" % token)
            yield atomo

    symbol = symbol_table["(end)"]
    yield symbol()


def parse(rbp=0):

    """
    Pratt parser implementation.
    See "Top Down Operator Precedence" (section 3: Implementation, pág 47)

    rbp = right binding power. value of the expression's right part
    lbp = left binding power. value of the expression's left part
    ta = current token
    left = expression's left side
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
    print (program, "-> Expression",tree,"\n")

# Samples

test("+1")
test("-1")
test("1")
test("-1+1")
test("1+2+4")
test("1+2+3-56")
test("1+2*3")
test("1*2+3")
test("2/4+1*3")
test("5+2*3+4/2-1")
test ("10%2*10%4+7")
test("3+2^5*2")


# Check:
# test("1+2*3+4/2-1")
# (Sub (Add (Add (Const 1) (Mul (Const 2) (Const 3))) (Div (Const 4) (Const 2))) (Const 1))

# Python 2.x
#>>> import compiler 
#>>> compiler.parse("1+2*3+4/2-1", "eval")
# Expression(Sub((Add((Add((Const(1), Mul((Const(2), Const(3))))), Div((Const(4), Const(2))))), Const(1))))
