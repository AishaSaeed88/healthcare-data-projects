import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/illness_data.csv")
print(df.head())

df.plot(x="Month", kind="bar", figsize=(12,6))
plt.title("Monthly Illness Cases")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/bar_chart.png")
plt.show()

totals = df[["Flu","Fever","Asthma","Stomach_Upset"]].sum()
plt.figure(figsize=(7,7))
plt.pie(totals, labels=totals.index, autopct="%1.1f%%", startangle=140)
plt.title("Total Illness Distribution (Yearly)")
plt.savefig("visuals/pie_chart.png")
plt.show()
