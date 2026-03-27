import pandas as pd

df = pd.read_excel("employee.xlsx")

auto_employees = df[df["Department"] == "Automotive"]
print(auto_employees)

emp_id = int(input("Enter Employee ID: "))
employee_details = df[df["Employee ID"] == emp_id]
print(employee_details)

developers = df[df["Designation"] == "Developer"]
print(developers)