age = 11
year = 2024
for i in range(age):
    rok = year - age + i
    print(f"V roce {rok} Ti bylo {i} let")
#
for i in range(1,11):
    for j in range(1,11):
        print(i*j, end ="")
        print()
#
a = int(input("jaky je rozmer obrazce"))
b = int(input("jaky je rozmer obrazce"))
for i in range(0,a):
    for j in range(0,b):
        print("*", end="")
    print()