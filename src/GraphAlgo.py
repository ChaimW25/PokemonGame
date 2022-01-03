import json
import math
from typing import List
import queue
from GraphAlgoInterface import GraphAlgoInterface
from GraphInterface import GraphInterface
from DiGraph import DiGraph
import matplotlib.pyplot as plt
from Node import Node
import random


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: GraphInterface = None):
        self.graph = g

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:

        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
                g = DiGraph()
                for i in data['Nodes']:
                    if 'pos' in i.keys():
                        str_lst = i['pos'].split(',')
                        pos = (float(str_lst[0]), float(str_lst[1]))
                        g.add_node(i['id'], pos)
                    else:
                        pos=(random.randint(35185,35215)/1000, random.randint(32101,32108)/1000)
                       # pos=(random.randint(0,10000)/1000, random.randint(0,10000)/1000)
                        g.add_node(i['id'], pos)
                for i in data['Edges']:
                    g.add_edge(i['src'], i['dest'], i['w'])
                self.graph = g

        except Exception as e:
            print(e)
            return False

        return True

    def save_to_json(self, file_name: str) -> bool:

        newJson = dict()
        newJson["Edges"] = list()
        newJson["Nodes"] = list()

        for node in self.graph.get_all_v().values():
            if node.getPos() is None:
                pos = '0.0,0.0,0.0'
            else:
                pos = str(str(node.getPos()[0]) + ',' + str(node.getPos()[1]) + ',0.0')
            newJson["Nodes"].append({"pos": pos, "id": node.getId()})
            for edge in self.graph.all_out_edges_of_node(node.getId()).items():
                newJson["Edges"].append({"src": node.getId(), "w": edge[1], "dest": edge[0]})

        try:
            with open(file_name, 'w') as json_f:
                json.dump(newJson, json_f)
                return True

        except IOError:
            return False

    def shortest_path(self, id1: int, id2: int) -> (float, list):

        shortestPath: list = []
        if (id1 not in self.graph.get_all_v().keys()) or (id2 not in self.graph.get_all_v().keys()):
            return math.inf, []

        elif id1 == id2:
            shortestPath.append(id1)
            return 0, shortestPath

        self.dijkstra(id1, id2)
        temp: int = id2
        shortestPath.append(id2)
        while temp != id1:
            temp = self.graph.get_all_v().get(temp).getTag()
            shortestPath.append(temp)
            if temp == -1:
                return math.inf, []

        shortestPath.reverse()
        shortestPathDist: float = self.graph.get_all_v().get(id2).getWeight()
        return shortestPathDist, shortestPath

    def TSP(self, node_lst: List[int]) -> (List[int], float):
        tsp: list = []
        tempNode: int = node_lst.pop(0)
        tsp.append(tempNode)
        citiesSet: set = set(node_lst)
        distTSP: float = 0
        nodeToAdd: int = -1
        minDist: float = math.inf

        while len(citiesSet) > 0:
            listToAdd: list = []
            minDist = math.inf
            for node in citiesSet:
                tempDist, shortestPath = self.shortest_path(tempNode, node)
                shortestPath.pop(0)
                if tempDist < minDist:
                    minDist = tempDist
                    listToAdd = shortestPath
                    nodeToAdd = node

            distTSP += minDist
            tsp = tsp + listToAdd
            citiesSet.remove(nodeToAdd)
            tempNode = nodeToAdd

        return tsp, distTSP

    def centerPoint(self) -> (int, float):

        center: int = -1
        minWeight: float = math.inf

        for node in self.graph.get_all_v().values():
            self.dijkstra(node.getId(), -1)
            maxWeight: float = 0
            for secondNode in self.graph.get_all_v().values():
                if secondNode.getWeight() == math.inf:
                    return None, math.inf
                if secondNode.getWeight() > maxWeight:
                    maxWeight = secondNode.getWeight()

            if maxWeight < minWeight:
                minWeight = maxWeight
                center = node.getId()

        return center, minWeight

    def plot_graph(self) -> None:
        x = []
        y = []
        for node in self.get_graph().get_all_v().values():
            if node.getPos() is not None:
                x.append(node.getPos()[0])
                y.append(node.getPos()[1])
            else:
                pos = (random.randint(35185, 35215) / 1000, random.randint(32101, 32108) / 1000)
                # pos=(random.randint(0,10000)/1000, random.randint(0,10000)/1000)
                x.append(pos[0])
                y.append(pos[1])
                newPos= (pos[0], pos[1], 0.0)
                node.setPos(newPos)
        # define a default color for the nodes and paint them
        plt.plot(x, y, 'bo')
        for i in range(len(x)):
            # paint the nodes id near the nodes in the graph
            plt.annotate(i, xy=(x[i] * 0.999992, y[i] * 1.000007))
        #paint the edges
        for nodeId in self.get_graph().get_all_v().keys():
            if self.get_graph().all_out_edges_of_node(nodeId) is not None:
                for edge in self.get_graph().all_out_edges_of_node(nodeId).keys():
                    xDest = self.get_graph().get_all_v().get(edge).getPos()[0]
                    yDest = self.get_graph().get_all_v().get(edge).getPos()[1]
                    xSrc = self.get_graph().get_all_v().get(nodeId).getPos()[0]
                    ySrc = self.get_graph().get_all_v().get(nodeId).getPos()[1]
                    # paint the arrows
                    plt.annotate("", xy=(xSrc, ySrc), xytext=(xDest, yDest), arrowprops={'arrowstyle': "<|-", 'lw': 1})
        plt.show()

    def dijkstra(self, src: int, dest: int):
        self.initTIW()
        q = queue.PriorityQueue()
        srcNode: Node = self.graph.get_all_v().get(src)
        srcNode.setWeight(0)
        q.put(srcNode)

        while not q.empty():
            u: Node = q.get()
            if u.getInfo() is None:
                u.setInfo("V")
                if u.getId() == dest:
                    return
                for outEdge, edgeWeight in self.graph.all_out_edges_of_node(u.getId()).items():
                    tempNode: Node = self.graph.get_all_v().get(outEdge)
                    if tempNode.getInfo() is None:
                        w: float = edgeWeight + u.getWeight()
                        if w < tempNode.getWeight():
                            tempNode.setWeight(w)
                            tempNode.setTag(u.getId())
                    q.put(tempNode)

    def initTIW(self):
        for node in self.graph.get_all_v().values():
            node.setTag(-1)
            node.setInfo(None)
            node.setWeight(math.inf)