import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    N, K = map(int, input().split())
    li = []
    for i in range(1, N+1):
        for j in range(1, K+1):
            li.append(int(str(i) + '0' + str(j)))
    print(sum(li))
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
