"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""
import json

from types import SimpleNamespace
from src.Game.GameManager import GameManager

import pygame
from pygame import *
from pygame import gfxdraw
import time

from src.Game.client import Client

YELLOWPOKENON = pygame.image.load('../Images/pikachu.png')
AGENT = pygame.image.load('../Images/ash.png')
BACKGROUNDIMG = pygame.image.load('../Images/pknature.jpg')
ORANGEPOKEMON = pygame.image.load('../Images/orange.png')
WIDTH, HEIGHT = 1080, 720
radius = 15

pygame.init()
pygame.font.init()


class Gui:

    def __init__(self, client: Client):

        self.client = client
        self.clock = pygame.time.Clock()
        self.graph_json = self.client.get_graph()
        # gui icons:
        self.OurImg = pygame.transform.scale(BACKGROUNDIMG, (1080, 720))
        self.OurYellow = pygame.transform.scale(YELLOWPOKENON, (50, 50))
        self.OurAgent = pygame.transform.scale(AGENT, (50, 50))
        self.OurOrange = pygame.transform.scale(ORANGEPOKEMON, (50, 50))

        self.FONT = pygame.font.SysFont('Arial', 20, bold=True)
        self.screen = display.set_mode((WIDTH, HEIGHT), depth=32, flags=RESIZABLE)

        # load the json string into SimpleNamespace Object
        self.graph = json.loads(self.graph_json, object_hook=lambda json_dict: SimpleNamespace(**json_dict))
        # find the edges points of the graph:
        for n in self.graph.Nodes:
            x, y, _ = n.pos.split(',')
            n.pos = SimpleNamespace(x=float(x), y=float(y))
        # get data proportions
        self.min_x = min(list(self.graph.Nodes), key=lambda n: n.pos.x).pos.x
        self.min_y = min(list(self.graph.Nodes), key=lambda n: n.pos.y).pos.y
        self.max_x = max(list(self.graph.Nodes), key=lambda n: n.pos.x).pos.x
        self.max_y = max(list(self.graph.Nodes), key=lambda n: n.pos.y).pos.y

    def scale(self, data, min_screen, max_screen, min_data, max_data):
        """
        get the scaled data with proportions min_data, max_data
        relative to min and max screen dimentions
        """
        return ((data - min_data) / (max_data - min_data)) * (max_screen - min_screen) + min_screen

    # decorate scale with the correct values

    def my_scale(self, data, x=False, y=False) -> bool:
        if x:
            return self.scale(data, 50, self.screen.get_width() - 50, self.min_x, self.max_x)
        if y:
            return self.scale(data, 50, self.screen.get_height() - 50, self.min_y, self.max_y)

    def button(self, msg, x, y, w, h, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        pygame.draw.rect(self.screen, (255, 0, 0), (x, y, w, h))
        id_srg = self.FONT.render(msg, True, Color(0, 0, 0))
        rect4 = id_srg.get_rect(center=((x + (w / 2)), (y + (h / 2))))
        self.screen.blit(id_srg, rect4)
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            if click[0] == 1:
                action()

    def draw(self):

        # check events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

        pokemons = json.loads(self.client.get_pokemons(), object_hook=lambda d: SimpleNamespace(**d)).Pokemons
        pokemons = [p.Pokemon for p in pokemons]

        for p in pokemons:
            x, y, _ = p.pos.split(',')
            p.pos = SimpleNamespace(x=self.my_scale(float(x), x=True), y=self.my_scale(float(y), y=True))

        agents = json.loads(self.client.get_agents(), object_hook=lambda d: SimpleNamespace(**d)).Agents
        agents = [agent.Agent for agent in agents]

        for a in agents:
            x, y, _ = a.pos.split(',')
            a.pos = SimpleNamespace(x=self.my_scale(float(x), x=True), y=self.my_scale(float(y), y=True))

        # refresh surface
        self.screen.blit(self.OurImg, (0, 0))
        time_left = int(self.client.time_to_end())
        seconds, milliseconds = divmod(time_left, 1000)
        self.screen.blit(self.FONT.render('Time left: {}.{}'.format(seconds, milliseconds), True, (0, 0, 0)), (100, 0))
        self.button("STOP", 200, 50, 50, 50, self.client.stop)

        # print moves
        moves = json.loads(self.client.get_info(), object_hook=lambda d: SimpleNamespace(**d))  # .GameServer
        curr_moves = moves.GameServer.moves
        curr_grade = moves.GameServer.grade
        self.screen.blit(self.FONT.render('Number of moves: {}'.format(curr_moves), True, (0, 0, 0)), (100, 30))

        # print grade
        self.screen.blit(self.FONT.render('Grade: {}'.format(curr_grade), True, (0, 0, 0)), (100, 60))

        # draw nodes
        for n in self.graph.Nodes:
            x = self.my_scale(n.pos.x, x=True)
            y = self.my_scale(n.pos.y, y=True)

            # its just to get a nice antialiased circle
            gfxdraw.filled_circle(self.screen, int(x), int(y), radius, Color(64, 80, 174))
            gfxdraw.aacircle(self.screen, int(x), int(y), radius, Color(255, 255, 255))

            # draw the node id
            id_srf = self.FONT.render(str(n.id), True, Color(255, 255, 255))
            rect = id_srf.get_rect(center=(x, y))
            self.screen.blit(id_srf, rect)

        # draw edges
        for e in self.graph.Edges:
            # find the edge nodes
            src = next(n for n in self.graph.Nodes if n.id == e.src)
            dest = next(n for n in self.graph.Nodes if n.id == e.dest)

            # scaled positions
            src_x = self.my_scale(src.pos.x, x=True)
            src_y = self.my_scale(src.pos.y, y=True)
            dest_x = self.my_scale(dest.pos.x, x=True)
            dest_y = self.my_scale(dest.pos.y, y=True)


            # draw the line
            pygame.draw.line(self.screen, Color(61, 72, 126), (src_x, src_y), (dest_x, dest_y))

        # draw agents
        for agent in agents:
            # pygame.draw.circle(screen, Color(122, 61, 23),(int(agent.pos.x), int(agent.pos.y)), 10)
            self.screen.blit(self.OurAgent, ((int(agent.pos.x),
                                              int(agent.pos.y))))  # .circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)

        # draw pokemons (note: should differ (GUI wise) between the up and the down pokemons (currently they are marked in the same way).
        for p in pokemons:
            if p.type < 0:
                self.screen.blit(self.OurYellow, ((int(p.pos.x), int(p.pos.y))))  # .circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)
            else:
                self.screen.blit(self.OurOrange, ((int(p.pos.x),int(p.pos.y))))  # .circle(screen, Color(0, 255, 255), (int(p.pos.x), int(p.pos.y)), 10)

        # update screen changes
        display.update()

        # refresh rate
        self.clock.tick(60)

