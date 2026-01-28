V = float(input("Enter voltage (V): "))
R = float(input("Enter resistance (R): "))
I = V / R
print("Current (I) = ",I,"A")
if I < 0.5:
    print("Low current")
elif 0.5 <= I <= 2:
    print("Normal current")
else:
    print("High current")

    