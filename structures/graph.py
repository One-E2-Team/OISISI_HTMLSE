class Graph:
    class Edge:
        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            return self._origin, self._destination

        def opposite(self, v):
            if v == self._origin or v == self._destination:
                return self._destination if v == self._origin else self._origin
            else:
                raise ValueError('v not incident to edge')

        def element(self):
            return self._element

        def set_element(self, val):
            self._element = val

        def __hash__(self):
            return hash((self._origin, self._destination))

        def __str__(self):
            return '({0},{1},{2})'.format(self._origin, self._destination, self._element)

        __repr__ = __str__

    def __init__(self, directed=False):
        self._outgoing = {}
        self._incoming = {} if directed else self._outgoing

    def _validate_vertex(self, v):
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, v):
        try:
            self._validate_vertex(v)
        except ValueError:
            self._outgoing[v] = {}
            if self.is_directed():
                self._incoming[v] = {}
            return v

    def insert_edge(self, u, v, x=None):
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_vertex(self, v):
        self._validate_vertex(v)
        for e in list(self._outgoing[v].keys()):
            self.remove_edge(Graph.Edge(v, e, None))
        if self.is_directed():
            for e in list(self._incoming[v].keys()):
                self.remove_edge(Graph.Edge(e, v, None))
            del self._incoming[v]
        del self._outgoing[v]

    def remove_edge(self, e):
        if not isinstance(e, Graph.Edge):
            raise TypeError('Edge expected')
        u, v = e.endpoints()
        self._validate_vertex(u)
        self._validate_vertex(v)
        del self._outgoing[u][v]
        del self._incoming[v][u]

    def remove_edge_uv(self, u, v):
        self.remove_edge(Graph.Edge(u, v, None))

    def __str__(self):
        return 'Outgoing:\n' + str(self._outgoing) + '\nIncoming:\n' + str(self._incoming)

    __repr__ = __str__
