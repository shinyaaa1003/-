import io
import sys

# input here
_INPUT = """\
13
"""
sys.stdin = io.StringIO(_INPUT)

# code
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
import sys
sys.setrecursionlimit(10**9)


def base10tobaseN(target, N) -> str:
    '''N進数表記に変換,
    args:
        target (int) : 変換したい10進数の値
        N (int) : 変換後の進数
    return:
        str : N進数表記の文字列
    '''
    tmp = ''
    while target >= N:
        tmp = str(target % N) + tmp
        target //= N
    tmp = str(target) + tmp
    return tmp


def main():
    N = int(input())
    answer = base10tobaseN(N, 2).zfill(10)
    print(answer)


if __name__ == "__main__":
    main()
