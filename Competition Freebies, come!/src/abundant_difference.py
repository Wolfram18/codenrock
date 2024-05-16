import sys
import math

def selection_sort(numbers):
   for step in range(len(numbers)-1):
       for i in range(step, len(numbers)-1):
           if numbers[step] > numbers[i+1]:           
               numbers[step], numbers[i+1] = numbers[i+1], numbers[step]
   return numbers

def trial_div(N): # except 1,N
    divisors = set()
    for i in range(2, int(math.sqrt(N))+1):
        if N%i == 0:
            divisors.add(i)
            divisors.add(N//i)
    print(divisors)
    return divisors

def abundant_difference(numbers):
    sort_num = selection_sort(numbers)
    max_diff = abs(sort_num[len(sort_num)-1] - sort_num[0])
    sum_div = sum(trial_div(max_diff))
    if sum_div > max_diff:
        print("True")
    else:
        print("False")

def main():
    for line in sys.stdin:
        numbers = [int(item) for item in line.split()]
        abundant_difference(numbers)
 
if __name__ == "__main__":
    main()