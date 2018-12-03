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
        else:
            return 'blue'

    while len(open) is not 0:
        parent = open[0]
        children = list(filter(lambda x: x is not None, [parent[0].first, parent[0].second, parent[0].third]))
        
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

    graph.write_png('draft_tree.png')
    img = mpimg.imread('draft_tree.png')
    imgplot = plt.imshow(img)

    plt.show()