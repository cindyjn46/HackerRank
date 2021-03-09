if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l=[]
    #cl = []
    for iz in range(0,z+1):
        #cl.append(iz)
        l.append([0,0,iz])
        
    for iy in range(1,y+1):
        for iz in range(0,z+1):
            #cl.append(iz)
            l.append([0,iy,iz])
    
    for ix in range(1,x+1):
        for iy in range(0,y+1):
            for iz in range(0,z+1):
                l.append([ix,iy,iz])
    
    result=[]
    for lst in l:
        if(sum(lst)!=n):
            result.append(lst)
    print(result)    
        
        
