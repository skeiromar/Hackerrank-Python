
if __name__ == '__main__':
    n = int(input())
    if n % 2 == 1:
        print("Weird")
    if n % 2 == 0 and 2 <= n <= 5:
        print("Not Weird")
    if n % 2 == 0 and 6 <= n <= 20:
        print("Weird")
    if n % 2 == 0 and 20 < n:
        print("Not Weird")
