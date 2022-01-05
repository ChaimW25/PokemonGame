import json

from client import Client
from Pokemon import Pokemon
from GameInfo import GameInfo
from Agent import Agent
from GraphAlgo import GraphAlgo


class GameManager:

    def __init__(self, client: Client):

        self.client = client
        self.info = None
        self.pokemons = []
        self.agents = []
        self.graphAlgo = GraphAlgo()

        self.load_info()
        self.load_graph()

    def load_info(self):
        json_info = json.loads(self.client.get_info())
        self.info = GameInfo(**json_info["GameServer"])

    def load_graph(self):
        self.graphAlgo.load_from_json(self.info.get_graph_name())
        print(self.graphAlgo)

    def load_pokemon(self):

        json_pokemons = json.loads(self.client.get_pokemons())
        for p in json_pokemons["Pokemons"]:
            po = Pokemon(**p["Pokemon"])
            po.set_graph(self.graphAlgo.get_graph())
            self.pokemons.append(po)

    def load_agent(self):

        json_agent = json.loads(self.client.get_agents())
        self.agents = []
        for a in json_agent["Agents"]:
            ad = Agent(**a["Agent"])
            self.agents.append(ad)
