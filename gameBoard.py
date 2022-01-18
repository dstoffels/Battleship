import string
from cell import Cell
from helpers import clear_console, index_uppercase

from ship import Ship
from constant import GRID, EMPTY_CELL

# specialized dictionary with coordinate tuple keys and cell object values
class GameBoard(dict[(int,int), Cell]):
  def __init__(self):
    super().__init__(self)
    self.build_cells()
    self.ships: list[Ship] = []

  def build_cells(self):
    for row in range(GRID + 1):
      for col in range(GRID + 1):
        self[(row, col)] = Cell()

  def display(self, for_self):
    for row in range(0,GRID + 1):
      line = ''
      for col in range(0,GRID + 1):
        line += self._build_header_row(row,col)
        line += self._build_header_col(row,col)
        line += self._get_cell((row, col), for_self)
      print(line)

  def _get_cell(self, coords, for_self):
    row, col = coords
    if row and col: return f' {self[(row,col)].get(for_self)}'
    return ''
  
  def _build_header_row(self, row, col):
    if not row and not col: return '  '
    if not row: return f' {col} ' if col < 10 else f'{col} '
    return ''

  def _build_header_col(self, row, col):
    if not col and row: return index_uppercase(row)
    return ''


########### OLD STUFF #############  

  def try_place_ship(self, new_ship: Ship, coords, vertical):
    new_ship.remove()
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
      if ship != new_ship: 
        if ship.compare_coords(new_ship):
          self._remove_ship(new_ship)
          return False
    return True

  def _place_ship(self, new_ship: Ship, coords, vertical):
    new_ship.place(coords, vertical)
    self.ships.append(new_ship)

  def _remove_ship(self, ship: Ship):
    self.ships.remove(ship)
    ship.remove()


gb = GameBoard()

gb[1,1].set_miss()
gb[10,7].set_miss()
gb[4,4].set_hit()
gb[1,1].set_hit()
gb[1,2].set_miss()

gb.display(True)