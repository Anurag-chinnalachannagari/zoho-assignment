from collections import OrderedDict
def addrootDisplay():
    a=input("Enter root role name:")
    print(a)
    d[a]=[]
#q2
def addsubrole():
    a=input("Enter sub role name:")
    b=input("Enter reporting to role name:")
    if b in d:
        d[b].append(a)
    else:
        d[b]=[a]
def help(d,r,a):
    if r in d:
        for i in d[r]:
            a.append(i)
        for i in d[r]:
            help(d,i,a)
def display(d):
    r=list(d.keys())[0]
    a=[r]
    help(d,r,a)
    print(a)
def deleterole(d):
    a=input("Enter the role to be deleted:")
    b=input("Enter the role to be transferred:")
    for i in d:
        if a in d[i]:
            d[i].remove(a)
            d[i].append(b)
    if a in d:
        if b in d:
            for j in d[a]:
                d[b].append(j)
        else:
            d[b]=d[a]
        d.pop(a)
d=OrderedDict()
