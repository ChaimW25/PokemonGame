from unittest import TestCase
import unittest
from src.Graph.GraphAlgo import GraphAlgo
from src.Game.GameManager import GameManager


class ClientTset:
    """
    A class that simulates the Client class we created for the test.
    (The tests below of this class).
    """

    def __init__(self):
        self.agents: str = """
        {
            "Agents":[
                {
                    "Agent":
                    {
                        "id":0,
                        "value":0.0,
                        "src":0,
                        "dest":1,
                        "speed":1.0,
                        "pos":"35.18753053591606,32.10378225882353,0.0"
                    }
                }
            ]
        }
        """
        self.info: str = """
        {
            "GameServer":{
                "pokemons":1,
                "is_logged_in":false,
                "moves":1,
                "grade":0,
                "game_level":0,
                "max_user_level":-1,
                "id":0,
                "graph":"data/A0",
                "agents":1
            }
        }
        """
        self.pokemons = """
        {
            "Pokemons":[
                {
                    "Pokemon":{
                        "value":5.0,
                        "type":-1,
                        "pos":"35.197656770719604,32.10191878639921,0.0"
                    }
                }
            ]
        }
        """
        self.graphAlgo = GraphAlgo()
        self.graphAlgo.load_from_json("data/A0")

    def get_pokemons(self):
        return self.pokemons

    def get_info(self) -> str:
        return self.info

    def get_agents(self):
        return self.agents

    def add_agent(self, json_of_node):
        return json_of_node

    def choose_next_edge(self, next_agent_node_json):
        return next_agent_node_json


class TestGameManager(TestCase):

    def test_load_pokemon(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.load_pokemon()
        self.assertEqual(1, len(self.game_manager.pokemons))
        self.assertEqual(5, self.game_manager.pokemons[0].get_value())  # value = 5.0
        self.assertEqual(-1, self.game_manager.pokemons[0].get_type())  # type = -1

    def test_load_agent(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.load_agent()
        self.assertEqual(1, len(self.game_manager.agents))
        self.assertEqual(0, self.game_manager.agents[0].get_id())  # id = 0
        self.assertEqual(1, self.game_manager.agents[0].get_speed())  # speed = 1.0
        self.assertEqual(0, self.game_manager.agents[0].get_src())  # src = 0
        self.assertEqual(1, self.game_manager.agents[0].get_dest())  # dest = 1

    def test_update(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.update()
        self.assertNotEqual(None, self.game_manager.info)
        self.assertEqual(1, len(self.game_manager.agents))  # num of agents = 1
        self.assertEqual(1, len(self.game_manager.pokemons))  # num of pokemons = 1

    def test_load_info(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.load_info()
        self.assertEqual(1, self.game_manager.info.num_of_agents())
        self.assertEqual(1, self.game_manager.info.num_of_pokemons())
        self.assertEqual('data/A0', self.game_manager.info.get_graph_name())

    def test_load_graph(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.load_graph()
        self.assertEqual(11, self.game_manager.graphAlgo.get_graph().v_size())

    def test_allocate_all_agents(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.assertFalse(self.game_manager.allocate_all_agents())

    def test_allocate_agent_dest(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.load_agent()
        self.game_manager.allocate_agent_dest(self.game_manager.agents[0])
        self.assertEqual(0, len(self.game_manager.pokemons))
        self.assertEqual(0, self.game_manager.agents[0].get_src())  # src = 0
        self.assertEqual(1, self.game_manager.agents[0].get_dest())  # dest = 1


    def test_add_agents(self):
        client = ClientTset()
        self.game_manager = GameManager(client)
        self.game_manager.load_agent()
        self.game_manager.add_agents()
        self.assertEqual(1, len(self.game_manager.agents))
        self.assertEqual(0, self.game_manager.agents[0].get_id())  # id = 0
        self.assertEqual(0, self.game_manager.agents[0].get_src())  # src = 0
        self.assertEqual(1, self.game_manager.agents[0].get_dest())  # dest = 1


if __name__ == '__main__':
    unittest.main()



