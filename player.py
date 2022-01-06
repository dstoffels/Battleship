import random
import string

from constant import BOARD_SETUP_MENU, GRID, MANUAL_PLACE_MENU
from gameBoard import GameBoard
from helpers import clear_console, validate_int_input
from ship import Ship, load_ships

class Player:
  def __init__(self):
    self.name = ''
    self.board = GameBoard()
    self.ships = load_ships()

  def setup(self, player_num, player1_name):
    self.set_name(player_num, player1_name)
    self.place_ships()

  def set_name(self, player_num, player1_name):
    prompt = f'Enter a name for player {player_num}: '
    self.name = player1_name
    while self.name == player1_name:
      name = input(prompt)
      if name == '': continue
      elif str.lower(name) == str.lower(player1_name): prompt = 'Player names cannot be the same! Enter a different name: '
      else: self.name = name
  
  def place_ships(self):
    if self._run_board_setup_menu(): print('game on')
    return

  def _run_board_setup_menu(self):
    self.board.display_for_player()

    while True:
      userInput = validate_int_input(BOARD_SETUP_MENU)

      match userInput:
        case 1: self._place_ships_manually()
        case 2:
          self._place_ships_randomly()
          self.board.display_for_player()
        case 3: pass # move ship (select ship menu)
        case 4: pass # clear board (need method)
        case 5: return True
        case 6: return False

  def _place_ships_manually(self):
    for ship in self.ships:
      self._run_manual_menu(ship)

  def _run_manual_menu(self, ship: Ship):
    prompt = MANUAL_PLACE_MENU
    successfully_placed = False
    vertical = True
    coords = (10, 10)

    while not successfully_placed:
      clear_console()
      orientation = 'Vertical' if vertical else 'Horizontal'
      self.board.display_for_player()
      print(f'Placing {ship.name}')

      userInput = validate_int_input(prompt)
      match userInput:
        case 1:
          vertical = not vertical
          if not self.board.try_place_ship(ship,coords,vertical):
            print('Invalid placement!: ')
            vertical = True
        case 2: 
          coords = (10, 10)
          while not self.board.try_place_ship(ship,coords,vertical):
            coords = self.get_coords_from_user()
            print('Invalid placement!: ')
        case 3:
          if self.board.try_place_ship(ship, coords, vertical):
            successfully_placed = True

  def _place_ships_randomly(self):
    for ship in self.ships:
      successfully_placed = False
      while not successfully_placed:
        coords = self._rand_cell()
        vertical = self._rand_bool()
        successfully_placed = self.board.try_place_ship(ship, coords, vertical)

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
