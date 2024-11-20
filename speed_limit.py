speed_limit = int(input("Write the speed limit: "))
if 60 < speed_limit <= 80:
    print("Fine is $100")
elif speed_limit > 80:
    print("Fine is $200")
else:
    print("No fine")
