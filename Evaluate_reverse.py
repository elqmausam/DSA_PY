l = list(input().split( ))
low = 0
hi = low + 1
t = 0

while low<hi:
    if (int(l[low]) >= 0 or int(l[low]) < 0) and (int(l[hi]) >= 0 or int(l[hi]) < 0) :
        if l[hi+1] == "+":
            t = int(l[low])+int(l[hi])
            l[low] = t
            l.remove(l[hi+1])
            l.remove(l[hi])
            
            low = 0
            hi = low + 1
        elif l[hi+1] == "-":
            t = int(l[low])-int(l[hi])
            l[low] = t
            l.remove(l[hi+1])
            l.remove(l[hi])
            
            low = 0
            hi = low + 1
        elif l[hi+1] == "/":
            t = int(l[low])/int(l[hi])
            l[low] = t
            l.remove(l[hi+1])
            l.remove(l[hi])
            
            low = 0
            hi = low + 1
        elif l[hi+1] == "*":
            t = int(l[low])*int(l[hi])
            l[low] = t
            l.remove(l[hi+1])
            l.remove(l[hi])
            
            low = 0
            hi = low + 1

        else:
            low+=1
            hi+=1
        
    
        
    
    if len(l) == 1:
        break

print(int(t))