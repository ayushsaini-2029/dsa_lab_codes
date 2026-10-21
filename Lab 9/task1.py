class MinHeap:
    def __init__(self,a): self.a=a; self.build()
    def build(self):
        for i in range(len(self.a)//2-1,-1,-1): self.down(i)
    def down(self,i):
        n=len(self.a); l=2*i+1; r=2*i+2; s=i
        if l<n and self.a[l]<self.a[s]: s=l
        if r<n and self.a[r]<self.a[s]: s=r
        if s!=i: self.a[i],self.a[s]=self.a[s],self.a[i]; self.down(s)
    def insert(self,v):
        self.a.append(v); i=len(self.a)-1
        while i and self.a[(i-1)//2]>self.a[i]:
            self.a[i],self.a[(i-1)//2]=self.a[(i-1)//2],self.a[i]; i=(i-1)//2

    

class MaxHeap(MinHeap):
    def down(self,i):
        n=len(self.a); l=2*i+1; r=2*i+2; s=i
        if l<n and self.a[l]>self.a[s]: s=l
        if r<n and self.a[r]>self.a[s]: s=r
        if s!=i: self.a[i],self.a[s]=self.a[s],self.a[i]; self.down(s)
    def insert(self,v):
        self.a.append(v); i=len(self.a)-1
        while i and self.a[(i-1)//2]<self.a[i]:
            self.a[i],self.a[(i-1)//2]=self.a[(i-1)//2],self.a[i]; i=(i-1)//2

print("\n------MinHeap-------")
print(MinHeap([5,2,9,1,7]).a)
print("\n------MaxHeap-------")
print(MaxHeap([5,2,9,1,7]).a)
