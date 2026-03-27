import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Company": ["Microsoft", "Google", "Amazon", "IBM", "Deloitte", "Capgemini", "ATOS", "Amdocs"],
    "Recruitments": [120, 150, 170, 90, 80, 110, 70, 95]
}

df = pd.DataFrame(data)

plt.bar(df["Company"], df["Recruitments"])
plt.xticks(rotation=45)
plt.title("New Recruitments - Bar Chart")
plt.show()

plt.pie(df["Recruitments"], labels=df["Company"], autopct="%1.1f%%")
plt.title("Recruitments Distribution")
plt.show()

plt.pie(df["Recruitments"], labels=df["Company"], autopct="%1.1f%%",
        wedgeprops={"edgecolor": "black"})
plt.title("Customized Pie Chart")
plt.show()

plt.pie(df["Recruitments"], labels=df["Company"], autopct="%1.1f%%",
        wedgeprops={"width":0.4})
plt.title("Doughnut Chart")
plt.show()

compare = df[df["Company"].isin(["IBM", "Amdocs"])]

plt.bar(compare["Company"], compare["Recruitments"])
plt.title("IBM vs Amdocs Recruitment Comparison")
plt.show()