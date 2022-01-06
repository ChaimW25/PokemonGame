"""
@author AchiyaZigi
OOP - Ex4
Very simple GUI example for python client to communicates with the server and "play the game!"
"""

from src.Game.GameManager import GameManager
from Gui import Gui
import time
from src.Game.client import Client

# default port
PORT = 6666
# server host (default localhost 127.0.0.1)
HOST = '127.0.0.1'

client = Client()
client.start_connection(HOST, PORT)

Gui = Gui(client)
manager = GameManager(client)
client.start()
while client.is_running() == 'true':
    Gui.draw()
    manager.update()
    manager.allocate_all_agents()
    client.move()
    time.sleep(0.1)
