import random,time

def linear_search(a,x):
    for i,v in enumerate(a):
        if v==x: return i
    return -1

def binary_search(a,x):
    l,r=0,len(a)-1
    while l<=r:
        m=(l+r)//2
        if a[m]==x: return m
        if a[m]<x: l=m+1
        else: r=m-1
    return -1

def bubble_sort(a):
    b=a[:]
    for i in range(len(b)):
        for j in range(0,len(b)-i-1):
            if b[j]>b[j+1]: b[j],b[j+1]=b[j+1],b[j]
    return b

def selection_sort(a):
    b=a[:]
    for i in range(len(b)):
        m=i
        for j in range(i+1,len(b)):
            if b[j]<b[m]: m=j
        b[i],b[m]=b[m],b[i]
    return b

def insertion_sort(a):
    b=a[:]
    for i in range(1,len(b)):
        k=b[i]; j=i-1
        while j>=0 and b[j]>k: b[j+1]=b[j]; j-=1
        b[j+1]=k
    return b

def quick_sort(a):
    if len(a)<=1: return a[:]
    p=a[len(a)//2]
    return quick_sort([x for x in a if x<p])+[x for x in a if x==p]+quick_sort([x for x in a if x>p])

def merge_sort(a):
    if len(a)<=1: return a[:]
    m=len(a)//2
    l=merge_sort(a[:m]); r=merge_sort(a[m:]); out=[]; i=j=0
    while i<len(l) and j<len(r):
        if l[i]<r[j]: out.append(l[i]); i+=1
        else: out.append(r[j]); j+=1
    return out+l[i:]+r[j:]

def bucket_sort(a):
    b=[[] for _ in range(101)]
    for x in a: b[x].append(x)
    return [v for x in b for v in x]

random.seed(0); d=[random.randint(0,99) for _ in range(20)]; s=sorted(d); t=d[5]
print('Linear',linear_search(d,t)); print('Binary',binary_search(s,t))
for f in [bubble_sort,selection_sort,insertion_sort,quick_sort,merge_sort,bucket_sort]:
    s=time.perf_counter(); f(d); print(f.__name__,time.perf_counter()-s)
