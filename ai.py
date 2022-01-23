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
    self._place_ships_randomly()
    self._display_place_ship_progress()
    
    self.game_board.display_for_self()
    input('press return')

  def _display_place_ship_progress(self):
    i = 0
    msg = f'{self.name} is placing ships.'
    while i < 5:
      clear_console()
      pause = random.uniform(0.5, 1)
      print(msg)
      time.sleep(pause)
      msg += '.'
      i += 1