import sys


def problem_solved(contest_data, c, p):
    if contest_data.get(c) and contest_data[c].get(p):
        records = contest_data[c][p]
        for record in records:
            if record[1] == 'C':
                return True
    return False


def sum_results(contest_data):
    results = {}
    for contestant in contest_data.keys():
        contestant_nsolved = 0
        contestant_penalty = 0
        for problem in contest_data[contestant]:
            solved = False
            penalty = 0
            records = contest_data[contestant][problem]
            for record in records:
                if record[1] == 'C':
                    penalty += record[0]
                    solved = True
                    break
                elif record[1] == 'I':
                    penalty += 20
            if solved:
                contestant_nsolved += 1
                contestant_penalty += penalty
        results[contestant] = (contestant_nsolved,contestant_penalty)
    for element in sorted(results.items(),key= lambda kv:(kv[1][0], - kv[1][1],-kv[0]), reverse=True):
        print(element[0],element[1][0], element[1][1])


def main():
    test_cases = int(sys.stdin.readline()[:-1])
    _ = sys.stdin.readline()
    while(test_cases):
        contest_data = {}
        input_data = sys.stdin.readline()[:-1]
        while input_data != "":
            c, p, t, l = input_data.split()
            c = int(c)
            p = int(p)
            t = int(t)
            if contest_data.get(c):
                if not problem_solved(contest_data, c, p):
                    if contest_data[c].get(p):
                        contest_data[c][p].append((t,l))
                    else:
                        contest_data[c][p] = [(t, l)]
            else:
                contest_data[c] = {p: [(t, l)]}
            input_data = sys.stdin.readline()[:-1]
        sum_results(contest_data)
        test_cases -= 1
        if test_cases != 0:
            print()

main()