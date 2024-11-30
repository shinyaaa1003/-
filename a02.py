import io
import sys

# input here
_INPUT = """\
5 40
10 20 30 40 50

"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)


def main():
    N, X = map(int, input().split())
    A = list(map(int, input().split()))
    answer = False
    for i in range(N):
        if A[i] == X:
            answer = True

    if answer:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
