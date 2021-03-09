if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    runner_up = sorted(list(set([x for x in arr])))[-2]
    print(runner_up)
    #print(sorted(list(set([x for x in arr]))))
    #sorted(list(set([x[1] for x in student])))[1]
