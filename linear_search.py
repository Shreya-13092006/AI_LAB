a = [i for i in range(7)]
search  = int(input("enter a search ele"))
for i in range(len(a)):
    if a[i]==search:
        print("found at:",i+1)
        break
else:
    print("not found")