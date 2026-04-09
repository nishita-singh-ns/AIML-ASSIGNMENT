import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset
study_hours = [1, 2, 3, 4, 5, 6]
marks = [35, 50, 60, 70, 85, 95]

data = pd.DataFrame({
    "Study Hours": study_hours,
    "Marks": marks
})

# Bar Chart
plt.bar(data["Study Hours"], data["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.show()

# Pie Chart
plt.pie(data["Marks"], labels=data["Study Hours"], autopct='%1.1f%%')
plt.title("Marks Distribution")
plt.show()

# Histogram
plt.hist(data["Marks"], bins=5)
plt.title("Marks Histogram")
plt.show()

