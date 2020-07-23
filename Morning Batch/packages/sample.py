# even or odd
def evenorodd(n):
    if n%2==0:
        print("True")
    else:
        print("False")
        
        
        
#unique elements
def unique(li):
    li1=[] 
    for i in li:
        if li.count(i)==1:
            li1.append(i)
    print(li1)