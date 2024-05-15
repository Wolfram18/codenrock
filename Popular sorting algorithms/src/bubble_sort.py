import sys
import re

def swap(a, b): # a = x, b = y
   a = a + b    # x + y
   b = a - b    # x + y - y = x
   a = a - b    # x + y - x = y
   return a, b

def bubble_sort(numbers):
   for step in range(len(numbers)-1):
       for i in range(len(numbers)-1-step):
           if numbers[i] > numbers[i+1]:
                numbers[i], numbers[i+1] = swap(numbers[i], numbers[i+1])
   return numbers

def main():
    for line in sys.stdin: # get input strings one by one
        sequences = re.findall(r'\b\d+\b', line) # returns sequences of numbers
        numbers = [int(item) for item in sequences] # to integer
        numbers = bubble_sort(numbers)
        print(','.join(map(str, numbers))) # to string
 
if __name__ == "__main__":
    main()
