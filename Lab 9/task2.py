def heapify(a,n,i,rev=False):
    l,r=2*i+1,2*i+2; s=i
    if l<n and (a[l]>a[s] if not rev else a[l]<a[s]): s=l
    if r<n and (a[r]>a[s] if not rev else a[r]<a[s]): s=r
    if s!=i: a[i],a[s]=a[s],a[i]; heapify(a,n,s,rev)

def heap_sort(a,rev=False):
    b=a[:]; n=len(b)
    for i in range(n//2-1,-1,-1): heapify(b,n,i,rev)
    for i in range(n-1,0,-1):
        b[0],b[i]=b[i],b[0]; heapify(b,i,0,rev)
    return b

arr=[12,11,13,5,6,7]
print(heap_sort(arr))
print(heap_sort(arr,True))
