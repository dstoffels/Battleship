import random
import string

from constant import GRID
from helpers import validate_int_input

def get_from_user():
  row = _get_row_from_user()
  col = _get_col_from_user()
  return (row, col)

def random_coords():
  row = random.randint(1, GRID)
  col = random.randint(1, GRID)
  return (row, col)

def _get_row_from_user():
  max_alpha_i = string.ascii_uppercase[GRID -1]
  prompt = f'Select a row (A-{max_alpha_i}): '

  row = ''
  while not _valid_row(row):
    row = input(prompt).lower()
  row = string.ascii_lowercase.index(row) + 1
  return row

def _get_col_from_user():
  col = 0
  while not _valid_col(col):
    col = validate_int_input(f'Select a column (1-{GRID}): ')
  return col

def _valid_row(row: str):
  if not row.isalpha(): return False
  i = string.ascii_lowercase.index(row)
  return i < GRID and not i < 0

def _valid_col(col: int):
  return col <= GRID and not col < 1