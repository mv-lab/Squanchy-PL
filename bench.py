#-------------------------------------------------------------------------------
# Copyright (C) 2018 Gabriel Rodriguez Canal
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


import time
import compiler


def main ():

    measure = []
    program = open("code.txt").read()
    program = program.replace("\n","\\n")
    program = program.replace("\t","\\t")

    for i in range (1000):
        start = time.time()   
        compiler.parseFile("code_py.txt")
        end = time.time()
        measure.append(end-start)

    sqyt = float(sum(measure)/len(measure))
    print "py time >>",sqyt


main()



