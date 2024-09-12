def get_landing_time(h,m):
    h = (h + 1 + (m + 48) // 60) % 24
    m = (m + 48) % 60
    return h, m

def main():
    h, m = input().split()
    h, m = get_landing_time(int(h),int(m))
    print(h, m)

if __name__ == "__main__":
    main()
