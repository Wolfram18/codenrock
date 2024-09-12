import math

def get_daytime(phase):
    if phase == 1:
        return 14.75
    elif phase == 2:
        return 0 # ambiguously
    elif phase == 3 or phase == 4:
        return 7.375

def main():
    S = int(input())
    V = int(input())
    phase = int(input())
    phase = get_daytime(phase)
    count = S/V + S/V//phase*phase 
    print(f"Луноход-1 проедет {S:.1f} км за {math.ceil(count)} дней")
 
if __name__ == "__main__":
    main()
