GRID = 10
EMPTY_CELL = '⬜'
MISS = ' -'
HIT = ' X'

SHIP_NAMES = {
  'Destroyer': 2,
  'Submarine': 3,
  'Cruiser': 3,
  'Battleship': 4,
  'Carrier': 5
}

BOW = 'Bow'
HULL = 'Hull'
STERN = 'Stern'

SHIP_VERT = {
  BOW: ' ∧',
  HULL: ' ▓',
  STERN: ' V'
}

SHIP_HORZ = {
  BOW: ' <',
  HULL: ' ═',
  STERN: ' >'
}

MAIN_MENU_PROMPT = '''1) Solo Game
2) Hotseat Game (two players)
3) Quit

Choose an option: '''

SET_BOARD_MENU = '''
1) Place ships manually
2) Place ships randomly
3) Move a ship
4) Clear ships from the board
5) TO BATTLE!
6) Return to main menu

Choose an option: '''

MANUAL_PLACE_MENU = '''1) Select coordinates
2) Flip Orientation
3) Confirm placement
'''

AI_NAMES = [
  "Cap'm Jack Sparrah",
  "Admiral Ackbar",
  "The East India Trading Co.",
  "Bob",
  "James Bugress",
  "Ariana Grande"
]