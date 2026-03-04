numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

print("Total number of items in tuple:", len(numbers))
print("Last item in tuple:", numbers[-1])
print("Tuple in reverse order:", numbers[::-1])

if 5 in numbers:
    print("The tuple contains 5")
else:
    print("The tuple does not contain 5")

if len(numbers) > 2:
    new_tuple = numbers[1:-1]
    sorted_tuple = tuple(sorted(new_tuple))
    print("Tuple after removing first & last and sorting:", sorted_tuple)
else:
    print("Not enough elements to remove first and last item.")