temperature = float(input("Enter the Current temperature: "))
rain = bool(input("Is it raining? (True/False): "))

if 15 < temperature < 30 and rain == False:
    print("Go ahead with the picnic")
else:
    print("Cancel the picnic")
