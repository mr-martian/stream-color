#!/usr/bin/python3

import sys

# states
BLANK, BLOCK, DELIM, DELIM_END, LEMH, LEMQ, POS, TAGS = range(8)

colors = {
  BLANK: '\033[0m\033[2m',
  BLOCK: '\033[0m\033[2m',
  DELIM: '\033[0m\033[32m',
  DELIM_END: '\033[0m\033[32m',
  LEMH: '\033[0m\033[1m',
  LEMQ: '\033[0m\033[1m',
  POS: '\033[0m\033[34m',
  TAGS: '\033[0m\033[35m',
  'end': '\033[0m'
}

transitions = {
  BLANK: {
    '[': BLOCK,
    '^': DELIM,
    None: BLANK
  },
  BLOCK: {
    ']': BLANK,
    None: BLOCK
  },
  DELIM: {
    None: LEMH
  },
  DELIM_END: {
    '^': DELIM,
    None: BLANK
  },
  LEMH: {
    '<': POS,
    '/': DELIM,
    '$': DELIM_END,
    None: LEMH
  },
  LEMQ: {
    '$': DELIM_END,
    None: LEMQ
  },
  POS: {
    '<': TAGS,
    '/': DELIM,
    '$': DELIM_END,
    '#': LEMQ,
    None: POS
  },
  TAGS: {
    '/': DELIM,
    '$': DELIM_END,
    '#': LEMQ,
    None: TAGS
  }
}

state = BLANK
print(colors[BLANK], end='')
cur = sys.stdin.read(1)
while cur:
    if cur == '\\':
        cur += sys.stdin.read(1)
    new_state = state
    if cur in transitions[state]:
        new_state = transitions[state][cur]
    else:
        new_state = transitions[state][None]
    if new_state != state:
        print(colors[new_state], end='')
        state = new_state
    print(cur, end='')
    cur = sys.stdin.read(1)
print(colors['end'])

