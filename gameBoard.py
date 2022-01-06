import string

from ship import Ship
from constant import GRID, EMPTY_CELL

class GameBoard:
  def __init__(self):
    self.cells = {}
    self.hits = []
    self.misses = []   
    self.ships: list[Ship] = [Ship('Destroyer', 4)]

    self.ships[0].place_ship((1,1), True)
    self.display_for_player()

  def display_for_opponent(self):
    self._build_grid(self.build_cell, False)

  def display_for_player(self):
    self._build_grid(self.build_cell, True)

  def _build_grid(self, build_cell, for_player):
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
        else: line += f' {build_cell((row, col), for_player)}'
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
        return ship.get_ship_coords(cell)
    for miss in self.misses:
      if cell == miss: return ' -'
    return EMPTY_CELL

  def validate_ship_placement(self, ship: Ship):
    pass
    




    # r = 0
    # c = 0
    # while r < GRID:
    #   row = string.ascii_lowercase[r]
    #   while c < GRID:
    #     col = c + 1
    #     c += 1
    #     self.cells.update({str(row)+str(col): (r+1,c)})
    #   c = 0
    #   r += 1