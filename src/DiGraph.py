from Node import Node


class DiGraph:

    def __init__(self):
        self.Nodes: dict = {}
        self.outEdges: dict = {}
        self.inEdges: dict = {}
        self.mcCounter: int = 0
        self.nodesCounter: int = 0
        self.edgesCounter: int = 0

    def v_size(self) -> int:
        return self.nodesCounter

    def e_size(self) -> int:
        return self.edgesCounter

    def get_all_v(self) -> dict:
        return self.Nodes

    def all_in_edges_of_node(self, id1: int) -> dict:
        return self.inEdges.get(id1)

    def all_out_edges_of_node(self, id1: int) -> dict:
        return self.outEdges.get(id1)

    def get_mc(self) -> int:
        return self.mcCounter

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:

        if self.Nodes.__contains__(id1) and \
                self.Nodes.__contains__(id2) and id1 != id2 and \
                not self.outEdges[id1].__contains__(id2):
            self.outEdges[id1][id2] = weight
            self.get_all_v().get(id1).addEdgeOut()
            self.inEdges[id2][id1] = weight
            self.get_all_v().get(id2).addEdgeIn()
            self.edgesCounter += 1
            self.mcCounter += 1
            return True

        return False

    def add_node(self, node_id: int, pos: tuple = None) -> bool:

        if self.Nodes.__contains__(node_id):
            return False

        self.Nodes[node_id] = Node(node_id, pos)
        self.inEdges[node_id] = {}
        self.outEdges[node_id] = {}
        self.nodesCounter += 1
        self.mcCounter += 1

        return True

    def remove_node(self, node_id: int) -> bool:

        if self.Nodes.__contains__(node_id):
            out = self.all_out_edges_of_node(node_id)
            for i in out:
                self.inEdges[i].pop(node_id)
            self.outEdges.pop(node_id)
            self.edgesCounter -= out.__len__()
            self.mcCounter += out.__len__()

            inside = self.all_in_edges_of_node(node_id)
            for i in inside:
                self.outEdges[i].pop(node_id)
                self.edgesCounter -= 1
                self.mcCounter += 1

            self.inEdges.pop(node_id)
            self.Nodes.pop(node_id)
            self.nodesCounter -= 1
            self.mcCounter += 1
            return True

        return False

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:

        if self.outEdges[node_id1].__contains__(node_id2):
            self.outEdges[node_id1].pop(node_id2)
            self.get_all_v().get(node_id1).removeEdgeOut()
            self.inEdges[node_id2].pop(node_id1)
            self.get_all_v().get(node_id2).removeEdgeIn()
            self.edgesCounter -= 1
            self.mcCounter += 1
            return True
        return False
    #
    # def __str__(self):
    #     return f"num of nodes: {self.nodesCounter}, num of edges: {self.edgesCounter}, mc: {self.mcCounter}," \
    #            f" nodes: {self.Nodes}, edges: {self.outEdges}, in edges: {self.inEdges}"

    def __repr__(self):
        return 'Graph: |V|={}, |E|={}'.format(self.nodesCounter, self.edgesCounter)