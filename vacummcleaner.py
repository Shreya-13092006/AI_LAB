room = input("enter room")
status =  int(input("1.clean\n2.Not Clean"))
if status==2:
    print("cleaning")
elif room == "a":
    print("moving right")
else:
    print("moving left")
