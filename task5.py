import csv

with open("task5.csv", "w+") as f:
    while True:
        name = input("What is your name? (or quit) ")
        if name == "quit":
            break
        else:
            f.write(f"{name}\n")
    
    f.seek(0)
    for line in f.readlines():
        print(line)