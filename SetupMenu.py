# from player import Player

# from helpers import validate_int_input
# from constant import SET_BOARD_MENU

# class SetupMenu:
#   def __init__(self, player: Player):
#     self.player = player
#     self.run()

#   def run(self):
#     # FIXME: refactor for new layout
#     self.player.game_board.display_for_self()
#     while True:
#       userInput = validate_int_input(SET_BOARD_MENU)

#       match userInput:
#         case 1: self._place_ships_manually()
#         case 3: pass # move ship (select ship menu)
#         case 4: pass # clear board (need method)
#         case 5: return True
#         case 6: return False

#   def _place_ships_manually(self):
#     for ship in self.ships:
#       self._run_manual_menu(ship)
