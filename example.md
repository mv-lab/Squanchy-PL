
## Code


```
# CODE EXAMPLE IN SQUANCHY#
# ------------------------------------------------#


# prueba de comentario
multilnea#


# OPERATORS #

a+b*c**2-(-1/2)

x:y:z:8

not a or b and c

pi

tuple : (a,b,c)

True and False

(a<<2)+1


# LISTS #

numbers : [1,2,3,4]
truths  : [True,False,False]
strings : ["here","are","some","strings"]

list : [1,2,3,4,5,"hello"]
mylist : [12,45463,1.56,"hello",
			45,35,57]

list_of_list : [1,2,3,[1,2,3]]


multiline_list : [
	a,b,c,
	d,e,f,
	1,2,3,
	"hi!",5.76,True
]


# TUPLES #

my_Tuple: ("Hello world", False)
my_tuple : (1,"hello",5.6)
((2,3), True)
((2,3), [2,3])
[(1,2), (3,4), (5,6)]


mylist.1
my_tuple.3


# GLOBAL #

global u
global v


# CONSTANTS #

a := 5
b := True
c := "constant"


# LAMBDA #

add : lambda a b :: a+b
lambda r :: r**2*pi


# FUNCTIONS #

foo () -> True
suma (a,b) -> a+b
foo (a,b) -> "function"
suma (4,5) -> 9

resta (a,b) -> (c,d) :: c:a-b
	d:(a-b)**2

suma (a,b) -> (c,d) ::
	c:a+b
	a:a+15
	b:5


# IF-THE-ELSE #

if b<5 and c>10 then d:45

if a<=50 then d : "hi!" else d: "bye"

if a<=50
	then d : "hi!"
	else d: "bye"

if a<=50
then d : "hi!" 
else d: "bye"


if a<=50
	then
		a:a+1
		b:b+1
		print(a+b)
	else
		print ("hi!")


# WHILE #

@ a<56 ::
	a:a+1
	b:True

@ a<100 ::
	if a > 50 then print ("hola") else suma(a,1)
	lambda a :: a+1
	function (a,b)-> (c,d) :: 
		c:a+b
		d:a-b
```


### AST

```

 Module [ 
	Sub(Add(Name (a),Mul(Name (b),Power(Name (c),Const (2)))),Div(UnarySub(Const (1)),Const (2)))
	Assign(Name (x),Assign(Name (y),Assign(Name (z),Const (8))))
	Or(Not(Name (a)),And(Name (b),Name (c)))
	Const (3.141592653589793)
	Assign(Name (tuple),Tuple([Name (a), Name (b), Name (c)]))
	And(Const (1),Const (0))
	Add(LeftShift(Name (a),Const (2)),Const (1))
	Assign(Name (numbers),List([Const (1), Const (2), Const (3), Const (4)]))
	Assign(Name (truths),List([Const (1), Const (0), Const (0)]))
	Assign(Name (strings),List([Const ("here"), Const ("are"), Const ("some"), Const ("strings")]))
	Assign(Name (list),List([Const (1), Const (2), Const (3), Const (4), Const (5), Const ("hello")]))
	Assign(Name (mylist),List([Const (12), Const (45463), Const (1.56), Const ("hello"), Const (45), Const (35), Const (57)]))
	Assign(Name (list_of_list),List([Const (1), Const (2), Const (3), List([Const (1), Const (2), Const (3)])]))
	Assign(Name (multiline_list),List([Name (a), Name (b), Name (c), Name (d), Name (e), Name (f), Const (1), Const (2), Const (3), Const ("hi!"), Const (5.76), Const (1)]))
	Assign(Name (my_Tuple),Tuple([Const ("Hello world"), Const (0)]))
	Assign(Name (my_tuple),Tuple([Const (1), Const ("hello"), Const (5.6)]))
	Tuple([Tuple([Const (2), Const (3)]), Const (1)])
	Tuple([Tuple([Const (2), Const (3)]), List([Const (2), Const (3)])])
	List([Tuple([Const (1), Const (2)]), Tuple([Const (3), Const (4)]), Tuple([Const (5), Const (6)])])
	Access(Name (mylist),Const (1))
	Access(Name (my_tuple),Const (3))
	global(Name (u))
	global(Name (v))
	Let(Name (a),Const (5))
	Let(Name (b),Const (1))
	Let(Name (c),Const ("constant"))
	Assign(Name (add),Lambda([Name (a), Name (b)],Add(Name (a),Name (b))))
	Lambda([Name (r)],Mul(Power(Name (r),Const (2)),Const (3.141592653589793)))
	Function(Name (foo),[[], [Const (1)]])
	Function(Name (suma),[[Name (a), Name (b)], [Add(Name (a),Name (b))]])
	Function(Name (foo),[[Name (a), Name (b)], [Const ("function")]])
	Function(Name (suma),[[Const (4), Const (5)], [Const (9)]])
	Function(Name (resta),[[Name (a), Name (b)], [Tuple([Name (c), Name (d)])]],[Assign(Name (c),Sub(Name (a),Name (b))), Assign(Name (d),Power(Sub(Name (a),Name (b)),Const (2)))])
	Function(Name (suma),[[Name (a), Name (b)], [Tuple([Name (c), Name (d)])]],[Assign(Name (c),Add(Name (a),Name (b))), Assign(Name (a),Add(Name (a),Const (15))), Assign(Name (b),Const (5))])
	IfExp(And(<(Name (b),Const (5)),>(Name (c),Const (10))),[Assign(Name (d),Const (45))])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (d),Const ("hi!"))],[Assign(Name (d),Const ("bye"))])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (d),Const ("hi!"))],[Assign(Name (d),Const ("bye"))])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (d),Const ("hi!"))],[Assign(Name (d),Const ("bye"))])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (a),Add(Name (a),Const (1))), Assign(Name (b),Add(Name (b),Const (1))), CallFunc(Name (print),[[Add(Name (a),Name (b))]])],[CallFunc(Name (print),[[Const ("hi!")]])])
	While_stmt(<(Name (a),Const (56)),[Assign(Name (a),Add(Name (a),Const (1))), Assign(Name (b),Const (1))])
	While_stmt(<(Name (a),Const (100)),[IfExp(>(Name (a),Const (50)),[CallFunc(Name (print),[[Const ("hola")]])],[CallFunc(Name (suma),[[Name (a), Const (1)]]), Lambda([Name (a)],Add(Name (a),Const (1))), Function(Name (function),[[Name (a), Name (b)], [Tuple([Name (c), Name (d)])]],[Assign(Name (c),Add(Name (a),Name (b))), Assign(Name (d),Sub(Name (a),Name (b)))])])])
]


```

