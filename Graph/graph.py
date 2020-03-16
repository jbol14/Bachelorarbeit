class Graph():
    def __init__(self, listOfNodes=[], listOfEdges=[]):
        self.nodes = listOfNodes
        self.edges = listOfEdges
    
    '''Knoten und Kanten hinzufügen'''
    def addNode(self,node):
        self.nodes.append(node)
    def addEdge(self, edge):
        self.edges.append(edge)

    def buildAdjacencyList(self):
        adjacencyList = {}
        for node in self.nodes:
            adjacencyList[node.name]=[]
        for edge in self.edges:
            adjacencyList[edge.node1.name].append(edge.node2.name)
        
        return adjacencyList

    ''' Einfache Suchalgorithmen'''
    ## Breitensuche
    ## TODO Pfad zum Ziel zurückgeben
    def bfs(self,start,target):
        g = self.buildAdjacencyList()
        s_name = start.name
        t_name = target.name
        stack = g[s_name]
        visited = []
        found = False
        while not found:
            current = stack.pop(0)
            visited.append(current)
            if current == t_name:
                found = True
            for node in g[current]:
                if node not in visited and node not in stack:
                    stack.append(node)
        
        return visited
    
    ## TODO Tiefensuche
    def dfs(self, start, target):
        g = self.buildAdjacencyList()
        s_name = start.name
        t_name = target.name

        visited = []

        stack = g[s_name]
        found = False
        while not found:
            # Wenn der Stacl leer ist sind alle erreichbaren Knoten besucht und das Ziel nicht gefunden
            if len(stack) == 0:
                return False
            
            current = stack.pop(0)
            print(current,g[current],stack)
            
            visited.append(current)
            if current == t_name:
                return True

            # Das muss doch besser gehen
            # Elemente der Adjazenzliste des aktuell besuchten Knotens auf den Stack pushen
            for i in range(len(g[current])-1,-1,-1):
                if g[current][i] not in visited and g[current][i] not in stack:
                    stack.insert(0,g[current][i])
            print(stack)