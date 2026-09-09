import math

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

D = b * b - 4 * a * c

if D > 0:
    root1 = (-b + math.sqrt(D)) / (2 * a)
    root2 = (-b - math.sqrt(D)) / (2 * a)

    print("Roots are real and different")
    print("Root 1 =", root1)
    print("Root 2 =", root2)

elif D == 0:
    root = -b / (2 * a)

    print("Roots are real and equal")
    print("Root =", root)

else:
    real = -b / (2 * a)
    imaginary = math.sqrt(-D) / (2 * a)

    print("Roots are imaginary")
    print("Root 1 =", real, "+", imaginary, "i")
    print("Root 2 =", real, "-", imaginary, "i")