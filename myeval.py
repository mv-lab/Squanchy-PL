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
from ctypes import CFUNCTYPE
import os
import json


i32_ty = ir.IntType(32)

def Eval(node, scope,builder = None,module= None,printf= None):

    """
    Main Evaluation function. If builder recieved (builder != None)
    then generates code on that IRBuilder.
    If builder == None, return the "simple" value of the expression .
    For example:
        - 4+5 -> Eval(Add (Cont 4, Cont 5))
                    -> return 9 
                    -> return builder.add(4,5), wich generates
    """

    codegen = {
    
    "+": lambda first,second: builder.add(first, second),
    "-": lambda first,second: builder.sub(first, second),
    "not": lambda first,second: builder.not_(first),
    "*": lambda first,second: builder.mul(first, second),
    "/": lambda first,second: builder.sdiv(first, second),
    "and": lambda first,second: builder.and_(first, second),
    "or": lambda first,second: builder.or_(first, second),
    "!=": lambda first,second: builder.icmp_signed("!=",first,second),
    "=": lambda first,second: builder.icmp_signed("==",first,second),
    "<": lambda first,second: builder.icmp_signed("<",first,second),
    ">": lambda first,second: builder.icmp_signed(">",first,second),
    "<=": lambda first,second: builder.icmp_signed("<=",first,second),
    ">=": lambda first,second: builder.icmp_signed(">=",first,second)

    }

    operations = {

    "+": lambda first,second: first+second,
    "-": lambda first,second: first-second,
    "not": lambda first,second: not first,
    "*": lambda first,second: first*second,
    "/": lambda first,second: int(first/second),
    "%": lambda first,second: first%second,
    "**": lambda first,second: first**second,
    "and": lambda first,second: first and second,
    "or": lambda first,second: first or second,
    "!=": lambda first,second: first != second,
    "=": lambda first,second: first == second,
    "<": lambda first,second: first<second,
    ">": lambda first,second: first>second,
    "<=": lambda first,second: first<=second,
    ">=": lambda first,second: first >= second,
    }
    

    #print (scope)
    #print ("node = ",node,node.first,node.second)

    if node.id == "Name":
        try:
            if type (scope.names[node.value]) == list:
                return scope.names[node.value]
            else:
                if builder == None:
                    try:
                        return int(scope.names[node.value])
                    except:
                        return scope.names[node.value]
                else:
                    try:
                        return i32_ty(int(scope.names[node.value]))
                    except:
                        return scope.names[node.value]
        except:
            raise NotDefined('Name "%s" is not defined' % node.value)


    if node.id == "Const":
        if builder == None:
            try: 
                return int(node.value)
            except:
                return node.value
        else:
            try:
                return i32_ty(int(node.value))
            except:
                return node.value.strip('"')

    if node.name == "Assign":

        if builder == None:
            return Eval(node.second,scope)
        else:
            val = Eval(node.second,scope,builder,module)
            ptr = builder.alloca(val.type)
            builder.store(val, ptr)
            return val

    if node.name == "List":
        return str([x.value for x in node.first])

    if node.name == "Tuple":
        return str([x.value for x in node.first])

    # OPERATOR
    if node.arity == 2:

        first= Eval(node.first,scope,builder,module)
        second= Eval(node.second,scope,builder,module)
        op = node.id

        if builder == None:
            return operations[op](first,second)
        else:
            return codegen[op](first,second) 

    elif node.arity == 1:

        second= Eval(node.first,scope,builder,module)
        first = i32_ty(int(0))
        op = node.id

        if builder == None:
            return operations[op](first,second)
        else:
            return codegen[op](first,second) 
    
    else:
        # is a statement
        # only print call considered.

        if builder !=None:

            func_name = node.first.value
            args = [x.value for x in node.second[0]]


            if func_name == "print":
                eval_print(node,scope,builder,module,printf)

            # basic functions
            elif node.id== "Function":
                #print (node)
                #print (func_name)
                #print (args)

                # de momento solo tipo int
                type_arg = [i32_ty for i in args]

                func_ty = ir.FunctionType(ir.IntType(32), type_arg)
                func = ir.Function(module, func_ty, name=func_name)

                for i in range(len(args)):
                    func.args[i].name = args[i]

                name_block = func_name+"_entry"
                fn_block = func.append_basic_block(name_block)
                func_builder = ir.IRBuilder(fn_block)

                tmp = Eval(node.second[1][0],scope,func_builder,module)
                ret = func_builder.ret(tmp)

                #print(module)
            elif node.id == "CallFunc":
                return "CALL"
            else:
                pass
        else:
            return "PROC"


class NotDefined(Exception):
    pass



def eval_print(node,scope,builder,module,printf):

    # print ("hola mundo",5) -> CallFunc(Name (print),[[Const ("hola mundo"), Const (5)]])

    end = "\n\0"
    arg = ""
    values = []

    args = node.second[0] # list of arguments to print
    for a in args:

        arg_value = Eval(a,scope,builder,module)
        if type(arg_value) == str:
            arg += arg_value
        else:
            arg += "%i"
            values.append (arg_value)
            
    arg+=end

    voidptr_ty = ir.IntType(8).as_pointer()    
    c_str_val = ir.Constant(ir.ArrayType(ir.IntType(8), len(arg)),
                            bytearray(arg.encode("utf8")))

    c_str = builder.alloca(c_str_val.type)
    builder.store(c_str_val, c_str)
    fmt_arg = builder.bitcast(c_str, voidptr_ty)

    # Call Print Function
    in_ = [fmt_arg]
    in_ += values
    builder.call(printf, in_)
