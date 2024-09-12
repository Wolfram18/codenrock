def get_system_mass(array):
    return sum(int(i[2]) for i in array)

def get_balanced_coordinate(m, array, idx):
    return sum(int(i[idx])*int(i[2]) for i in array)/m

def main():
    number = int(input())
    satellites = []
    for _ in range(number): 
        satellites.append(input().split())
    m = get_system_mass(satellites)
    x = get_balanced_coordinate(m, satellites, 0)
    y = get_balanced_coordinate(m, satellites, 1)
    print(f"{x:.2f} {y:.2f}")
 
if __name__ == "__main__":
    main()
