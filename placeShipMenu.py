import string
import coords

from gameBoard import GameBoard
from ship import Ship
from ships import Ships

from constant import GRID
from helpers import clear_console, validate_int_input

class PlaceShipMenu:
  def __init__(self, player, ship: Ship):
    self.ship = ship
    self.game_board: GameBoard = player.game_board
    self.ships: Ships = self.game_board.ships
    self.done = False
    self.run()

  def run(self):
    coords = self._select_coords()
    prompt = f'''
Placing {self.ship.name}
  1) Select coordinates
  2) Rotate {self.ship.name}
  3) Confirm placement
'''
    while not self.done:
      clear_console()
      self.game_board.build_cells()
      self.game_board.display()

      userInput = validate_int_input(prompt)
      match userInput:
        case 1: coords = self._select_coords()
        case 2: self._rotate_ship(coords)
        case 3: self.done = True

  def _select_coords(self):
    successfully_placed = False
    while not successfully_placed:
      bow_coords = coords.get_from_user()
      successfully_placed = self.ships.try_place_ship(self.ship, bow_coords)
    return bow_coords

  def _rotate_ship(self, coords):
    successfully_placed = False
    while not successfully_placed:
      self.ship.flip_orientation()
      successfully_placed = self.ships.try_place_ship(self.ship, coords)    