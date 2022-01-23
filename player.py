import random
import string

from constant import SET_BOARD_MENU, GRID, MANUAL_PLACE_MENU
from gameBoard import GameBoard
from helpers import clear_console, validate_int_input
from ship import Ship, init_ships

# FIXME: refactor for parent Player class -> human, ai subclasses

class Player:
  def __init__(self):
    self.name = ''
    self.game_board = GameBoard()
    self.ships = init_ships()

  def setup(self, player_num, player1_name):
    self.set_name(player_num, player1_name)
    self.place_ships()

  def set_name(self): pass
  
  def place_ships(self):
    if self._run_board_setup(): print('game on')
    return

  def _run_board_setup(self):
    self.game_board.display_for_self()
    # FIXME: move to Set_Board class
    while True:
      userInput = validate_int_input(SET_BOARD_MENU)

      match userInput:
        case 1: self._place_ships_manually()
        case 2:
          self._place_ships_randomly()
          self.game_board.display_for_self()
        case 3: pass # move ship (select ship menu)
        case 4: pass # clear board (need method)
        case 5: return True
        case 6: return False

  def _place_ships_manually(self):
    for ship in self.ships:
      self._run_manual_menu(ship)

  # FIXME: move to place_ships_menu class
  def _run_manual_menu(self, ship: Ship):
    prompt = MANUAL_PLACE_MENU
    successfully_placed = False
    vertical = True
    coords = (10, 10)

    while not successfully_placed:
      clear_console()
      orientation = 'Vertical' if vertical else 'Horizontal'
      self.game_board.display_for_self()
      print(f'Placing {ship.name}')

      userInput = validate_int_input(prompt)
      match userInput:
        case 1: 
          coords = (10, 10)
          while not self.game_board.try_place_ship(ship,coords,vertical):
            coords = self.get_coords_from_user()
            print('Invalid placement!: ')
        case 2:
          vertical = not vertical
          if not self.game_board.try_place_ship(ship,coords,vertical):
            print('Invalid placement!: ')
            vertical = True
        case 3:
          if self.game_board.try_place_ship(ship, coords, vertical):
            successfully_placed = True

  def _place_ships_randomly(self):
    for ship in self.ships:
      successfully_placed = False
      while not successfully_placed:
        coords = self._rand_cell()
        vertical = self._rand_bool()
        successfully_placed = self.game_board.try_place_ship(ship, coords, vertical)

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
    if i < GRID and not i < 0: return True
    return False

  def _valid_col(self, col: int):
    if col < GRID and not col < 1:
      return True
    return False
  
  def _rand_cell(self):
    row = random.randint(1, GRID)
    col = random.randint(1, GRID)
    return (row, col)

  def _rand_bool(self):
    return random.randint(0, 1)