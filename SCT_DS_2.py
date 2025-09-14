import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('titanic.csv')

# Clean data
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Embarked'].fillna(data['Embarked'].mode()[0], inplace=True)

# Just 3 key visualizations
fig, axes = plt.subplots(1, 3, figsize=(15, 4))

# 1. Survival by gender
data.groupby('Sex')['Survived'].mean().plot(kind='bar', ax=axes[0], color=['pink', 'blue'])
axes[0].set_title('Survival Rate by Gender')

# 2. Survival by class
data.groupby('Pclass')['Survived'].mean().plot(kind='bar', ax=axes[1], color=['gold', 'silver', 'brown'])
axes[1].set_title('Survival Rate by Class')

# 3. Age distribution
axes[2].hist(data['Age'], bins=20, color='green', alpha=0.7)
axes[2].set_title('Age Distribution')

plt.tight_layout()
plt.show()