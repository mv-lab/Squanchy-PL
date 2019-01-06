
## Code

**test.sqy**

```
# CODE GENERATION EXAMPLE IN SQUANCHY#
# ------------------------------------------------#

print (1, " hola mundo en Squanchy")

425+5266

2636-5263+5

+1*53-4262

a:5
b:c:d:10

print ("a = ",a," b = ",b," c= ",c," d= ",d)

print(a+b-c*d)
print ("b+c = c+d ",b+c = c+d)
print ("a+b < c+d ",a+b < c+d)
print ("a+b > c+d ",a+b > c+d)

print (400/5+20-15/3)
print (253 and 253)
print (10 or 16)

# some functions #

suma (a,b) -> a+b

resta (a,b) -> a-b

operation (a,b,c) -> a-b*c

```


### AST

```

Module [ 

	CallFunc(Name (print),[[Const (1), Const (" hola mundo en Squanchy")]])

	Add(Const (425),Const (5266))

	Add(Sub(Const (2636),Const (5263)),Const (5))

	Sub(Mul(UnaryAdd(Const (1)),Const (53)),Const (4262))

	Assign(Name (a),Const (5))

	Assign(Name (b),Assign(Name (c),Assign(Name (d),Const (10))))

	CallFunc(Name (print),[[Const ("a = "), Name (a), Const (" b = "), Name (b), Const (" c= "), Name (c), Const (" d= "), Name (d)]])

	CallFunc(Name (print),[[Sub(Add(Name (a),Name (b)),Mul(Name (c),Name (d)))]])

	CallFunc(Name (print),[[Const ("b+c = c+d "), =(Add(Name (b),Name (c)),Add(Name (c),Name (d)))]])

	CallFunc(Name (print),[[Const ("a+b < c+d "), <(Add(Name (a),Name (b)),Add(Name (c),Name (d)))]])

	CallFunc(Name (print),[[Const ("a+b > c+d "), >(Add(Name (a),Name (b)),Add(Name (c),Name (d)))]])

	CallFunc(Name (print),[[Sub(Add(Div(Const (400),Const (5)),Const (20)),Div(Const (15),Const (3)))]])

	CallFunc(Name (print),[[And(Const (253),Const (253))]])

	CallFunc(Name (print),[[Or(Const (10),Const (16))]])

	Function(Name (suma),[[Name (a), Name (b)], [Add(Name (a),Name (b))]])

	Function(Name (resta),[[Name (a), Name (b)], [Sub(Name (a),Name (b))]])

	Function(Name (operation),[[Name (a), Name (b), Name (c)], [Sub(Name (a),Mul(Name (b),Name (c)))]])
]

```
### Scope

```
 {"a": 5, "d": 10, "c": 10, "b": 10}
```



### LLVM-IR

**output.ll**

