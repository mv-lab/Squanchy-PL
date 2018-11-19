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
# ej) {Const symbol-Constant,
#       + symbol_+,
#       - symbol_-,
#       * symbol_*,
#        ...
#       (end) symbol_end
#       }

symbol_table = {}

names_map = {"+":"Add","-":"Sub","*":"Mul","/":"Div",
        "**":"Power","%":"Mod","and":"And","or":"Or",
        "|":"Bitor","&":"Bitand","^":"Bitxor",
        "<<":"LeftShift",">>":"RightSift","lambda":"Lambda",
        "if":"IfExp","<":"Compare",">":"Compare",
        "<=":"Compare",">=":"Compare","==":"Compare","!=":"Compare",
        "<>":"Compare","[":"List"}


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
                self.first = self.second = self.third = None
                self.id = id
                try : self.name = names_map[self.id]
                except KeyError: self.name= self.id

            def led (self,left):
                self.first = left
                if self.id in ["^","or","and"]:
                    self.second = parse(bp-1)
                else:
                    self.second = parse(bp)
                return self

            def __repr__(self):
                if self.id == "Name" or self.id == "Const":
                    return "(%s %s)" % (self.id, self.value)
                out = [self.name, self.first, self.second, self.third]
                out = map(str, filter(None, out))
                return "(" + " ".join(out) + ")"
   
        Clase_base.__name__ = "symbol-" + id
        Clase_base.lbp = bp
        symbol_table[id] = Clase_base

    return Clase_base



def advance (id=None):
    global token, value,tipo
    if id and token.id != id:
        raise SyntaxError("Expected %r" % id)
    token = next()


def method(s):
    # decorator
    assert s in symbol_table.values()
    def bind(fn):
        setattr(s, fn.__name__, fn)
    return bind



# Ver https://docs.python.org/3/reference/expressions.html | 6.16. Operator precedence

symbol("Const"); symbol("Name")
symbol("+", 110); symbol("-", 110)
symbol("*", 120); symbol("/", 120)
symbol("**", 140); symbol("%",120)
symbol("(end)")

symbol("[", 150); symbol("(", 150);symbol(")");symbol("]")
symbol("}");symbol("{"); symbol(",");symbol(":"); symbol("=")

symbol("lambda", 20); symbol("if", 20); symbol("else")

symbol("or",30);symbol("and",40)
symbol("|", 70); symbol("^", 80); symbol("&", 90)
symbol("<<", 100); symbol(">>", 100)
symbol("<", 60); symbol("<=", 60)
symbol(">", 60); symbol(">=", 60)
symbol("<>", 60); symbol("!=", 60); symbol("==", 60)


# nud method -> constants, + , -

def prefix(id, bp):
    """
    UnarySub(-1) y UnaryAdd(+1)
    """
    def nud(self):
        self.first = parse(bp)
        self.second = None
        aux = {"+":"UnaryAdd", "-":"UnarySub","not":"Not"}
        self.name = aux[self.id]
        return self
    symbol(id).nud = nud

prefix("+", 130); prefix("-", 130); prefix("not", 50)

symbol("Const").nud = lambda self: self
symbol("Name").nud = lambda self: self



@method(symbol("("))
def nud(self):
    # parenthesized form; replaced by tuple former below
    expr = parse()
    advance(")")
    return expr


@method(symbol("if"))
def led(self, left):
    self.first = left
    self.second = parse()
    advance("else")
    self.third = parse()
    return self


@method(symbol("["))
def led(self, left):
    self.first = left
    self.second = parse()
    advance("]")
    return self


@method(symbol("("))
def led(self, left):
    self.first = left
    self.second = []
    if token.id != ")":
        while 1:
            self.second.append(parse())
            if token.id != ",":
                break
            advance(",")
    advance(")")
    self.name = "FuncCall"
    return self


