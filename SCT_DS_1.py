import matplotlib.pyplot as plt

age_groups = ['0 to 20 years' , '21 to 64 years ','65+ years']
population = [512, 807, 78]
colors = ['#FF9999', '#66B2FF', '#99FF99']

plt.figure(figsize=(8,6))
bars = plt.bar(age_groups, population, color=colors, edgecolor='black')

for i, value in enumerate(population):
    plt.text(i, value+10, f'{value} Mn', ha='center', va='bottom')

plt.title("India's Population Distribution by Age (2022)")
plt.xlabel('Age Groups')
plt.ylabel('Population (Millions)')

plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()