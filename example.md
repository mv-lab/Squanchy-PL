
## Code

```
global u
global v


suma (a,b) -> (c,d) ::
	c:a+b
	a:a+15
	b:5

suma (a,b) -> a+b
suma (a,b) -> c
suma (4,5) -> 9


if a<=50 then 
	d : "hola"
	else d: "adios"

if a<=50 then d : "hola" else d: "adios"

if a<=50 then d : "hola"
	else d: "adios"

while a<56 ::
	a:a+1
	b:True

numbers : [1,2,3,4]
truths  : [True,False,False]
strings : ["here","are","some","strings"]

list : [1,2,3,4,5,"hello"]
mylist : [12,45463,1.56,"hello",
		45,35,57]

list_of_list : [1,2,3,[1,2,3]]


my_Tuple: ("Hello world", False)
my_tuple : (1,"hello",5.6)
((2,3), True)
((2,3), [2,3])
[(1,2), (3,4), (5,6)]

mylist.1
my_tuple.3


add : lambda a b :: a+b
lambda r :: r**2*pi


a+b*c**2-(-1/2)

x:y:z:8

not a or b and c

pi

tuple : (a,b,c)

True and False

(a<<2)+1

```


### Output

```
Module [ 
	global(Name (u))
	global(Name (v))
	Function(Name (suma),[[Name (a), Name (b)], [Tuple([Name (c), Name (d)])]],[Assign(Name (c),Add(Name (a),Name (b))), Assign(Name (a),Add(Name (a),Const (15))), Assign(Name (b),Const (5))])
	Function(Name (suma),[[Name (a), Name (b)], [Add(Name (a),Name (b))]])
	Function(Name (suma),[[Name (a), Name (b)], [Name (c)]])
	Function(Name (suma),[[Const (4), Const (5)], [Const (9)]])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (d),Const ("hola"))],[Assign(Name (d),Const ("adios"))])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (d),Const ("hola"))],[Assign(Name (d),Const ("adios"))])
	IfExp(<=(Name (a),Const (50)),[Assign(Name (d),Const ("hola"))],[Assign(Name (d),Const ("adios"))])
	While_stmt(<(Name (a),Const (56)),[Assign(Name (a),Add(Name (a),Const (1))), Assign(Name (b),Const (1))])
	Assign(Name (numbers),List([Const (1), Const (2), Const (3), Const (4)]))
	Assign(Name (truths),List([Const (1), Const (0), Const (0)]))
	Assign(Name (strings),List([Const ("here"), Const ("are"), Const ("some"), Const ("strings")]))
	Assign(Name (list),List([Const (1), Const (2), Const (3), Const (4), Const (5), Const ("hello")]))
	Assign(Name (mylist),List([Const (12), Const (45463), Const (1.56), Const ("hello"), Const (45), Const (35), Const (57)]))
	Assign(Name (list_of_list),List([Const (1), Const (2), Const (3), List([Const (1), Const (2), Const (3)])]))
	Assign(Name (my_Tuple),Tuple([Const ("Hello world"), Const (0)]))
	Assign(Name (my_tuple),Tuple([Const (1), Const ("hello"), Const (5.6)]))
	Tuple([Tuple([Const (2), Const (3)]), Const (1)])
	Tuple([Tuple([Const (2), Const (3)]), List([Const (2), Const (3)])])
	List([Tuple([Const (1), Const (2)]), Tuple([Const (3), Const (4)]), Tuple([Const (5), Const (6)])])
	Access(Name (mylist),Const (1))
	Access(Name (my_tuple),Const (3))
	Assign(Name (add),Lambda([Name (a), Name (b)],Add(Name (a),Name (b))))
	Lambda([Name (r)],Mul(Power(Name (r),Const (2)),Const (3.141592653589793)))
	Sub(Add(Name (a),Mul(Name (b),Power(Name (c),Const (2)))),Div(UnarySub(Const (1)),Const (2)))
	Assign(Name (x),Assign(Name (y),Assign(Name (z),Const (8))))
	Or(Not(Name (a)),And(Name (b),Name (c)))
	Const (3.141592653589793)
	Assign(Name (tuple),Tuple([Name (a), Name (b), Name (c)]))
	And(Const (1),Const (0))
	Add(LeftShift(Name (a),Const (2)),Const (1))
]

```

