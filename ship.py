from constant import BOW, EMPTY_CELL, HULL, SHIP_HORZ, SHIP_NAMES, SHIP_VERT, STERN


#FULL REFACTOR: move most logic to GameBoard
class Ship:
  def __init__(self, name, length) -> None:
    self.name = name
    self.length = length
    self.coords = {} # key: coordinates tuple (1,4), value: what to display in cell ^, v, <, >, =, ‖
    #FIXME: remove coords, ship does not need to know where it is, only gameboard
  
  def place(self, coords, vertical=False): #bow of ship placed at coords
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

  def remove(self):
    self.coords.clear()

  def compare_coords(self, new_ship):
    for coords in self.coords:
      for new_coords in new_ship.coords:
        if coords == new_coords: return True
    return False
  
  def get_coords(self, cell):
    for key, val in self.coords.items():
      if key == cell: return val
    return EMPTY_CELL

def init_ships():
  ships = []
  for name, length in SHIP_NAMES.items():
    ship = Ship(name, length)
    ships.append(ship)
  return ships