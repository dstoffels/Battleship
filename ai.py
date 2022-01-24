import random
import time

import coords
from constant import AI_NAMES
from helpers import clear_console

from player import Player

class AI(Player):

  # TODO: make AI smarter by detecting hits and targeting nearby
  def select_target(self):
      return coords.random_coords()

  def _setup_game_board(self):
    self.place_ships_randomly()

  # ensure player & ai don't share the same name
  def _set_name(self):
    while self.name == '':
      name = random.choice(AI_NAMES)
      if name != self.opponent.name:
        self.name = name
  
  def place_ships(self):
    self.place_ships_randomly()
    self._display_place_ship_progress()
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