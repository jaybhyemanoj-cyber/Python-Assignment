import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("sales_data.csv")

plt.plot(df["month_number"], df["total_profit"])
plt.xlabel("Month")
plt.ylabel("Total Profit")
plt.title("Total Profit Per Month")
plt.show()

plt.plot(df["month_number"], df["facecream"], label="Face Cream")
plt.plot(df["month_number"], df["facewash"], label="Face Wash")
plt.plot(df["month_number"], df["toothpaste"], label="Toothpaste")
plt.plot(df["month_number"], df["bathingsoap"], label="Bathing Soap")
plt.legend()
plt.xlabel("Month")
plt.ylabel("Sales")
plt.title("Product Sales Data")
plt.show()

products = ["facecream", "facewash"]
sales = df[products].sum()

plt.bar(products, sales)
plt.title("Face Cream and Face Wash Sales")
plt.show()

total_sales = df.drop(columns=["month_number", "total_profit"]).sum()

plt.pie(total_sales, labels=total_sales.index, autopct="%1.1f%%")
plt.title("Total Yearly Sales by Product")
plt.show()