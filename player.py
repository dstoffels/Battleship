import coords
from gameBoard import GameBoard
from ships import Ships

class Player:
  def __init__(self, player_num):
    self.name = ''
    self.game_board = GameBoard()
    self.ships = Ships.init_ships()
    self.opponent: Player = None
    self.player_num = player_num

  def setup(self, opponent):
    self.opponent = opponent
    self._set_name()
    self._setup_game_board()

  def take_turn(self):
    target_coords = self.select_target()
    self._check_target(target_coords)

  def _set_name(self): pass

  def _setup_game_board(self): pass

  def select_target(self): pass

  def _check_target(self, target_coords):
    opp_board = self.opponent.game_board
    for ship, ship_coords in opp_board.ships.items():
      for i in range(len(ship_coords)):
        if target_coords == ship_coords[i]:
          ship.set_hit(i)
          return
    opp_board[target_coords].set_miss()

  def place_ships_randomly(self):
    self.game_board.clear_ships()

    for ship in self.ships:
      successfully_placed = False
      while not successfully_placed:
        bow_coords = coords.random_coords()
        ship.random_orientation()
        successfully_placed = self.game_board.ships.try_place_ship(ship, bow_coords)

  def is_defeated(self):
    for ship in self.ships:
      if not ship.is_destroyed():
        return False
    return True

  