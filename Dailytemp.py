l = [30, 40, 50, 60]
low = 0
hi = 1
t = 0
l1 = []
while low<hi:
    if l[low] < l[hi]:
        t = hi - low
        l1.append(t)
        
        low+=1
        if low != len(l)-1:
               hi = low + 1
        
        print("1")

    if l[low] > l[hi]:
        print(hi)

        if hi == len(l)-1:
            l1.append(0)
            low += 1
            if low != len(l)-1:
               hi = low + 1
        else:
            hi+=1
    
     

l1.append(0)
print(l1)

