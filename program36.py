CP = float(input("Enter Cost Price: "))
SP = float(input("Enter Selling Price: "))

if SP > CP:
    profit = SP - CP
    print("Profit =", profit)

elif CP > SP:
    loss = CP - SP
    print("Loss =", loss)

else:
    print("No profit, no loss")