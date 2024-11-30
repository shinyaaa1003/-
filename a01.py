import io
import sys

# input here
_INPUT = """\
"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)


def main():
    N = int(input())
    print(N**2)


if __name__ == "__main__":
    main()
