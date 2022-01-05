import math


class Node:

    def __init__(self, id: int, pos: tuple = None):
        self.pos = pos
        self.id = id
        self.weight: float = math.inf
        self.tag: int = 0
        self.info: str = ""
        self.edges_out: int = 0
        self.edges_in: int = 0

    def getId(self) -> int:
        return self.id

    def getPos(self) -> tuple:
        return self.pos

    def setPos(self, pos: tuple):
        self.pos = pos

    def getWeight(self) -> float:
        return self.weight

    def setWeight(self, weight: float):
        self.weight = weight

    def getInfo(self) -> str:
        return self.info

    def setInfo(self, info: str):
        self.info = info

    def getTag(self) -> int:
        return self.tag

    def setTag(self, tag: int):
        self.tag = tag

    def addEdgeIn(self):
        self.edges_in += 1

    def addEdgeOut(self):
        self.edges_out += 1

    def removeEdgeIn(self):
        self.edges_in -= 1

    def removeEdgeOut(self):
        self.edges_out -= 1

    def __lt__(self, node):
        return self.weight < node.weight

    def __repr__(self):
        return '{}: |edges_out| {} |edges in| {}'.format(self.getId(), self.edges_out, self.edges_in)