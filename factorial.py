# numbers = [1, 3, 5, 6, 8]
#
# for x in numbers:
#     print(x)

# vowels = "aeiou"
# count = 0
#
# phrase = input("Enter sentence: ").lower()
#
# for letter in phrase:
#     if letter in vowels:
#         count = count + 1
#
# print(f"Number of vowels is {count}")

vowels = "aeiou"
phrase = input("Enter sentence: ").lower()
test_list = []

for letter in phrase:
    if letter in vowels:
        test_list.append(letter)

print(test_list)
print(len(test_list))


