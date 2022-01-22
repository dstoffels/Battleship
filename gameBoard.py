from cell import Cell
from ship import Ship
from ships import Ships

from constant import GRID
from helpers import index_uppercase

# specialized dictionary with coordinate tuple keys and cell object values
class GameBoard(dict[(int,int), Cell]):
  def __init__(self):
    super().__init__(self)
    self.build_cells()
    self.ships = Ships()

  def build_cells(self):
    for row in range(GRID + 1):
      for col in range(GRID + 1):
        self[(row, col)] = Cell()

  def display(self, for_self):
    self.populate_ships_in_cells()
    for row in range(0,GRID + 1):
      line = ''
      for col in range(0,GRID + 1):
        line += self._build_header_row(row,col)
        line += self._build_header_col(row,col)
        line += self._get_cell(row, col, for_self)
      print(line)

  def _get_cell(self, row, col, for_self):
    if row and col: return f' {self[(row,col)].get(for_self)}'
    return ''
  
  def _build_header_row(self, row, col):
    if not row and not col: return '  '
    if not row: return f' {col} ' if col < 10 else f'{col} '
    return ''

  def _build_header_col(self, row, col):
    return index_uppercase(row) if not col and row else ''
  
  def populate_ships_in_cells(self):
    for ship, coords in self.ships.items():
      for i in range(len(coords)):
        self[coords[i]].set_ship(ship.sections[i])


ship = Ship('Destroyer', 4)
ship2 = Ship('Cruiser', 3)
gb = GameBoard()

gb.ships.try_place_ship(ship, (10,1))
gb.ships.try_place_ship(ship2, (9,1))

gb.ships.check_for_hit((10,1))

gb.display(True)