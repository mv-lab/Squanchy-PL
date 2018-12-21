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

import pydot
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


def visualise(tree):

    graph = pydot.Dot(graph_type = 'graph')

    open = [(tree, 0)]
    closed = []
    nodeCounter = 0
    filterLabel = lambda x: x.value if x.id == 'Const' or x.id == 'Name' else x.id

    def nodeColour(id):
        if id is 'Const':
            return 'green'
        elif id is 'Name':
            return 'yellow'
        elif id is "Module":
        	return "grey"
        else:
            return 'cyan'

    while len(open) is not 0:
        parent = open[0]
        children_ = list(filter(lambda x: x is not None, [parent[0].first, parent[0].second, parent[0].third]))

        children = []
        for i in range(len(children_)):
            if isinstance(children_[i], (list,)):
                children = children_[:i] + children_[i]
            else:
                children.append(children_[i])
        
        parentNode = pydot.Node(parent[1], label = filterLabel(parent[0]), style = "filled", fillcolor = nodeColour(parent[0].id))
        nodeCounter += 1

        children = list(zip(children, range(nodeCounter, nodeCounter + len(children))))
        nodeCounter += len(children)


        childrenNodes = [pydot.Node(c[1], label = filterLabel(c[0]), style = "filled", fillcolor = nodeColour(c[0].id)) for c in children]

        graph.add_node(parentNode)
        [graph.add_node(c) for c in childrenNodes]
        [graph.add_edge(pydot.Edge(parentNode, c)) for c in map(lambda x: x[1], children)]

        closed.append(open[0])
        open = children + open[1:]

    formato = "svg"
    filename = 'draft_tree.%s' % formato
    graph.write(filename,format=formato)

    formato = "png"
    filename = 'draft_tree.%s' % formato

    graph.write(filename,format=formato)
    img = mpimg.imread(filename)
    imgplot = plt.imshow(img)
    plt.axis("off")
    plt.show()



