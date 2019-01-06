#-------------------------------------------------------------------------------
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


import llvmlite.ir as ir
import llvmlite.binding as llvm
from sqyparser import ast
from codegen import CodeGen
import myeval as e
import os


def console ():

    try:
	    while True:
	        expr = input (">> ")
	        if expr == "exit": exit()
	        if expr == "clear": 
	            os.system('clear')
	            console()
	        
	        program,scope = ast(expr)
	        tree = program.first[0]
	        print (tree)
	        print (scope)
	        print (e.Eval(tree,scope))

    except Exception as e:
        print (e.args[0])
        console()



f = open("test.sqy")
program = f.read()
f.close()
program = program.replace("\n","\\n").replace("\t","\\t")

tree,scope = ast(program)
print ("\n",tree)
print ("\n",scope,"\n")

#console()

codegen = CodeGen()

module = codegen.module
builder = codegen.builder
printf = codegen.printf

for i in tree.first:
	#print (">>", i)
	e.Eval(i,scope,builder,module,printf)


codegen.create_ir()
codegen.save_ir("output.ll")
tm = llvm.Target.from_default_triple().create_target_machine()

os.system('llc -filetype=obj output.ll')
os.system('clang output.o -o output')
os.system('cat output.ll')
#os.system('./output')