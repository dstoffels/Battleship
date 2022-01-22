from constant import GRID
from ship import Ship

class Ships(dict[Ship, list[tuple[int,int]]]):

  def check_for_hit(self, target_coords):
    for ship, coords in self.items():
      for i in range(len(coords)):
        if coords[i] == target_coords:
          ship.set_hit(i)

  def try_place_ship(self, ship: Ship, coords):
    return self._ship_within_grid(ship, coords) and self._ships_not_overlapping(ship, coords)

  def _ship_within_grid(self, ship: Ship, coords):
    end_row = coords[0] + ship.length - 1
    end_col = coords[1] + ship.length - 1

    if ship.is_vertical: return end_row <= GRID
    else: return end_col <= GRID
  
  def _ships_not_overlapping(self, new_ship: Ship, bow_coords):
    self._place_ship(new_ship, bow_coords)

    for ship, coords in self.items():
      if ship != new_ship:
        if not self._coords_are_unique(self[new_ship], coords):
          self.pop(new_ship)
          return False
    return True

  def _place_ship(self, ship: Ship, bow_coords):
    ship_coords = [bow_coords]
    row = bow_coords[0]
    col = bow_coords[1]

    for i in range(ship.length):
      if i != 0: ship_coords.append((row,col))
      if ship.is_vertical: row += 1
      else: col += 1

    self[ship] = ship_coords

  def _coords_are_unique(self, new_coords, coords):
    for new_coord in new_coords:
      for coord in coords:
        if new_coord == coord: return False
    return True