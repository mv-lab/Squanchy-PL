# Squanchy Programming Language
**_Bastard son of Python and Haskell, and failed Scratch_**

<img src="https://user-images.githubusercontent.com/37480508/49680121-89914100-fa91-11e8-9aa7-3956d855173f.png" width="15%"></img>


## About
Squanchy is a brand new, easy to learn, general purpose, multi-paradigm, high performance programming language created by:

* **Marcos V. Conde Osorio**  [marcond](marcosventura.conde@alumnos.uva.es)
* **Gabriel Rodríguez Canal**  [gabrielrodcanal](gabriel.rodriguez.canal@alumnos.uva.es)

Work on the language began on September, 2018.
The language is written from scratch (it includes an integrated lexer, parser and interpreter, etc.).

#### This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
#### Built With

* [Python3.0](https://www.python.org/download/releases/3.0/) 

---

## Getting Started

Here is Fibonacci demo program written in Haskell and Squanchy. You can see more code example in [example](example.md).

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
fib (x) -> y ::
  if x<2 then y:1 else y: fib(x-1)+fib(x-2)
  
  
fib (1) -> 1
fib (2) -> 2
fib(x) -> fib(x-1) + fib(x-2)

```

__If you want to program in Squanchy now, see the [tutorials](tutorials/index.md) for how to get started.__



## Current State
The features that are currently implemented are as follows:

* Primitive data types `List`,`String`, `Int` and `Double`
* Operators (`+`,`-`, `*`,`/`,`**`, `%`, `:`, `=`, `>`, `<=`, `and`,`or`, etc.)
* Flow control (if/the/else, while loop)
* Constants and global variables
* Lists, Tuples and access
* Functions
* Lambda

The following features are coming soon:

* Flow control (ternary ?, for)
* Data structs
* Dictionaries
* array
* ...


### Contributing
**Not yet.**


---

## Bibliography

### General

- [The Python Language Reference](https://docs.python.org/3.3/reference/index.html#reference-index)
- [Compilers: Principles, Techniques, and Tools 2ed](https://en.wikipedia.org/wiki/Compilers:_Principles,_Techniques,_and_Tools)
- [Let’s Build A Simple Interpreter](https://ruslanspivak.com/lsbasi-part9/)
- [Parsing Techniques: A Practical Guide](https://www.researchgate.net/publication/233437139_Parsing_Techniques_A_Practical_Guide)

### Lexer

- [Using Regular Expressions for Lexical Analysis](http://effbot.org/zone/xml-scanner.htm)
- [Write your own lexer](http://pygments.org/docs/lexerdevelopment/)
- [Eiben Github ](https://gist.github.com/eliben/5797351)
- [Parsing In Python: Tools And Libraries](https://tomassetti.me/parsing-in-python/)

### Parser

Pratt Parser implementation.

- [Top down operator precedence by Vaughan R. Pratt](https://web.archive.org/web/20151223215421/http://hall.org.ua/halls/wizzard/pdf/Vaughan.Pratt.TDOP.pdf)
- [A New Approach of Complier Design in Context of Lexical
Analyzer and Parser Generation for NextGen Languages](https://pdfs.semanticscholar.org/f449/3fc2ac5491ff626d1aa6e3142aac87d0960f.pdf)
- [Top down operator precedence](https://tdop.github.io/)
- [ Simple Top-Down Parsing in Python](http://effbot.org/zone/simple-top-down-parsing.htm)
- [Top Down Operator Precedence by Douglas Crockford](http://crockford.com/javascript/tdop/tdop.html)
- [Pratt Parsers: Expression Parsing Made Easy](http://journal.stuffwithstuff.com/2011/03/19/pratt-parsers-expression-parsing-made-easy/)
- [Pratt Parsing and Precedence Climbing Are the Same Algorithm](https://www.oilshell.org/blog/2016/11/01.html)
- [Review of Pratt/TDOP Parsing Tutorials](https://www.oilshell.org/blog/2016/11/02.html)
- [A Pratt Parser implementation in Python](https://github.com/percolate/pratt-parser)
- [A Guide to Parsing: Algorithms and Terminology](https://tomassetti.me/guide-parsing-algorithms-terminology/)
- [Parsing text with Python](https://www.vipinajayakumar.com/parsing-text-with-python/)


### Interpreter and Code generation

- [Compiler Design | Intermediate Code Generation](https://www.geeksforgeeks.org/intermediate-code-generation-in-compiler-design/)
- [Compilers Algorithms](http://www.softpanorama.org/Algorithms/compilers.shtml)
- [Compiler Design - Code Optimization](https://www.tutorialspoint.com/compiler_design/compiler_design_code_optimization.htm)
- [Writing your own programming language and compiler with Python](https://blog.usejournal.com/writing-your-own-programming-language-and-compiler-with-python-a468970ae6df)

