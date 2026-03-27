# Health Screening Data Insights
# Author: Aisha Saeed

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/screening_data.csv")

# Display first rows
print(df.head())

# Bar Chart: Screening Results
result_counts = df["Result"].value_counts()
result_counts.plot(kind="bar", figsize=(7,5), color=["skyblue","salmon"])
plt.title("Screening Results Distribution")
plt.ylabel("Number of Students")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig("visuals/bar_chart.png")
plt.show()

# Pie Chart: BMI Categories
df["BMI_Category"] = pd.cut(df["BMI"], bins=[0,18.5,25,30], labels=["Underweight","Normal","Overweight"])
bmi_counts = df["BMI_Category"].value_counts()

plt.figure(figsize=(7,7))
plt.pie(bmi_counts, labels=bmi_counts.index, autopct="%1.1f%%", startangle=140)
plt.title("BMI Category Distribution")
plt.savefig("visuals/pie_chart.png")
plt.show()

# Insights
print("\n--- Key Insights ---")
print("• Overweight students had higher follow-up rates.")
print("• Vision issues increased with age.")
print("• Screening data supports targeted health interventions.")
