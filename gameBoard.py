import string
from helpers import clear_console

from ship import Ship
from constant import GRID, EMPTY_CELL

class GameBoard:
  def __init__(self):
    self.hits = []
    self.misses = []   
    self.ships: list[Ship] = []

  def display_for_opponent(self):
    self._build_grid(False)

  def display_for_player(self):
    clear_console()
    self._build_grid(True)

  def _build_grid(self, for_player):
    row = 0
    col = 0

    line = ''
    while row <= GRID:
      while col <= GRID:
        if row == 0 and col == 0: line += '  '
        elif row == 0: 
          if col < 10: line += f' {col} '
          else: line += f' {col}'
        elif col == 0: line += f' {string.ascii_uppercase[row - 1]}'
        else: line += f' {self.build_cell((row, col), for_player)}'
        col += 1
      row += 1
      col = 0
      print(line)
      line = ''

  def build_cell(self, cell, for_player):
    for hit in self.hits:
      if cell == hit: return ' X'
    if for_player:
      for ship in self.ships:
        new_cell = ship.get_coords(cell)
        if new_cell != EMPTY_CELL: return new_cell 
    for miss in self.misses:
      if cell == miss: return ' -'
    return EMPTY_CELL

  def try_place_ship(self, new_ship: Ship, coords, vertical):
    if self._ship_within_grid(new_ship, coords, vertical) and self._ship_not_overlapping(new_ship,coords,vertical):
      return True
    else:
      return False

  def _ship_within_grid(self, new_ship: Ship, coords, vertical):
    end_row = coords[0] + new_ship.length - 1
    end_col = coords[1] + new_ship.length - 1

    if vertical:
      if end_row > GRID: return False
    else:
      if end_col > GRID: return False
    return True
  
  def _ship_not_overlapping(self, new_ship: Ship, coords, vertical):
    self._place_ship(new_ship,coords,vertical)

    for ship in self.ships:
      if ship == new_ship: 
        continue
      elif ship.compare_coords(new_ship):
        self._remove_ship(new_ship)
        return False
    return True

  def _place_ship(self, new_ship, coords, vertical):
    new_ship.place(coords, vertical)
    self.ships.append(new_ship)

  def _remove_ship(self, ship: Ship):
    self.ships.remove(ship)
    ship.remove()
  
  def _convert_coords(self, input_coords):
    letter: str = input_coords[0]
    row = string.ascii_lowercase.index(letter)
    row = int(row) + 1
    col = int(input_coords[1])
    return (row, col)