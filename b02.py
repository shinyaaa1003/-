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
    A, B = map(int, input().split())
    answer = False
    for i in range(A, B + 1):
        if 100 % i == 0:
            answer = True
            break
    if answer:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
