import random
import time

from constant import AI_NAMES, GRID
from helpers import clear_console, index_len

from player import Player

class AI(Player):
  def __init__(self):
    super().__init__()

  def set_name(self, player_num, player1_name):
    # ensure player & ai don't share the same name
    self.name = player1_name
    while self.name == player1_name:
      i = random.randint(0, index_len(AI_NAMES))
      self.name = AI_NAMES[i]
  
  def place_ships(self):
    for ship in self.ships:
      successfully_placed = False
      while not successfully_placed:
        coords = self.rand_cell()
        vertical = self.rand_bool()
        successfully_placed = self.board.try_place_ship(ship, coords, vertical)

    i = 0
    msg = f'{self.name} is placing ships.'
    while i < 5:
      clear_console()
      pause = random.uniform(0.5, 2)
      print(msg)
      time.sleep(pause)
      msg += '.'
      i += 1
    
    self.board.display_for_player()
    input('press return')

  def rand_cell(self):
    row = random.randint(1, GRID)
    col = random.randint(1, GRID)
    return (row, col)

  def rand_bool(self):
    return random.randint(0, 1)