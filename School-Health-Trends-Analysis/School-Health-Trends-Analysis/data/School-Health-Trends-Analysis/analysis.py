# School Health Trends Analysis
# Author: Aisha Saeed

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/illness_data.csv")

# Display first rows
print(df.head())

# Bar Chart
df.plot(x="Month", kind="bar", figsize=(12,6))
plt.title("Monthly Illness Cases")
plt.ylabel("Number of Cases")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/bar_chart.png")
plt.show()

# Pie Chart
totals = df[["Flu","Fever","Asthma","Stomach_Upset"]].sum()
plt.figure(figsize=(7,7))
plt.pie(totals, labels=totals.index, autopct="%1.1f%%", startangle=140)
plt.title("Total Illness Distribution (Yearly)")
plt.savefig("visuals/pie_chart.png")
plt.show()

# Insights
print("\n--- Key Insights ---")
print("• Flu peaks in winter (Dec–Jan).")
print("• Asthma increases in late spring and summer.")
print("• Stomach-related illnesses remain steady.")
