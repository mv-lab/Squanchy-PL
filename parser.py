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
import json
import visualiser as visu


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
        "&":"Bitand","^":"Bitxor",
        "<<":"LeftShift",">>":"RightSift","lambda":"Lambda",
        "if":"IfExp","[":"List","=":"Assign"}



#--------------------------------------------------------------------------------------------
# NAME SPACE | SCOPE

class namespace:

    """Clase espacio de nombres. Scope
    See https://pythonspot.com/scope/
    Modeliza un espacio donde las variables son definidas y accesibles,
    pudiendo haber variables locales y globales.
    """

    def __init__ (self):

        self.names = {}

    def define (self,n):

        """ Define nuevas variables en el espacio <self>.
        Transforma el token de un nombre a una variable.
        Error si la variable ya esta en el espacio, o si el nombre dado ya esta reservado.
        """
        t = self.names[n.value]
        if t:
            raise NameError ("Already defined or reserved %r" % n)

        self.names[n.value] = n
        n.reserved = False
        name.nud = lambda self: self
        n.led = None
        n.std = None
        n.lbp = 0
        n.space = space
        return n

    def find (self,name):

        """Encuentra la defincion de <nombre>, el valor.
        Busca en el espacio actual <self> y si no lo encuentra sube niveles,
        en ultima instancia devuelve valor en symbol_table si no lo encuentra.
        Además comprueba si <nombre> no esta undefined o es una funcion.
        """

        e = self
        while 1:
            o = e.names[name]
            if o and o.arity != "function":
                return e.names[name]
            
            e = e.parent
            if not e:
                o = symbol_table[name];
                if o.arity != "function": return o
                else: return symbol_table["Name"] 


    def pop (self):

        """Asciende un nivel en la jerárquia del espacio de nombres.
        """
        scope = self.parent


    def reserve(self,name):

        """Indica que <nombre> se ha usado o es una palabra reservada
        en el espacio actual <self>.
        Por ejemplo "if" será reservada y no podrá usarse como nombre de variable o funcion.
        Los nombres se reservan localmente solo cuando se usen como palabras reservadas.

        """

        if (name.arity != "Name" or name.reserved):
            return

        t = self.names[name.value]
        if t :
            if t.reserved: return
            if t.arity == "Name": raise NameError ("Already defined")

        else:
            self.names[name.value] = name
            name.reserved = True


    def __repr__(self):
        return json.dumps(self.names)


def new_space ():
    s = space
    space = namespace()
    space.parent = s
    return space;


#--------------------------------------------------------------------------------------------

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

            lbp = bp
            value = id
            
            if id == "Name" or id == "Const":
                arity = id
            else:
                arity=2

            def __init__ (self):

                self.first = self.second = self.third = None
                self.id = id
                self.arity = None
                self.reserved = False 
                try : self.name = names_map[self.id]
                except KeyError: self.name= self.id    

            def nud (self):
                pass

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
        symbol_table[id] = Protoclase

    return Protoclase



def advance (id=None):

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

    if token.id == "(end)": pass
    else:
        token = next()



def method(s):

    """Decorador para simplificar el código referido a los métodos nud y led.
        Añade a la clase <tipo> la función referenciada al decorador, como método. 
    """
    assert s in symbol_table.values()
    def new_method(fn):
        setattr(s, fn.__name__, fn) # (clase, nombre funcion, valor = funcion)
    return new_method




# See https://docs.python.org/3/reference/expressions.html | 6.16. Operator precedence

symbol("Const")
symbol("Name")
symbol("(end)")

symbol("+", 110); symbol("-", 110)
symbol("*", 120); symbol("/", 120)
symbol("**", 140); symbol("%",120)
symbol("=",10)

symbol("or",30);symbol("and",40)
symbol("|", 70); symbol("^", 80); symbol("&", 90)
symbol("<<", 100); symbol(">>", 100)
symbol("<", 60); symbol("<=", 60)
symbol(">", 60); symbol(">=", 60)
symbol("<>", 60); symbol("!=", 60); symbol("==", 60)

symbol("}");symbol("{"); symbol(",");symbol(":");symbol(";") #symbol(" ")
symbol("\\n\\t"); symbol("\\n")

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
        return self
    symbol(id).nud = nud

prefix("+", 130); prefix("-", 130); prefix("not", 50)

# Parenthesized Expressions 

