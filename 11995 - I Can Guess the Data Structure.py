import sys

def check_stack(bag, x):
    output = False
    if len(bag) and x == bag[-1]:
        output = True
        del bag[-1]
    return output

def check_queue(bag, x):
    output = False
    if len(bag) and x == bag[0]:
        output = True
        del bag[0]
    return output

def check_pqueue(bag, x):
    output = False
    if len(bag) and x == max(bag):
        output = True
        bag.remove(x)
    return output
    
def main():
    
    num_commands = sys.stdin.readline()[:-1]
    while num_commands != "":
        stack = []
        queue = []
        pqueue = []
        q, s, pq = 1, 1, 1
        for _ in range(int(num_commands)):
            command, x =sys.stdin.readline()[:-1].split()
            if command == '1':
                stack.append(int(x))
                queue.append(int(x))
                pqueue.append(int(x))
            else:
                update_q, update_s, update_pq = check_queue(queue,int(x)), check_stack(stack,int(x)), check_pqueue(pqueue,int(x))
                q, s, pq = q & update_q, s & update_s, pq & update_pq     
        if q | s | pq == 0:
            print("impossible")
        elif q + s + pq > 1:
            print("not sure")
        elif q == 1:
            print("queue")
        elif s == 1:
            print("stack")
        else:
            print("priority queue")

        num_commands = sys.stdin.readline()[:-1]
main()