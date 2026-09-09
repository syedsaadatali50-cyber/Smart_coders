hour = int(input("Enter the hour (0-23): "))

if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 16:
    print("Good Afternoon")
elif 17 <= hour <= 20:
    print("Good Evening")
elif 0 <= hour <= 4 or 21 <= hour <= 23:
    print("Good Night")
else:
    print("Invalid hour")