name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")
monthly_purchases = []
total = 0
print("\nEnter Monthly Purchase Amounts:")
for i in range(1, 13):
    amount = float(input(f"Month {i}: "))
    monthly_purchases.append(amount)
    total += amount
average = total / 12
print("\n----- Annual Purchase / Billing Report -----")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Total Annual Purchase: Rs.", total)
print("Average Monthly Purchase: Rs.", average)
