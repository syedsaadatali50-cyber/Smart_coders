n = int(input("Enter a number: "))

if n < 2:
    print("It is not a prime number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("It is a prime number")
    else:
        print("It is not a prime number")