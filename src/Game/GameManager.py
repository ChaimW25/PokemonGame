import json
import math
import queue

from src.Game.client import Client
from Pokemon import Pokemon
from GameInfo import GameInfo
from src.Game.Agent import Agent
from src.Graph.GraphAlgo import GraphAlgo


class GameManager:

    def __init__(self, client: Client):

        self.client = client
        self.info: GameInfo = None
        self.pokemons = []
        self.agents = []
        self.graphAlgo = GraphAlgo()

        self.load_info()
        self.load_graph()
        self.add_agents()

    # the function update the info, the agents list, and the pokemons list.
    def update(self):

        self.load_info()
        self.load_agent()
        self.load_pokemon()

    def allocate_all_agents(self):

        """
        Go through all the agents, in case one of the agents is at rest,
        the function sends it to a function that will locate the nearest
        Pokemon and update the agent's destination accordingly.
        """

        self.update()
        for agent in self.agents:
            if agent.get_dest() == -1:
                self.allocate_agent_dest(agent)

    def allocate_agent_dest(self, agent: Agent):

        """
        The function receives an agent and locates the nearest
        Pokemon and updates the agent's destination accordingly.
        :param agent:
        """

        min_dist: float = math.inf
        dest: int = -1

        for pok in self.pokemons:
            temp_dist, path = self.graphAlgo.shortest_path(agent.get_src(), pok.get_src())
            temp_dist = temp_dist / agent.get_speed()
            if temp_dist < min_dist:
                min_dist = temp_dist
                if min_dist == 0:
                    dest = pok.get_dest()
                else:
                    dest = path[1]

        self.client.choose_next_edge('{"agent_id":'+str(agent.get_id())+', "next_node_id":'+str(dest)+'}')

    def add_agents(self):

        self.load_pokemon()
        q = queue.PriorityQueue()

        for pok in self.pokemons:
            q.put(pok)

        for i in range(self.info.num_of_agents()):
            if not q.empty():
                pok: Pokemon = q.get()
                self.client.add_agent("{\"id\":" + str(pok.get_src()) + "}")
            else:
                self.client.add_agent("{\"id\":" + str(i+1 % self.graphAlgo.get_graph().nodesCounter) + "}")

    # loads game info to info
    def load_info(self):

        json_info = json.loads(self.client.get_info())
        self.info = GameInfo(**json_info["GameServer"])

    # loads the graph to graphAlgo
    def load_graph(self):

        self.graphAlgo.load_from_json(self.info.get_graph_name())
        print(self.graphAlgo)

    # loads the pokemons to list of pokemons
    def load_pokemon(self):

        json_pokemons = json.loads(self.client.get_pokemons())
        self.pokemons = []
        for p in json_pokemons["Pokemons"]:
            po = Pokemon(**p["Pokemon"])
            po.set_graph(self.graphAlgo.get_graph())
            self.pokemons.append(po)

    # loads the agents to list of agents
    def load_agent(self):

        json_agent = json.loads(self.client.get_agents())
        self.agents = []
        for a in json_agent["Agents"]:
            ad = Agent(**a["Agent"])
            self.agents.append(ad)
