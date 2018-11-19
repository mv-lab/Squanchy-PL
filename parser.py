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


# symbol: constans, operators, ids, keywords
# symbol_table = {symbol : symbol_class}
# ej) {Const symbol-Constant,
#       + symbol_+,
#       - symbol_-,
#       * symbol_*,
#        ...
#       (end) symbol_end
#       }

token_list = []

symbol_table = {}

names_map = {"+":"Add","-":"Sub","*":"Mul","/":"Div",
        "**":"Power","%":"Mod","and":"And","or":"Or",
        "|":"Bitor","&":"Bitand","^":"Bitxor",
        "<<":"LeftShift",">>":"RightSift","lambda":"Lambda",
        "if":"IfExp","[":"List","=":"Assign"}



def symbol(id, bp=0):

    """Crea una clase para el token dado su id y bp, solo si es necesario,
     si ya existe una clase no se hace nada.
    Parámetros:
    id -- identificador, simbolo
    bp -- binding power
    Return:
    Protoclase -- Clase de ese símbolo. Protoclase es una proto-clase, un modelo.
            Por ejemplo si el token es "+" base será la clase del token +
            o lo que es lo mismo la clase del operador Add, si el token fuera *
            sería la clase operatorMul. Por ello se cambia el nombre de la clase.
    """

    try:
        Protoclase = symbol_table[id]
    except KeyError:

        class Protoclase:

            def __init__ (self):
                self.value = None
                self.first = self.second = self.third = None
                self.id = id
                self.arity = 2
                try : self.name = names_map[self.id]
                except KeyError: self.name= self.id

            def led (self,left):
                self.first = left
                if self.id in ["**","or","and","="]: # left asociative operators
                    self.second = parse(bp-1)
                else:
                    self.second = parse(bp)
                return self

            def __repr__(self):
                               
                out = [self.first, self.second, self.third]
                out = map(str, filter(None, out))

                if self.arity == 1:
                    return "(" + self.name +" "+ " ".join(out) + ")"

                elif self.id == "Name" or self.id == "Const":
                    return "(%s %s)" % (self.id, self.value)

                return "(" + self.name + " "+ ",".join(out) + ")"
   
        Protoclase.__name__ = "symbol-" + id
        Protoclase.lbp = bp
        symbol_table[id] = Protoclase

    return Protoclase



def peek (id=None):

    """Genera la instancia el token siguiente según su correspondiente clase.
    Permite comparar el id del siguiente con un id pasado por párametro.

    Párametros:
    id -- id del token que vamos a instanciar (next token). 
        Si id = None simplemente se instanciará el siguiente token.
        Si id tiene un valor, se compmrobará antes de instanciar.
    """

    global token
    if id and token.id != id:
        raise SyntaxError("Expected %r" % id)

    token = next()
   

def method(s):

    """Decorador para simplificar el código referido a los métodos nud y led.
        Añade a la clase <tipo> la función referenciada al decorador, como método. 
    """
    assert s in symbol_table.values()
    def new_method(fn):
        setattr(s, fn.__name__, fn) # (clase, nombre funcion, valor = funcion)
    return new_method



# Ver https://docs.python.org/3/reference/expressions.html | 6.16. Operator precedence

symbol("Const"); symbol("Name")
symbol("Const"); symbol("Name")
symbol("+", 110); symbol("-", 110)
symbol("*", 120); symbol("/", 120)
symbol("**", 140); symbol("%",120)
symbol("(end)"); symbol("=",10)

symbol("or",30);symbol("and",40)
symbol("|", 70); symbol("^", 80); symbol("&", 90)
symbol("<<", 100); symbol(">>", 100)
symbol("<", 60); symbol("<=", 60)
symbol(">", 60); symbol(">=", 60)
symbol("<>", 60); symbol("!=", 60); symbol("==", 60)


symbol("}");symbol("{"); symbol(",");symbol(":"); symbol("=")

symbol("lambda", 20); 


#--------------------------------------------------------------------------------------------
# NUD FUNCTIONS

symbol("Const").nud = lambda self: self
symbol("Name").nud = lambda self: self

# nud method -> + , - , not

