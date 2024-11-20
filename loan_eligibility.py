# from contextlib import nullcontext
#
# salary = int(input("Enter current salary: "))
# loan = int(input("Enter outstanding loan amt: "))
#
# if salary >= 30000 and loan == 0:
#     print("You are eligible to take a loan")
#     if loan * -1 < 0:
#      print ("Invalid")
# else:
#     print("You are not eligible to take a loan")

loan = -5000
if loan * -1 > 0:
    print("positive")
elif loan * -1 < 0:
    print("negative")