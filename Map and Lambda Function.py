cube = lambda x:x**3  # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if(n==0):
        return []
    elif(n==1):
        return [0]
    else:
        list = [0,1]
        for i in range(2,n):
            list.append(list[i-1] + list[i-2])
        #print(list)
        return list
 

    
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
