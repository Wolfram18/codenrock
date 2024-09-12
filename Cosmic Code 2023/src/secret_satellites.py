def selection_sort(array, M_or_V):
    for step in range(len(array)-1):
        for i in range(step, len(array)-1):
            if array[step][M_or_V] > array[i+1][M_or_V]:           
                array[step], array[i+1] = array[i+1], array[step]
    return array

def get_max_count(satellites, max_M, max_V, M_or_V):
    satellites = selection_sort(satellites, M_or_V)
    current_M, current_V, count = 0, 0, 0
    while (current_M < max_M and current_V < max_V and count < len(satellites)):
        current_M += satellites[count][0]
        current_V += satellites[count][1]
        count += 1
    return count - 1

def main():
    max_M, max_V = input().split()
    number = int(input())
    satellites = []
    for n in range(number):
        satellites.append(input().split())
    satellites = [[int(item[0]),int(item[1])] for item in satellites] 
    count_M = get_max_count(satellites, int(max_M), int(max_V), 0)
    count_V = get_max_count(satellites, int(max_M), int(max_V), 1)
    print(max(count_M, count_V))

if __name__ == "__main__":
    main()
