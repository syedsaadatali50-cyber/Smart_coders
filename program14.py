n = int(input("Enter a number: "))
k = int(input("Enter the bit position: "))

if n & (1 << k):
    print("The Kth bit is set")
else:
    print("The Kth bit is not set")