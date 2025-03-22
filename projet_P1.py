import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns


def encoder(df):
    label_encoder = LabelEncoder()

    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            # Remplacer les valeurs nulles par la valeur la plus fréquente
            df[col].fillna(df[col].mode()[0], inplace=True)

            # Utiliser LabelEncoder pour encoder les valeurs non numériques
            df[col] = label_encoder.fit_transform(df[col].astype(str))

        elif df[col].isnull().any():
            # Remplacer les valeurs nulles dans les colonnes numériques par la moyenne
            df[col].fillna(df[col].mean(), inplace=True)

    return df

def supprime(df, columns_to_keep):
    # Supprimer les colonnes inutiles
    df = df[columns_to_keep]
    return df

proj = pd.read_csv('Loan.csv')
#1
print(proj.info)
#2
print(proj.describe())
#3 et 4
proj1= encoder(proj)
print("\nAprès les modifications :")
print(proj1.info)
print(proj1.describe())
#5
Lescolonnes = ['Loan_ID', 'Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                         'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                         'Credit_History', 'Property_Area', 'Loan_Status']
proj2=supprime(proj1, Lescolonnes)
print("ap")
print(proj2)
#6
print("\nNouvelle dimension de l'ensemble de données :")
print(proj2.shape)

print("\nTypes de données après les modifications :")
print(proj2.dtypes)

print(proj2.describe())
#7
print("\nOpérations statistiques de base pour la nouvelle version :")
print("Total par colonne :")
print(proj2.sum())
print("\nValeur minimale par colonne :")
print(proj2.min())
print("\nValeur maximale par colonne :")
print(proj2.max())
print("\nPourcentage des valeurs uniques par colonne :")
print(proj2.nunique() / len(proj2) * 100)
print("\nMoyenne par colonne :")
print(proj2.mean())
print("\nÉcart type par colonne :")
print(proj2.std())
#8
# Diviser les données en ensembles d'entraînement et de test
X = proj2.drop('Loan_Status', axis=1)  # Features
y = proj2['Loan_Status']  # Target variable

# Diviser les données en ensembles d'entraînement et de test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Appliquer SVM
svm_model = SVC()
svm_model.fit(X_train, y_train)
svm_predictions = svm_model.predict(X_test)
#9
# Mesurer la performance du SVM
print("\nPerformance du SVM :")
print("Accuracy:", accuracy_score(y_test, svm_predictions))
print("\nClassification Report:")
print(classification_report(y_test, svm_predictions, zero_division=1))

# Appliquer la régression logistique
logreg_model = LogisticRegression()
logreg_model.fit(X_train, y_train)
logreg_predictions = logreg_model.predict(X_test)

# Mesurer la performance de la régression logistique
print("\nPerformance de la régression logistique :")
print("Accuracy:", accuracy_score(y_test, logreg_predictions))
print("\nClassification Report:")
print(classification_report(y_test, logreg_predictions, zero_division=1))
