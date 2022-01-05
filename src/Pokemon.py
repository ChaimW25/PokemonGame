import math

from DiGraph import DiGraph

EPS: float = 0.001*0.001


class Pokemon:

    def __init__(self, value: float, type: int, pos: str):

        self.value: float = value
        self.type: int = type
        self.loc = pos.split(',')
        self.pos = (float(self.loc[0]), float(self.loc[1]), float(self.loc[2]))
        self.location: tuple

    def set_graph(self, graph):
        self.graph = graph
        self.location: tuple = self.find_location()

    def get_value(self) -> float:
        return self.value

    def get_type(self) -> int:
        return self.type

    def get_pos(self) -> tuple:
        return self.pos

    def get_src(self) -> int:
        return self.location[0]

    def get_dest(self) -> int:
        return self.location[1]

    def find_location(self) -> (int, int):

        for src in self.graph.get_all_v().keys():
            for dest in self.graph.all_out_edges_of_node(src).keys():
                if self.is_location(src, dest):
                    return src, dest

        return -1, -1

    def is_location(self, src: int, dest: int) -> bool:

        if self.type < 0 and src < dest:
            return False

        if self.type > 0 and src > dest:
            return False

        src_pos: tuple = self.graph.get_all_v().get(src).getPos()
        dest_pos: tuple = self.graph.get_all_v().get(dest).getPos()

        dist: float = self.distance(src_pos, dest_pos)
        dist_to_pokemon: float = self.distance(src_pos, self.pos) + self.distance(dest_pos, self.pos)

        return dist > dist_to_pokemon - EPS

    def distance(self, src: tuple, dest: tuple):
        d = 0.0
        d = math.sqrt((src[0] - dest[0]) ** 2 + (src[1] - dest[1]) ** 2)
        return d

    def __lt__(self, pokemon):
        return self.value < pokemon.value
