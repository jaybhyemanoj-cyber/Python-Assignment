Hardness = float(input("Enter hardness: "))
Carbon_content  = float(input("Enter carbon content: "))
Tensile_strength  = float(input("Enter tensile strength: "))
cond1 = Hardness > 50
cond2 = Carbon_content  < 0.7
cond3 = Tensile_strength  > 5600
if cond1 and cond2 and cond3:
    grade = 10
elif cond1 and cond2:
    grade = 9
elif cond2 and cond3:
    grade = 8
elif cond1 and cond3:
    grade = 7
elif cond1 or cond2 or cond3:
    grade = 6
else:
    grade = 5
print("Grade of the steel = ",grade)
