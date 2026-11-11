a = [i for i in range(7)]
a.sort()
search  = int(input("enter a search ele"))
l=0
r=len(a)-1
while l<=r:
    mid = int((l+r)/2)
    if a[mid]==search:
        print("found at:",mid+1)
        break
    elif a[mid]>search:
        r=mid-1
    else:
        l=mid+1
else:
    print("not found")
