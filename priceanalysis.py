prices = tuple(map(float, input("Enter prices separated by space: ").split()))

print("Total items sold:", len(prices))
print("Cheapest item price:", min(prices))
print("Costliest item price:", max(prices))
print("Prices in ascending order:", tuple(sorted(prices)))

costliest_price = max(prices)
count = prices.count(costliest_price)
print("Number of costliest items sold:", count)