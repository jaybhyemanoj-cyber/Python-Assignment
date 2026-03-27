import pandas as pd

data = {
    "State": ["Maharashtra", "Gujarat", "Rajasthan", "Karnataka", "Punjab"],
    "Area": [307713, 196244, 342239, 191791, 50362],
    "Population": [112374333, 60439692, 68548437, 61095297, 27743338]
}

df = pd.DataFrame(data)

print("\nState Data:\n", df)

print("\nState with Largest Area:")
print(df.loc[df['Area'].idxmax()]['State'])

print("\nState with Largest Population:")
print(df.loc[df['Population'].idxmax()]['State'])

df['Density'] = df['Population'] / df['Area']
print("\nWith Density:\n", df)

print("\nState with Highest Density:")
print(df.loc[df['Density'].idxmax()]['State'])