def print_numbers(n):
    if n == 0:
        return

    print_numbers(n - 1)

    print(n, end=" ")

    if n == 1:
        return


n = int(input("Enter N: "))

print_numbers(n)

for i in range(n - 1, 0, -1):
    print(i, end=" ")