symbol("(", 150);symbol(")");

def nud(self):
    expr = parse()
    advance(")")
    return expr
symbol("(").nud = nud


#--------------------------------------------------------------------------------------------
# CONSTANTS

ctes = []


def constant(id,value=None):
    ctes.append(id)
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


def declare (self):
    self.first = parse()
    print (self.first.value)
    constant(self.first.value)
    return self

symbol("global",1000)
symbol("global").nud = declare

#--------------------------------------------------------------------------------------------
# LISTAS

symbol("]"); symbol("[", 150);

# !! añadir multilinea

@method(symbol("["))
def nud(self):
    lista = []
    if token.id != "]":
        while 1:
            lista.append(token)
            advance()
            if token.id == "]":break
    advance("]")
    self.first = lista
    self.arity = 1
    self.name = "List"
    return self


#--------------------------------------------------------------------------------------------
# STATEMENTS



def statement (end_stmt,end_block):

    """Parses one statement. Si el token tiene un método std se llama al método,
    en otro caso se trata de una expresión, una linea que termina en ";".

    -- ?? Error: si el statement no es una asignacion o una funcall.

    """
	
    print (">>",token)

    if (token.arity == "statement"):
        advance()
        # ojo al scope
        return token.nud()

    expr = parse()

    print ("!!!! statement",token)

    if token.id in end_block:
        pass

    elif token.id in end_stmt:
        advance(token.id)
    else:
        raise SyntaxError ("Expected %r" % end_stmt)

    """
    try:
        advance("\\n\\t")

    except SyntaxError:  
        advance("(end)")
    """
    return expr
		

def statements (end_block=["\\n","(end)"], end_line= ["\\n\\t","(end)","\\n"]):
    
    """Parses statements hasta llegar a (end) o }, que indica el fin del bloque.
        Return:
            - statement
            - stmt = array of statements
            - None si no hay statement
    """

    
    stmt = [] # array of statements

    while 1:
        print (">>> estoy en statements",token)

        if token.id in end_block : break
        s = statement(end_line,end_block) # un solo statement
        if s:
            stmt.append(s)

    if len(stmt) == 0: return None
    elif len(stmt) == 1: return [stmt[0]] # s
    else: return stmt



symbol("::")

@method(symbol("::"))
def nud (self):
    a = statements()
    print ("despues de \\n",token)
    return a


def block (key=None):
    t = token
    advance(key) 
    return t.nud()


# while stmt

symbol("while")

@method(symbol("while"))
def nud (self):
    self.first = parse()
    self.second = block("::")
    self.arity = "statement"
    return self


# while a<50 :: c=a+b\n\td=4\n ->  (while (< (Name a),(Const 50)),[(Assign (Name c),(Add (Name a),(Name b))), (Assign (Name d),(Const 4))]) 
# while a<50 ::\nc=a+b\n\td=56**7 ->  (while (< (Name a),(Const 50)),[(Assign (Name c),(Add (Name a),(Name b))), (Assign (Name d),(Power (Const 56),(Const 7)))])



symbol("if", 20); symbol("else"); symbol("then",5)


@method(symbol("then"))
def nud (self):
    a = statements(["(end)","else"])
    return a

@method(symbol("else"))
def nud (self):
    a = statements()
    return a

def nud(self):
    self.first = parse(20)
    self.second = block("then")
    self.third = block() 
    self.arity = "statement"
    return self

symbol("if").nud = nud


symbol(")"); symbol(",")

@method(symbol("("))
def led(self,left):
    self.first = left
    # scope
    self.second = [] # param
    if token.id != ")":
        while 1:
            self.second.append(token)
            advance()
            if token.id == ")":break
            
    advance(")")
    print (">>",token)

    try: 
        self.third = block("::")
        self.arity = "statement"
        self.name = "Function"
        self.id = self.name
    
    except SyntaxError:
        self.third = None   
        self.arity = "2"
        self.name = "FunCall"
        self.id = self.name

    return self


# !!!
def module ():
    program = []

    if token.id != "(end)":
        while 1:
            if token.id == "(end)": break
            program.append(parse())
            #print (">>",program)
            if token.id != "\\n": break
            advance ("\\n")

    advance("(end)")
    return program


symbol("Module")

@method(symbol("Module"))
def nud (self):
    self.first = module()
    return self