def prefix(id, bp):
    """
    Prefix expressions.
    Arity 1 => +,-, not => UnaryAdd, UnaryMinus, Not
    """
    names = {"+":"UnaryAdd", "-":"UnarySub","not":"Not"}
    def nud(self):
        self.first = parse(bp)
        self.name = names[self.id]
        self.arity = 1
        print (">",self.first,self.name)
        return self
    symbol(id).nud = nud

prefix("+", 130); prefix("-", 130); prefix("not", 50)

# Parenthesized Expressions 

symbol("(", 150);symbol(")");

def nud(self):
    expr = parse()
    peek(")")
    return expr
symbol("(").nud = nud


# if-then-else
# if _ then _ else _

symbol("if", 20); symbol("else"); symbol("then",5)

def nud(self):
    self.first = parse(20)
    peek("then")
    self.second = parse(5)
    try: 
        peek("else")
        self.third = parse()
    except SyntaxError:
        pass

    self.arity = 3
    return self

symbol("if").nud = nud


def constant(id,value=None):
    @method(symbol(id))
    def nud(self):
        self.id = "Const"
        self.value = value
        return self


constant("None")
constant("True",1)
constant("False",0)
constant("null")
constant("pi", 3.141592653589793)


#--------------------------------------------------------------------------------------------
# LISTAS

symbol("]"); symbol("[", 150);

@method(symbol("["))
def nud(self):
    lista = []
    if token.id != "]":
        while 1:
            if token.id == "]":
                break
            lista.append(parse())
            if token.id != ",":
                break
            peek(",")
    peek("]")
    self.first = lista
    self.arity = 1
    return self

#--------------------------------------------------------------------------------------------
# FUNCTION CALLS

symbol(")"); symbol(",")

@method(symbol("("))
def led(self, left):

    self.first = left # function name
    
    # if left in Tabla de nombres
    # else raise FuncionNameError as detail funcion + left + is not defined

    self.second = [] # param
    if token.id != ")":
        while 1:
            self.second.append(parse())
            if token.id != ",":
                break
            peek(",")
    peek(")")
    self.arity = "function"
    self.name = "FunCall"
    return self

#--------------------------------------------------------------------------------------------


def tokenize_python(program):

    """
    Genera los tokens de <program> utilizando el propio módulo de Python tokenize.
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
    Genera una instancia 'atom' para la clase asociada al token obtenido mediante tokenize_python
    (tokenize module). Ver symbol_table.
    """

    for id, value in tokenize_python(program):

        token_list.append((id,value)) # test

        if id == "Const":
            Clase_token = symbol_table[id]
            atom = Clase_token()
            atom.value = value
        else:
            Clase_token = symbol_table.get(value)
            if Clase_token: # operator
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
    token = current token
    left = expression's left side
    """

    global token
    t = token
    peek()
    left = t.nud()

    while rbp < token.lbp:
        t = token
        peek()
        left = t.led(left)
    return left


def test(program):

    global token, next

    next = tokenize(program).__next__ 
    token = next()
    tree = parse()
    print (program, "-> ",tree,"\n")
    #print (token_list) for debugging



# Samples


test("1+3*4+2**5")
test("(a+b*4+5)**2")
test("x=1")
test("x= a+b")
test("if a then b else c")
test("if a>3 then b=3")

test("not 1")
test("not 3+4")
test("not a+3*b")

test("1");test("-1");test("+1")
test("pi"); 
test("False"); test("not True")

test("lista=[1,2,3,'hola',56]")
test("suma(4,5)")

test("a and b")
test("1 or 2")
test("not a and b or c**4 ")
test("a << b")
test("1 >> 6")
test("x != y")

"""

# Check:
# test("1+2*3+4/2-1")
# (Sub (Add (Add (Const 1) (Mul (Const 2) (Const 3))) (Div (Const 4) (Const 2))) (Const 1))

# Python 2.x
#>>> import compiler 
#>>> compiler.parse("1+2*3+4/2-1", "eval")
# Expression(Sub((Add((Add((Const(1), Mul((Const(2), Const(3))))), Div((Const(4), Const(2))))), Const(1))))

"""
