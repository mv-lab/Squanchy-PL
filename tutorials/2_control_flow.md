# Control Flow

> In computer science, control flow (or flow of control) is the order in which individual statements, instructions or function calls of an imperative program are executed or evaluated. The emphasis on explicit control flow distinguishes an imperative programming language from a declarative programming language. 

In Squanchy, there are **If-then-(else)** statements and **while** statements, based on Pacal, Haskell and Python. Soon we will have **for** and **Case** and switch statements.


## If/Then/Else

Based on Pascal and Haskell, the syntax for `if` statement is: 

```haskell
if <condition> then <true-value> else <false-value>
```
The condition or expression doesn't have to be enclosed in parentheses, and `else` is optional.

Haskell:

```haskell
describeLetter :: Char -> String
describeLetter c =
    if c >= 'a' && c <= 'z'
        then "Lower case"
        else if c >= 'A' && c <= 'Z'
            then "Upper case"
            else "Not an ASCII letter"
```

Pascal:

```pascal
if a > 0 then
  writeln("yes")
else
  writeln("no");
  
```

In Squanchy there are many ways ...

* Simple **if-then** statement:

```pascal
if b<5 and c>10 then d:45
```

* Simple **if-then-else** statement:

```pascal
if a<=50 then d : "hi!" else d: "bye"
```

* **Multi-line** if-then-else statement. In this case you have to take care of `INDENTATION`, but we are very permissive:

```haskell
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
```

* For **else if**, follow an else with another if statement. Here is an example:

```haskell
if a<=50
	then
		a:a+1
		b:b+1
		print(a+b)
	else if a>10 then print ("hi!")
	else print ("bye")
```

## While

`while` is the basic loop operator. The syntax is:

```python
while <expression> :: <body>
```

As in if statement, the condition or expression doesn't have to be enclosed in parentheses. Simple while loop examples are below:

```haskell
while a<56 ::
	a:a+1
	b:True

while a<100 ::
	if a > 50 then print ("hola") else suma(a,1)
	lambda a :: a+1
	function (a,b)-> (c,d) :: 
		c:a+b
		d:a-b

a:0
while a<len(lista)::
	lista.a : a
	a:a+1

```


[index](index.md) | [next: Functions ->](3_functions.md)