#--------------------------------------------------------------------------------------------
# FUNCTION CALLS

"""
symbol(")"); symbol(",")

@method(symbol("("))
def led(self, left):

    self.first = left # function name
    
    # if left in Tabla de nombres
    # else raise FuncionNameError as detail funcion + left + is not defined

    self.second = [] # param
    if token.id != ")":
        while 1:
            self.second.append(token)
            advance()
            if token.id == ")":break
            
    advance(")")
    self.arity = 2
    self.name = "FunCall"
    return self
"""

#--------------------------------------------------------------------------------------------
# LAMBDA FUNCTION

symbol(":"), symbol("lambda",20)

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


#--------------------------------------------------------------------------------------------
# LEXER

def tokenize(program):

    """
    # Genera una instancia 'atom' para la clase asociada al token obtenido mediante tokenize_python
    # (tokenize module). Ver symbol_table.
    """

    import lexer as lex

    for token in lex.lexer(program):

    	if token.id == "number" or token.id == "string":
    		Clase_token = symbol_table["Const"]
    		atom = Clase_token()
    		atom.value = token.value

    	else:

    		Clase_token = symbol_table.get(token.value)

    		if Clase_token:
    			atom = Clase_token()

    		elif token.id == "Name":

    			Clase_token = symbol_table[token.id]
    			atom = Clase_token()
    			atom.value = token.value
    		else:
    			raise SyntaxError("Unknown operator (%r)" % token.value)

    	yield atom


#--------------------------------------------------------------------------------------------
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
    advance()
    left = t.nud()

    while rbp < token.lbp:
        t = token
        advance()
        left = t.led(left)
    return left


# parser tree to ast
def pratt(program): # ast

    global token,space, next 

    next = tokenize(program).__next__ 
    token = next()
    tree = parse()
    return tree
 


def test(program):

    tree = pratt(program)
    print (program, "-> ",tree,"\n")
    #print (format(tree))



if "--console" in sys.argv:
    print ("Squanchy PL console test")
    print ("v1.0","\n")
    while True:
        expr = input (">> ")
        if expr == "exit": exit()
        print (pratt(expr))


if "--sample" in sys.argv:

	print ("\nExamples\n"+(30*"--")+"\n")
    # hacer un fichero txt con todo esto y que lo lea ...

	test('lista=[1,2,3,"hola",56]')

	test ("a+b+c")
	test("x= a+b")

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

	test('lista=[1,2,3,"hola",56]')
	test("suma(4,5)")
	test ("lambda a, b, c: a+b+c")

	test("a and b")
	test("1 or 2")
	test("not a and b or c**4 ")

	test("a << b")
	test("1 >> 6")
	test("x != y")
	test("a+a*(b-c)")

	
if "--benchmark" in sys.argv:

	program = """(lambda Ru,Ro,Iu,Io,IM,Sx,Sy:reduce(lambda x,y:x+y,map(lambda y,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,Sy=Sy,L=lambda yc,Iu=Iu,Io=Io,Ru=Ru,Ro=Ro,i=IM,Sx=Sx,Sy=Sy:reduce(lambda x,y:x+y,map(lambda x,xc=Ru,yc=yc,Ru=Ru,Ro=Ro,i=i,Sx=Sx,F=lambda xc,yc,x,y,k,f=lambda xc,yc,x,y,k,f:(k<=0)or (x*x+y*y>=4.0) or 1+f(xc,yc,x*x-y*y+xc,2.0*x*y+yc,k-1,f):f(xc,yc,x,y,k,f):chr(64+F(Ru+x*(Ro-Ru)/Sx,yc,0,0,i)),range(Sx))):L(Iu+y*(Io-Iu)/Sy),range(Sy))))(-2.1, 0.7, -1.2, 1.2, 30, 80, 24)"""
	test (program)


if "--check" in sys.argv:
	program = input (">> ")
	tree = pratt(program)
	print (program, "-> ",tree,"\n")
	visu.visualise(tree)


if "--stmt" in sys.argv:
    program = input (">> ")
    tree = pratt(program)
    print (program, "-> ",tree,"\n")


if "--try" in sys.argv:

    f = open("code.txt","r")
    program = f.read()
    f.close()

    program = program.strip()
    print (program)

    tree = pratt(program)
    print ("\n\n",program, "->\n ",tree)
    

def main():
	pass


if __name__ == "__main__":
	main()

