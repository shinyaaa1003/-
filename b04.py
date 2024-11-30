import io
import sys

# input here
_INPUT = """\
1101
"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)


def baseNtobase10(target: str, N) -> int:
    '''N進数を10進数に変換
    args:
        target (str) : N進数表記の文字列
        N (int) : 元の進数
    return:
        int : 10進数表記の値
    '''
    base10 = 0
    for i in range(1, len(target) + 1):
        base10 += N**(i - 1) * int(target[-i])
    return base10


def main():
    N = input()
    answer = baseNtobase10(N, 2)
    print(answer)


if __name__ == "__main__":
    main()
