# Squanchy Programming Language
**_Bastard son of Python and Haskell, and failed Scratch_**

<img src="https://user-images.githubusercontent.com/37480508/49680121-89914100-fa91-11e8-9aa7-3956d855173f.png" width="15%"></img>


## About
Squanchy is a brand new, easy to learn, general purpose, multi-paradigm, high performance programming language created by:

* **Marcos V. Conde**  [Jesucrist0](https://github.com/Jesucrist0)
* **Gabriel Rodríguez Canal**  [gabrielrodcanal](https://github.com/gabrielrodcanal)

Work on the language began on September, 2018.
The language is written from scratch (it includes an integrated lexer, parser and interpreter, etc.).

#### This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details


## Example
Here is Fibonacci demo program written in Haskell and Squanchy. You can see code example in the [example](example.md) or the [tutorials](tutorials/index.md).

```haskell

fib x
  | x < 2 = 1
  | otherwise = fib (x - 1) + fib (x - 2)


fib 1 = 1
fib 2 = 2
fib x = fib (x - 1) + fib (x - 2)

```
Squanchy:

```
fib (1) -> 1
fib (2) -> 2
fib(x) -> fib(x-1) + fib(x-2)
```


## Guide
__If you want to program in Squanchy now, see the [tutorials](tutorials/index.md) for how to get started.__
Yes, there are no tutorials by the way

### Getting Started

Force us to let you download it. Then ...

```
python3 parser.py --in
```

This is only an example


## Current State
The features that are currently implemented are as follows:

* Primitive data types `List`,`String`, `Int` and `Double`
* Operators (`+`,`-`, `*`,`/`,`**`, `%`, `:`, `=`, `>`, `<=`, `and`,`or`, etc.)
* Flow control (if/the/else, while loop)
* Constants
* Tuples
* Functions
* Lambda

The following features are coming soon:

* Single and multi line comments
* Flow control (if, for)
* Data structs
* String operations
* Dictionaries
* ...


## Contributing
You can email your suggestions to squanchy@wedontgiveafuck.com.

## Built With

* [Python3.0](https://www.python.org/download/releases/3.0/) 

## References

* https://tdop.github.io/
* http://effbot.org/zone/simple-top-down-parsing.htm
* http://crockford.com/javascript/tdop/tdop.html
* https://ruslanspivak.com/lsbasi-part9/
* more

