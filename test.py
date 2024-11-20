number = int(input("Number: "))

# for x in range(1, 21, 2):
#     print(x)

result = 1
for x in range(1, number + 1):
    result = result * x

print("The factorial of {} is {}".format(number, result))