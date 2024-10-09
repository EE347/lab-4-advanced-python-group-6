name = input("What is your name? ")
with open("task3.txt", "a") as f:
    f.write(f"{name}\n")
    