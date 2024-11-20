from itertools import count

vowels = "aeiou"
count = 0

phrase = input("Enter sentence: ")

for letter in phrase:
    if letter in vowels:
        count = count + 1

print(f"Number of vowels are {count}")
