from constant import BOW, HIT, HULL, SHIP_HORZ, SHIP_VERT, STERN

class Ship:
  def __init__(self, name, length) -> None:
    self.name = name
    self.length = length
    self.is_vertical = False
    self.sections = [None] * self.length
    self._set_sections()

  def set_hit(self, positional_index):
    self.sections[positional_index] = HIT
    if self.is_destroyed(): print('Hit and sunk!')
    else: print('Hit!')

  def flip_orientation(self):
    self.is_vertical = not self.is_vertical
    self._set_sections()

  def is_destroyed(self):
    for section in self.sections:
      if section != HIT: return False
    return True

  def _set_sections(self):
    for i in range(self.length):
      if i == 0: 
        self.sections[i] = SHIP_VERT[BOW] if self.is_vertical else SHIP_HORZ[BOW]
      elif i == self.length - 1: 
        self.sections[i] = SHIP_VERT[STERN] if self.is_vertical else SHIP_HORZ[STERN]
      else: 
        self.sections[i] = SHIP_VERT[HULL] if self.is_vertical else SHIP_HORZ[HULL]
  
  def __str__(self): return self.name