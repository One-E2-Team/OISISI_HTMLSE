class Graph:
    class Edge:
        def __init__(self, u, v, x):
            self._origin = u
            self._destination = v
            self._element = x

        def endpoints(self):
            """
            O(1)
            :return: tuple with vertices - endpoints
            """
            return self._origin, self._destination

        def opposite(self, v):
            """
            returns opposite vertex on edge, O(1)
            :param v: given vertex
            :return: opposite vertex
            """
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
        """
        Checks if a given vertex is in graph (otherwise raises ValueError), in O(1), abs worst case is O(n).
        :param v: given vertex
        :return: None
        """
        if v not in self._outgoing:
            raise ValueError('Vertex does not belong to this graph.')

    def is_directed(self):
        """
        O(1)
        :return:
        """
        return self._incoming is not self._outgoing

    def vertex_count(self):
        return len(self._outgoing)

    def vertices(self):
        return self._outgoing.keys()

    def edge_count(self):
        total = sum(len(self._outgoing[v]) for v in self._outgoing)
        return total if self.is_directed() else total // 2

    def edges(self):
        """
        Never used, so don't mind the forbidden apple in form of set()
        :return:
        """
        result = set()  # avoid double-reporting edges of undirected graph
        for secondary_map in self._outgoing.values():
            result.update(secondary_map.values())  # add edges to resulting set
        return result

    def get_edge(self, u, v):
        """
        O(1) brought to you by the power of hash map
        :param u: vertex 1
        :param v: vertex 2
        :return: edge if vertices are adjacent, otherwise None
        """
        self._validate_vertex(u)
        self._validate_vertex(v)
        return self._outgoing[u].get(v)  # returns None if v not adjacent

    def degree(self, v, outgoing=True):
        """
        returns degree of a vertex in graph, O(1)
        :param v: vertex
        :param outgoing: graph type
        :return: degree (integer)
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        return len(adj[v])

    def incident_edges(self, v, outgoing=True):
        """
        returns a generator object of incident edges for a vertex O(m), m connected vertices
        :param v: vertex
        :param outgoing: type
        :return: generator object
        """
        self._validate_vertex(v)
        adj = self._outgoing if outgoing else self._incoming
        for edge in adj[v].values():
            yield edge

    def insert_vertex(self, v):
        """
        Inserts lone vertex, exception on already existing vertex, in O(1)
        :param v: vertex
        :return: vertex
        """
        try:
            self._validate_vertex(v)
        except ValueError:
            self._outgoing[v] = {}
            if self.is_directed():
                self._incoming[v] = {}
            return v

    def insert_edge(self, u, v, x=None):
        """
        Inserts edge in O(1)
        :param u: vertex 1
        :param v: vertex 2
        :param x: edge weight
        :return: None (can raise exceptions)
        """
        if self.get_edge(u, v) is not None:  # includes error checking
            raise ValueError('u and v are already adjacent')
        e = self.Edge(u, v, x)
        self._outgoing[u][v] = e
        self._incoming[v][u] = e

    def remove_vertex(self, v):
        """
        Removes all edges on given vertex and the vertex itself, in O(m), m connected edges
        :param v: vertex
        :return: None
        """
        self._validate_vertex(v)
        for e in list(self._outgoing[v].keys()):
            self.remove_edge(Graph.Edge(v, e, None))
        if self.is_directed():
            for e in list(self._incoming[v].keys()):
                self.remove_edge(Graph.Edge(e, v, None))
            del self._incoming[v]
        del self._outgoing[v]

    def remove_edge(self, e):
        """
        Removes given edge in O(1)
        :param e: edge
        :return: None (method can raise exceptions)
        """
        if not isinstance(e, Graph.Edge):
            raise TypeError('Edge expected')
        u, v = e.endpoints()
        self._validate_vertex(u)
        self._validate_vertex(v)
        del self._outgoing[u][v]
        del self._incoming[v][u]

    def remove_edge_uv(self, u, v):
        """
        removes edge by given vertices, in O(1)
        :param u: vertex 1
        :param v: vertex 2
        :return: None (method can raise exceptions)
        """
        self.remove_edge(Graph.Edge(u, v, None))

    def __str__(self):
        return 'Outgoing:\n' + str(self._outgoing) + '\nIncoming:\n' + str(self._incoming)

    __repr__ = __str__
