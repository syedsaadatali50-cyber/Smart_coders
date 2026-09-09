age = int(input("Enter your age: "))

if age < 13:
    print("Category: Child")
elif age <= 19:
    print("Category: Teenager")
elif age < 60:
    print("Category: Adult")
else:
    print("Category: Senior")