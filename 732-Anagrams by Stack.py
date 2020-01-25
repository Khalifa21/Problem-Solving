import sys


def exist_with_order(to_stack, target):
    to_stack = to_stack [::-1]
    i = 0
    for ch in target:
        if ch == to_stack[i]:
            i += 1
            if i ==len(to_stack):
                return True
    return False


def print_output(output):
    output = sorted(output)
    for ans in output:
        for i, a in enumerate(ans):
            if i == 0:
                print("{}".format(a), end='')
            else:
                print(" {}".format(a), end='')
        print()


def solve(stack, source, target, ans, output):
    if target == "":
        output.append(''.join(ans))
        return
    ch = target[0]
    if len(stack) and stack[-1] == ch:
        new_ans = ans[:]
        new_ans.extend('o')
        solve(stack[:-1], source, target[1:],new_ans, output)

    locations = [i for i, ltr in enumerate(source) if ltr == ch]
    for loc in locations:
        if loc == 0:
            new_ans = ans[:]
            new_ans.extend(['i', 'o'])
            solve(stack, source[loc+1:], target[1:], new_ans, output)
        else:
            to_stack = source[:loc]
            new_stack = stack[:]
            new_stack.extend(to_stack)
            if exist_with_order(new_stack, target):
                to_ans = ['i' for i in range(len(to_stack)+1)]
                to_ans.extend('o')
                new_ans = ans[:]
                new_ans.extend(to_ans)
                solve(new_stack,source[loc+1:], target[1:], new_ans, output)


def main():
    source = sys.stdin.readline()[:-1]
    while source != "":
        target = sys.stdin.readline()[:-1]
        stack = []
        ans = []
        print("[")
        output = []
        solve(stack, source, target, ans, output)
        print_output(output)
        print("]")
        source = sys.stdin.readline()[:-1]

main()
