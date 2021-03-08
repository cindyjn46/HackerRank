if __name__ == '__main__':
    student = []
    for _ in range(int(input())):
        ns = []
        name = input()
        score = float(input())
        ns.extend([name,score])
        student.append(ns)
    
    #print(student)
    student.sort(key = lambda x: x[0])
    student.sort(key = lambda x: x[1])
    
    # for idx in student
    # print(student[1][0])
    # if((student[0][1]<student[1][1]) and (student[1][1] == student[2][1])):
    #     print(student[1][0])
    #     print(student[2][0])
    # else:
    #     print(student[1][0])
    second_score = sorted(list(set([x[1] for x in student])))[1]

    desired_students = []
    for s in student:
        if(s[1]==second_score):
            desired_students.append(s[0])

    print('\n'.join(desired_students))