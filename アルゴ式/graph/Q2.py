"""

"""

import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
6 7
0 1
0 5
1 3
1 5
2 3
3 4
4 5

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import deque
def main():
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
