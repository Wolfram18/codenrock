import sys

def sieve(N):
    nums = [i for i in range(N+1)]
    nums[1] = 0
    i = 2
    while i <= N:
        if nums[i] != 0:
            for j in range(i+i, N+1, i):
                nums[j] = 0
        i += 1
    return [i for i in nums if i != 0]

if __name__ == '__main__':
    for line in sys.stdin:
        print(len(sieve(int(line))))
