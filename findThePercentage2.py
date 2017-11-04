if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_list = student_marks[query_name]
    average = (query_list[0] + query_list[1] + query_list[2]) / 3
    print("%.2f" % average)
