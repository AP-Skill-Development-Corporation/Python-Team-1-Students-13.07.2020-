# Even or Odd Fun
def Even(num):
    if num % 2 == 0:
        return "Even"
    return "Odd"


def Leapyears(l,u):
    for year in range(l,u+1):
        if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
            print(year,end = " ")
        else:
            pass
        

def unique(l):
    li = []
    for i in l:
        if l.count(i) == 1:
            li.append(i)
    print(li)
    
def uniqueData(l):
    li = []
    for i in l:
        if i not in li:
            li.append(i)
    return li