```
; ModuleID = "..."
target triple = "x86_64-unknown-linux-gnu"
target datalayout = ""

define void @"main"() 
{
entry:
  %".2" = alloca [27 x i8]
  store [27 x i8] c"%i hola mundo en Squanchy\0a\00", [27 x i8]* %".2"
  %".4" = bitcast [27 x i8]* %".2" to i8*
  %".5" = call i32 (i8*, ...) @"printf"(i8* %".4", i32 1)
  %".6" = add i32 425, 5266
  %".7" = sub i32 2636, 5263
  %".8" = add i32 %".7", 5
  %".9" = add i32 0, 1
  %".10" = mul i32 %".9", 53
  %".11" = sub i32 %".10", 4262
  %".12" = alloca i32
  store i32 5, i32* %".12"
  %".14" = alloca i32
  store i32 10, i32* %".14"
  %".16" = alloca i32
  store i32 10, i32* %".16"
  %".18" = alloca i32
  store i32 10, i32* %".18"
  %".20" = alloca [27 x i8]
  store [27 x i8] c"a = %i b = %i c= %i d= %i\0a\00", [27 x i8]* %".20"
  %".22" = bitcast [27 x i8]* %".20" to i8*
  %".23" = call i32 (i8*, ...) @"printf"(i8* %".22", i32 5, i32 10, i32 10, i32 10)
  %".24" = add i32 5, 10
  %".25" = mul i32 10, 10
  %".26" = sub i32 %".24", %".25"
  %".27" = alloca [4 x i8]
  store [4 x i8] c"%i\0a\00", [4 x i8]* %".27"
  %".29" = bitcast [4 x i8]* %".27" to i8*
  %".30" = call i32 (i8*, ...) @"printf"(i8* %".29", i32 %".26")
  %".31" = add i32 10, 10
  %".32" = add i32 10, 10
  %".33" = icmp eq i32 %".31", %".32"
  %".34" = alloca [14 x i8]
  store [14 x i8] c"b+c = c+d %i\0a\00", [14 x i8]* %".34"
  %".36" = bitcast [14 x i8]* %".34" to i8*
  %".37" = call i32 (i8*, ...) @"printf"(i8* %".36", i1 %".33")
  %".38" = add i32 5, 10
  %".39" = add i32 10, 10
  %".40" = icmp slt i32 %".38", %".39"
  %".41" = alloca [14 x i8]
  store [14 x i8] c"a+b < c+d %i\0a\00", [14 x i8]* %".41"
  %".43" = bitcast [14 x i8]* %".41" to i8*
  %".44" = call i32 (i8*, ...) @"printf"(i8* %".43", i1 %".40")
  %".45" = add i32 5, 10
  %".46" = add i32 10, 10
  %".47" = icmp sgt i32 %".45", %".46"
  %".48" = alloca [14 x i8]
  store [14 x i8] c"a+b > c+d %i\0a\00", [14 x i8]* %".48"
  %".50" = bitcast [14 x i8]* %".48" to i8*
  %".51" = call i32 (i8*, ...) @"printf"(i8* %".50", i1 %".47")
  %".52" = sdiv i32 400, 5
  %".53" = add i32 %".52", 20
  %".54" = sdiv i32 15, 3
  %".55" = sub i32 %".53", %".54"
  %".56" = alloca [4 x i8]
  store [4 x i8] c"%i\0a\00", [4 x i8]* %".56"
  %".58" = bitcast [4 x i8]* %".56" to i8*
  %".59" = call i32 (i8*, ...) @"printf"(i8* %".58", i32 %".55")
  %".60" = and i32 253, 253
  %".61" = alloca [4 x i8]
  store [4 x i8] c"%i\0a\00", [4 x i8]* %".61"
  %".63" = bitcast [4 x i8]* %".61" to i8*
  %".64" = call i32 (i8*, ...) @"printf"(i8* %".63", i32 %".60")
  %".65" = or i32 10, 16
  %".66" = alloca [4 x i8]
  store [4 x i8] c"%i\0a\00", [4 x i8]* %".66"
  %".68" = bitcast [4 x i8]* %".66" to i8*
  %".69" = call i32 (i8*, ...) @"printf"(i8* %".68", i32 %".65")
  ret void
}

declare i32 @"printf"(i8* %".1", ...) 

define i32 @"suma"(i32 %"a", i32 %"b") 
{
suma_entry:
  %".4" = add i32 5, 10
  ret i32 %".4"
}

define i32 @"resta"(i32 %"a", i32 %"b") 
{
resta_entry:
  %".4" = sub i32 5, 10
  ret i32 %".4"
}

define i32 @"operation"(i32 %"a", i32 %"b", i32 %"c") 
{
operation_entry:
  %".5" = mul i32 10, 10
  %".6" = sub i32 5, %".5"
  ret i32 %".6"
}

```


Obtenemos **output.ll** del módulo *main.py*, para ejecutar el código basta con escribir los siguientes comandos:

```
llc -filetype=obj output.ll
clang output.o -o output
./output
```
