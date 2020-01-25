import sys
n = int(sys.stdin.readline()[:-1])
while n != 0:
    score_dict = {}
    for i in range(n):
        courses = sys.stdin.readline()[:-1].split()
        courses.sort()
        courses = ''.join(courses)
        if score_dict.get(courses):
            score_dict[courses] +=1
        else:
            score_dict[courses] = 1
    values = list(score_dict.values())
    most_popular = max(values)
    count = values.count(most_popular)
    print(count*most_popular)
    n = int(sys.stdin.readline()[:-1])