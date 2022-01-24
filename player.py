import random
import string

from constant import SET_BOARD_MENU, GRID
from gameBoard import GameBoard
from helpers import clear_console, validate_int_input
from ship import Ship
from ships import Ships

# FIXME: refactor for parent Player class -> human, ai subclasses

class Player:
  def __init__(self):
    self.name = ''
    self.game_board = GameBoard()
    self.ships = Ships.init_ships()

  def setup(self, player_num, player1_name):
    self.set_name(player_num, player1_name)
    # boardSetupMenu

  def set_name(self): pass

  def place_ship(self, ship):
    pass

  # def place_ships(self):
  #   if self._run_board_setup(): print('game on')
  #   return

  # FIXME: move to place_ships_menu class
  # def _run_manual_menu(self, ship: Ship):
    

  