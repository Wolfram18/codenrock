import sys

def print_tree(N):
    for i in range(1,N+1):
        print(*['*' for x in range(i)], sep='')

if __name__ == '__main__':
    for line in sys.stdin:
        print_tree(int(line))