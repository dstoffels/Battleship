from gameBoard import GameBoard
from ship import load_ships

class Player:
  def __init__(self) -> None:
      self.board = GameBoard()
      self.ships = load_ships()