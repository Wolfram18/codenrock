def get_length_of_LIS(array, number):
    din, pos = [0]*number, [0]*number
    for i in range(number):
        din[i] = 1
        pos[i] = -1
        for j in range(i):
            if array[i] > array[j]:
                if 1 + din[j] > din[i]:
                    din[i] = 1 + din[j]
                    pos[i] = j
    return din, pos

def position_of_LIS(din, pos, number):
    correct = set()
    max_len, idx_max_len = din[0], 0
    for i in range(number):
        if din[i] > max_len:
            max_len = din[i]
            idx_max_len = i
    correct.add(idx_max_len)
    for i in range(max_len - 1):
        correct.add(pos[idx_max_len])
        idx_max_len = pos[idx_max_len]
    return correct

def main():
    number = int(input())
    data = []
    for _ in range(number):
        data.append(input().split())
    data = [[int(item[0]),int(item[1])] for item in data]
    a, b = list(zip(*data))
    din_a, pos_a = get_length_of_LIS(a, number)
    correct_a = position_of_LIS(din_a, pos_a, number)
    din_b, pos_b = get_length_of_LIS(b, number)
    correct_b = position_of_LIS(din_b, pos_b, number)
    print(number - len(correct_a & correct_b))

if __name__ == "__main__":
    main()