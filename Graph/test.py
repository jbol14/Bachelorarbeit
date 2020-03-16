from node import Node
from edge import Edge
from graph import Graph

a = Node("A")
b = Node("B")

print(a,b)

c = Node("C")
d = Node("D")
e = Node("E")
f = Node("F")
s = Node("S")
t = Node("T")
nodes = [a,b,c,d,e,f,s,t]

e1 = Edge(a,d)
e2 = Edge(a,f)
e3 = Edge(b,c)
e4 = Edge(b,e)
e5 = Edge(c,f)
e6 = Edge(e,d)
e7 = Edge(e,t)
e8 = Edge(f,e)
e9 = Edge(f,t)
e10 = Edge(s,a)
e11 = Edge(s,b)

edges = [e1,e2,e3,e4,e5,e6,e7,e8,e9,e10,e11]

graph = Graph(nodes,edges)

print(graph.buildAdjacencyList())

#print(graph.bfs(c,e))
print(graph.dfs(a,b))