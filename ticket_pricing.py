age = int(input("Enter Your Age: "))

if age < 12:
    print("Tickets for Children")
elif age >= 65:
    print("Tickets for Seniors")
elif 12 <= age < 65:
    print("Ticket for Adults")
