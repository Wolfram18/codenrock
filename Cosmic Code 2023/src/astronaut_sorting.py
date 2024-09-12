def insertion_sort(array):
    for step in range(1, len(array)):
        current = step
        for i in range(step-1, -1, -1):
            if int(array[current][2]) > int(array[i][2]):
                array[current], array[i] = array[i], array[current]
                current = i
    return array

def main():
    number = int(input())
    cosmonauts = []
    for n in range(number): 
        cosmonauts.append(input().split())
    insertion_sort(cosmonauts)
    cosmonauts = [' '.join(item) for item in cosmonauts]
    for cosmonaut in cosmonauts: 
        print(cosmonaut)
 
if __name__ == "__main__":
    main()
