#!/usr/bin/env python3

import os
import sys
from .dictionary import Dictionary

def main():
  if len(sys.argv) < 2 or len(sys.argv) > 3:
    print('Usage: diceware.py 9 [words.txt]', file=sys.stderr)
    sys.exit(1)

  if not sys.argv[1].isdigit():
    print('Word count must be an integer', file=sys.stderr)
    sys.exit(1)

  if len(sys.argv) == 3:
    filename = sys.argv[2]
  else:
    filename = os.path.join(
      os.path.dirname(os.path.abspath(__file__)), 
      'words.txt'
    )
  try:
    with open(filename) as f:
      dictionary = Dictionary(f)
  except FileNotFoundError:
    print('File "{}" was not found'.format(filename), file=sys.stderr)
    sys.exit(1)
  except OSError as ex:
    print('OS Error: {}'.format(ex), file=sys.stderr)
    sys.exit(1)

  words = dictionary.get_random_words(int(sys.argv[1]))
  print(' '.join(words))