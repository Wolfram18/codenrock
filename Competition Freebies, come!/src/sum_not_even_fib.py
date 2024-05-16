import sys

def sum_not_even_fib(N):
    f1 = 1
    f2 = 1
    sum = 2
    for i in range(2, N):
        f1, f2 = f2, f1 + f2
        if (f2%2 == 1):
            sum += f2
    return sum

if __name__ == '__main__':
    for line in sys.stdin:
        print(sum_not_even_fib(int(line)))