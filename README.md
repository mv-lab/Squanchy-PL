[![contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/Jesucrist0/Squanchy-PL/issues)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)
![version](https://img.shields.io/badge/version-1.0.0-blue.svg?maxAge=2592000)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-no-red.svg)](https://github.com/Jesucrist0/Squanchy-PL)
[![code](https://img.shields.io/badge/codestyle-clean-blueviolet.svg)](https://www.amazon.es/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882/ref=pd_lpo_sbs_14_t_0?_encoding=UTF8&psc=1&refRID=HYBK4ZCEKQREQCC461CC)


# Squanchy Programming Language
**_Bastard son of Python and Haskell, and failed Scratch_**

<img src="https://user-images.githubusercontent.com/37480508/49680121-89914100-fa91-11e8-9aa7-3956d855173f.png" width="16%"></img>

## Important

- [code.sqy](code.sqy) Example of code written in Squancy. Ejemplo de código escrito en Squanchy.
- [example.md](example.md) Parser test example, see the AST. Ejemplo para comprobar el parser y ver el AST generado.
- [ir_code.md](ir_code.md) Comprobar la generacin de código intermedio LLVM y compilación.


## About
Squanchy is a brand new, easy to learn, general purpose, multi-paradigm, compiled programming language created by:

* **Marcos V**  [mv-lab](https://github.com/mv-lab)                     

Student at University of Valladolid.
Alumno de la Universidad de Valladolid.

Work on the language began on September, 2018.

Related to the courses: Algorithms and computing, Formal Grammars and Languages.
Asignaturas relacionadas: Algoritmos y Computación, Gramáticas y Lenguajes formales.

The language is written from scratch (it includes an integrated lexer, parser, code generator etc).

  **Why?** 

- Python is lit, that's all, arguably one of the best programming languages ever.
- I wrote the same code in Haskell and Java. Now you see how concise, clean, and perfect is  Haskell code:

<!-- <img src="https://images.huffingtonpost.com/2013-11-08-arronctonrcode118.jpg" width="72%"></img> -->
    
```java
final int LIMIT = 50;
int[] a = new int[LIMIT];
int[] b = new int [LIMIT-5];
for (int i=0; i< LIMIT; i++){
 a[i] = (i+1)*2;
 if (i >= 5) b(i-5)= [i];
}
```
```haskell
let a = [2,4...100]
let b = drop 5 a

```

So I tried to put together Python and Haskell (or at least the main features from both) in Squanchy. 


#### Contact      [![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](mailto:marcosventura.conde@alumnos.uva.es)

#### This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details

#### Built With

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/download/releases/3.0/) 

<a href="https://llvm.org/"><img src="https://llvm.org/img/LLVM-Logo-Derivative-5.png" width="10%"></img>
</a>

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

```haskell
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
* array (like numpy)
* more default functions
* fixed visualisation module
* ...


## Contributing

```prolog
This is an open source project.
```
![contributors](https://img.shields.io/badge/contributors-1-green.svg)

* Gabriel Rodríguez Canal [@gabrielrodcanal](https://github.com/gabrielrodcanal)

You want to contribute?
Please do! The source code is hosted at GitHub. If you want something, open an issue or a pull request.
If you need want to contribute but don't know where to start, take a look at:

- [Step by step guide to make your first contribution](https://codeburst.io/a-step-by-step-guide-to-making-your-first-github-contribution-5302260a2940)
- [Github guideline for repository contributors](https://help.github.com/articles/setting-guidelines-for-repository-contributors/)

This is the main [documentation](documentation.pdf) of the project, only Spanish version (for the moment). Also
you can checkout down below all my sources in Bibliography

Before doing anything, see [Code of Conduct](CODE_OF_CONDUCT.md)

**Contributing Code**

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request 

Check this out if you don't know how to start:


## Aims and objectives

- [x] Make it work
- [x] Basic code generation
- [ ] Beautiful and Clean Code + documentation !! 
- [ ] Add data structures and arrays 
- [ ] IDLE for Squanchy: something easy and minimalist, just write & run like Jupyter.
- [ ] Work on the code optimization
- [ ] Update tutorials, documentation ...
- [ ] a ton of things more


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
- [68 Resources To Help You To Create Programming Languages](https://tomassetti.me/resources-create-programming-languages/)
