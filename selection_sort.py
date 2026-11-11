a = [7,7,2,3,7,1,2,3,7,8,9,4,3]
n= len(a)
for i in range(n):
    minid = i
    for j in range(i+1,n):
        if a[j]<a[minid]:
            minid = j
    if minid !=i:
        a[i],a[minid]=a[minid],a[i]
print("sorted array", a)
