# Basic Concepts

The tutorials for most programming languages start with a hello world program,so

```
print ("hello world")
```

Coming soon:

```
print "hello world"
```

That's it. Just save that as a normal text file with the extension `.sqy` and run it.


## Primitive Types

496 is an example of an __Int__, which is the same as an int in C. It can hold positive and negative whole numbers. The other two primitive data types are Double and List.

__Double__ is the same as a C double.

__List__ is the same as a Python or Haskell list.

A __Bool__ can only be `1` or `0` like C, so in fact is __Int__

A __String__ isn't really a primitive data type, it is a __List__ of letters, numbers or other characters of any length, as in Haskell.


## Operators

In general, operators in Squanchy work the same as in any other language. It has all the ones you would expect with sensible order of operations. The following are the only major differences between operators in Pinecone and C-style languages:
* The assignment operator is `:` instead of `=`.
* The equality operator is `=` instead of `==`.
* There are no bitwise operators, they may be implemented at some point.
* The short no semicolons.


## Variables

A __variable__ is a place you can store a value. Every variable has a type, but types are deduced implicitly. To create, change and use a variable, simply do the following:

```
myVarName: 88
myVarName: "hello"
print (myVarName)
```

`myVarName` can be any series of letters, digits and underscores, as long as it doesn't start with a number.

We have on the backend `Names`that includes __variables__ and __function names__


## Tuples

As in haskell. To construct one you simple combine several expressions with commas. The names of the elements of a tuple are `1`, `2`, etc. Elements can be accesed with the `.` operator. Here is an example:

```
my_tuple : (1,"hello",5.6)
print: myTuple.c
print: myTuple.a
```

The output of this will be

```
> 5.6
> 1
```


## Lists

As Haskell and Python. To construct one you don't need commas !. Elements can be accesed with the `.` operator as __Tuples__. Here is an example:

```
list : [1 2 3 4 5 "hello"]

list2 : [12 45463 1.56 "hello"
		45 35 57]

```

## Constants

A __constant__ is a value that is determined at compile time. Constants are created with the constants assignment operator `global`. You can declare constants as follows: `global var_name value ` . Here is an example of a simple use of constants:

```
global a 5
global b 10
global pi 3.141592653589793
global c "string"
print (a+b)
print (c)
```

This will print 15 and "string" a,b,c are no longer `Names`, now are `Constants`.
Variable pi is now constant 3.141592653589793

## Comments

__coming soon__
Comments are parts of your program that the compiler doesn't look at, so you can write notes and whatnot. In Squanchy, single-line comments start with a `--`. Multi-line comments start with `//` and end with `\\`.


[index](index.md) | [next: Control Flow ->](2_control_flow.md)