@method(symbol("lambda"))
def nud(self):
    self.first = []
    if token.id != ":":
        argument_list(self.first)
    advance(":")
    self.second = parse()
    return self

def argument_list(list):
    while 1:
        if token.id != "Name":
            SyntaxError("Expected an argument name.")
        list.append(token)
        advance()
        if token.id != ",":
            break
        advance(",")

# constants

def constant(id):
    @method(symbol(id))
    def nud(self):
        self.id = "(literal)"
        self.value = id
        return self

constant("None")
constant("True")
constant("False")


# displays

@method(symbol("("))
def nud(self):
    self.first = []
    comma = False
    if token.id != ")":
        while 1:
            if token.id == ")":
                break
            self.first.append(parse())
            if token.id != ",":
                break
            comma = True
            advance(",")
    advance(")")
    if not self.first or comma:
        self.name = "Tuple"
        return self # tuple
    else:
        return self.first[0]


@method(symbol("["))
def nud(self):
    self.first = []
    if token.id != "]":
        while 1:
            if token.id == "]":
                break
            self.first.append(parse())
            if token.id != ",":
                break
            advance(",")
    advance("]")
    return self


@method(symbol("{"))
def nud(self):
    self.first = []
    if token.id != "}":
        while 1:
            if token.id == "}":
                break
            self.first.append(parse())
            advance(":")
            self.first.append(parse())
            if token.id != ",":
                break
            advance(",")
    advance("}")
    self.name = "Dict"
    return self



def tokenize_python(program):

    """
    Obtiene los tokens de <program> utilizando el propio módulo de Python tokenize.
    """
    
    import tokenize
    from io import BytesIO
    type_map = {
        tokenize.NUMBER: "Const",
        tokenize.STRING: "Const",
        tokenize.OP: "operator",
        tokenize.NAME: "Name",
    }
    for t in tokenize.tokenize(BytesIO(program.encode('utf-8')).readline):
        try:
            yield type_map[t[0]], t[1]
        except KeyError:
            if t[0] == tokenize.NL:
                continue
            if t[0] == tokenize.ENCODING:
                continue
            if t[0] == tokenize.ENDMARKER:
                break
            else:
                raise SyntaxError("Syntax error")
    yield "(end)", "(end)"


def tokenize(program):

    """
    Instancia 'atom' para la clase asociada a los tokens obtenidos mediante tokenize_python
    (tokenize module). Ver symbol_table.
    """

    for id, value in tokenize_python(program):
        if id == "Const":
            Clase_token = symbol_table[id]
            atom = Clase_token()
            atom.value = value
        else:
            # name or operator
            Clase_token = symbol_table.get(value)
            if Clase_token:
                atom = Clase_token()
            elif id == "Name":
                Clase_token = symbol_table[id]
                atom = Clase_token()
                atom.value = value
            else:
                raise SyntaxError("Unknown operator (%r)" % id)
        yield atom


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
    print (program, "-> ",tree,"\n")

# Samples

test("not 1")
test("not 3+4")
test("not a+3*b")
test("a and b")
test("1 or 2")
test("not a and b or c**4 ")
test("a << b")
test("1 >> 6")
test("x != y")
test("(1+2)*3")
test("1 if 2 else 3")
test("suma(4,5)")
test("lambda a, b, c: a+b+c")
test ("None"); test("True"); test("False")
test("[1,2,3,4,5]")
test("(a,b)")
test("+1")
test("not a")
test("{1: 'one', 2: 'two'}")


# Check:
# test("1+2*3+4/2-1")
# (Sub (Add (Add (Const 1) (Mul (Const 2) (Const 3))) (Div (Const 4) (Const 2))) (Const 1))

# Python 2.x
#>>> import compiler 
#>>> compiler.parse("1+2*3+4/2-1", "eval")
# Expression(Sub((Add((Add((Const(1), Mul((Const(2), Const(3))))), Div((Const(4), Const(2))))), Const(1))))
