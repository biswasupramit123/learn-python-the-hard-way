
numbers = []

def count_wn(x):
    i = 0
    while i <= x:
        print("At the top i is %d" % i)
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print("At the bottom i is %d" % i)

    print("The numbers: ", end="")

y = int(input("Give the number of whole numbers you want to count to: "))
count_wn(y)

for num in numbers:
    print(num," ", end="")
