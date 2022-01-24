import string

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
      coords = self.get_coords_from_user()
      successfully_placed = self.ships.try_place_ship(self.ship, coords)
    return coords

  def _rotate_ship(self, coords):
    successfully_placed = False
    while not successfully_placed:
      self.ship.flip_orientation()
      successfully_placed = self.ships.try_place_ship(self.ship, coords)    

  def get_coords_from_user(self):
    row = self._get_row_from_user()
    col = self._get_col_from_user()
    return (row, col)

  def _get_row_from_user(self):
    max_alpha_i = string.ascii_uppercase[GRID -1]
    prompt = f'Select a row (A-{max_alpha_i}): '

    row = ''
    while not self._valid_row(row):
      row = input(prompt).lower()
    row = string.ascii_lowercase.index(row) + 1
    return row

  def _get_col_from_user(self):
    col = 0
    while not self._valid_col(col):
      col = validate_int_input(f'Select a column (1-{GRID}): ')
    return col

  def _valid_row(self, row: str):
    if not row.isalpha(): return False
    i = string.ascii_lowercase.index(row)
    return i < GRID and not i < 0

  def _valid_col(self, col: int):
    return col < GRID and not col < 1