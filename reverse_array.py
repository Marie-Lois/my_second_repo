numbers = [1, 2, 3, 4, "Money"]
test = []
indexx = -1

for item in numbers:
    test.append(numbers[indexx])
    indexx = indexx - 1

print(test)
print(numbers[::-1])