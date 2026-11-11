a = input("A room (clean/dirty): ")
b = input("B room (clean/dirty): ")

p = input("Vacuum at (A/B): ")
battery = int(input("Battery percentage: "))


memory = {
    "A": a,
    "B": b
}

while battery > 0:

    visited = input("\nDid someone visit a room? (A/B/none): ")

    if visited == "A":
        a = "dirty"
        memory["A"] = "dirty"
        print("Someone visited A -> A is now dirty.")

    elif visited == "B":
        b = "dirty"
        memory["B"] = "dirty"
        print("Someone visited B -> B is now dirty.")

    elif visited == "none":
        print("Nobody visited a room.")

    else:
        print("Invalid input. No room was changed.")


    if p == "A":

        if a == "dirty":
            print("Cleaning A...")
            a = "clean"
            memory["A"] = "clean"
            battery -= 10
        else:
            print("A is already clean.")


        if battery > 0:
            print("Moving to B...")
            p = "B"
            battery -= 5


    else:

        if b == "dirty":
            print("Cleaning B...")
            b = "clean"
            memory["B"] = "clean"
            battery -= 10
        else:
            print("B is already clean.")

        if battery > 0:
            print("Moving to A...")
            p = "A"
            battery -= 5


    if battery < 0:
        battery = 0

    print("\n--- Status ---")
    print("A:", a)
    print("B:", b)
    print("Vacuum:", p)
    print("Battery:", battery, "%")
    print("Memory:", memory)

print("\nBattery dead!")
print("Vacuum stopped.")
print("Final A:", a)
print("Final B:", b)
print("Battery:", battery, "%")
