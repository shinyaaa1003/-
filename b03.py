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
    A = list(map(int, input().split()))
    answer = False
    for i in range(N):
        for j in range(i + 1, N):
            for k in range(j + 1, N):
                if A[i] + A[j] + A[k] == 1000:
                    answer = True
    if answer:
        print("Yes")
    else:
        print("No")


if __name__ == "__main__":
    main()
