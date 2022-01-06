from constant import BOW, EMPTY_CELL, HULL, SHIP_HORZ, SHIP_VERT, STERN


class Ship:
  def __init__(self, name, length) -> None:
    self.name = name
    self.length = length
    self.coords = {} # key: coordinates tuple (1,4), value: what to display in cell ^, v, <, >, =, ‖
  
  def place_ship(self, coords, vertical=False): #bow of ship placed at coords
    row = coords[0]
    col = coords[1]
    ship = SHIP_VERT if vertical else SHIP_HORZ

    i = 0
    while i < self.length:
      if i == 0: self.coords.update({(row, col): ship[BOW]})
      elif i == self.length - 1: self.coords.update({(row, col): ship[STERN]})
      else: self.coords.update({(row, col): ship[HULL]})

      if vertical: row += 1
      else: col += 1
      i += 1
  
  def get_ship_coords(self, cell):
    for key, val in self.coords.items():
      if key == cell: return val
    return EMPTY_CELL