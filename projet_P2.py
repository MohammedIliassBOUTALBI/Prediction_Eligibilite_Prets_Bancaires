import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

proj = pd.read_csv('Loan.csv')
# A. Montrer le revenu du demandeur en fonction de :
# 1.Le sexe et de la situation civile (Married)
sns.catplot(x='Gender', y='ApplicantIncome', hue='Married', kind='bar', data=proj)
plt.show()

# 2.Le sexe et le niveau d’éducation
sns.catplot(x='Gender', y='ApplicantIncome', hue='Education', kind='bar', data=proj)
plt.show()

# 3.La situation civile et le niveau d’éducation
sns.catplot(x='Married', y='ApplicantIncome', hue='Education', kind='bar', data=proj)
plt.show()

# 4.Le type de travail (Self_Employed)
sns.catplot(x='Self_Employed', y='ApplicantIncome', kind='bar', data=proj)
plt.show()

# 5.Le nombre de personnes à charge
sns.scatterplot(x='Dependents', y='ApplicantIncome', data=proj)
plt.show()

# 6.Le nombre de crédits antécédents et la localisation
sns.catplot(x='Credit_History', y='ApplicantIncome', hue='Property_Area', kind='bar', data=proj)
plt.show()

# 7.Le niveau d’éducation et le nombre de crédits antécédents
sns.catplot(x='Education', y='ApplicantIncome', hue='Credit_History', kind='bar', data=proj)
plt.show()

# 8.Montrer le montant du prêt en fonction du revenu du demandeur
sns.scatterplot(x='ApplicantIncome', y='LoanAmount', data=proj)
plt.show()
