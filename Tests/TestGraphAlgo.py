import unittest
from unittest import TestCase

from src.Graph.DiGraph import DiGraph
from src.Graph.GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):

    def test_load_save_json(self):
        file_path = 'data/A5.json'
        ga = GraphAlgo()
        self.assertTrue(ga.load_from_json(file_path))

    def test_shortest_path(self):
        g = self.simple_graph_generate()
        ga = GraphAlgo(g)
        self.assertEqual((3.0, [1, 2, 3, 7]), ga.shortest_path(1, 7))
        self.assertEqual((float("inf"), []), ga.shortest_path(1, 88))
        self.assertEqual((9, [3, 7, 8, 9]), ga.shortest_path(3, 9))

    def test_tsp(self):
        g = self.simple_graph_generate()
        ga = GraphAlgo(g)
        self.assertEqual(([1, 2, 8], 1.5), ga.TSP([1, 8]))
        self.assertEqual(([7,8,9,1], 12), ga.TSP([7, 1]))
        self.assertEqual(([7,3,4,6,7,8,9,1], 22), ga.TSP([7, 1, 4, 9]))

    def test_center_point(self):
        # test center of A0.json:
        file = 'data/A0'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((7, 6.806805834715163), graphAlgo.centerPoint())

        # test center of A1.json:
        file = 'data/A1'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((8, 9.925289024973141), graphAlgo.centerPoint())

        # test center of A2.json:
        file = 'data/A2'
        graphAlgo = GraphAlgo()
        self.assertTrue(graphAlgo.load_from_json(file))
        self.assertEqual((0, 7.819910602212574), graphAlgo.centerPoint())


    @staticmethod
    def simple_graph_generate():
        g = DiGraph()
        for i in range(10):
            g.add_node(i)

        for i in range(10):
            g.add_edge(i, 10 - i, i * 0.5)
            g.add_edge(i, i + 1, i * 0.5)
        return g


if __name__ == '__main__':
    unittest.main()
