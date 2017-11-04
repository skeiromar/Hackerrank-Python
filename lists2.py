if __name__ == '__main__':
    N = int(input())
    list = []
    for i in range(N):
        x = input()
        if "insert" in x and x[-2] == " ":
            list.insert(int(x[-3]), int(x[-1]))
        elif "insert" in x and x[-2] != " ":
            list.insert(int(x[-4]), int(x[-2:]))
        elif "print" in x:
            print(list)
        elif "remove" in x:
            list.remove(int(x[-1]))
        elif "append" in x and x[-2] == " ":
            list.append(int(x[-1]))
        elif "append" in x and x[-2] != " ":
            list.append(int(x[-2:]))
        elif "sort" in x:
            list.sort()
        elif "pop" in x:
            list.pop()
        elif "reverse" in x:
            list.reverse()

