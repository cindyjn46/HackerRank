if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for name,score in student_marks.items():
        if(name==query_name):
            total = sum(score)
    #print(avg)
    print('%.2f' %(total/3))
    #2
    #Harsh 25 26.5 28
    #Anurag 26 28 30
    #Harsh
