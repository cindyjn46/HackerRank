import numpy as np
n = int(input())

array = []
for i in range(0,n):
    array.append(list(map(float,input().split(" "))))
    #np.append()

a = np.array(array)
print(round(np.linalg.det(a),2))
