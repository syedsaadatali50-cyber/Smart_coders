num = int(input("Enter a 3-digit number: "))

if num < 100 or num > 999:
    print("Please enter a 3-digit number")
else:
    a = num // 100
    b = (num // 10) % 10
    c = num % 10

    sum = a**3 + b**3 + c**3

    if sum == num:
        print("It is an Armstrong number")
    else:
        print("It is not an Armstrong number")