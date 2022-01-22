from constant import EMPTY_CELL, HIT, MISS

class Cell:
  def __init__(self):
      self.contents = EMPTY_CELL

  def get(self, for_self):
    # return EMPTY_CELL
    if for_self: 
       return self.contents
    else: 
      return self.contents if self._is_hit_or_miss() else EMPTY_CELL

  def _is_hit_or_miss(self):
    return self.contents == HIT or self.contents == MISS
  
  def set_hit(self):
    self.contents = HIT
  
  def set_miss(self):
    self.contents = MISS

  def set_ship(self, part):
    self.contents = part
