import io
import sys

# input here
_INPUT = """\
77 23

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)


def main():
    A, B = map(int, input().split())
    print(A + B)


if __name__ == "__main__":
    main()
