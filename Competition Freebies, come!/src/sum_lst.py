import sys

def get_unique_numbers(numbers):
    unique = [x for x in numbers if numbers.count(x) == 1]
    return sum(unique)

def main():
    for line in sys.stdin:
        numbers = [int(item) for item in line.split()]
        print(get_unique_numbers(numbers[1:len(numbers)-1]))
 
if __name__ == "__main__":
    main()