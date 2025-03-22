# 📊 Prédiction d'Éligibilité aux Prêts Bancaires

## 📌 Description
Ce projet vise à utiliser l’**apprentissage automatique** pour analyser les demandes de prêt et aider les banques à **décider d’approuver ou non un prêt** en fonction des caractéristiques du client.

Les données proviennent d’un ensemble de banques et sont contenues dans le fichier **loan_data.csv**.

## 🎯 Objectifs
- **Nettoyer et prétraiter les données** 🔄
- **Appliquer des modèles de classification** (SVM, Régression Logistique) 📈
- **Comparer les performances des modèles** avec des métriques d’évaluation ✅
- **Visualiser les résultats pour mieux comprendre les tendances** 📊

## 🗂 Contenu du Dataset
| **Variable**        | **Description** |
|---------------------|----------------|
| `Loan_ID`          | Identifiant du prêt |
| `Gender`           | Sexe du demandeur (Male/Female) |
| `Married`          | Statut matrimonial (Y/N) |
| `Dependents`       | Nombre de personnes à charge |
| `Education`        | Niveau d’éducation (Graduate/Under Graduate) |
| `Self_Employed`    | Travailleur indépendant (Y/N) |
| `ApplicantIncome`  | Revenu du demandeur |
| `CoapplicantIncome` | Revenu du co-demandeur |
| `LoanAmount`       | Montant du prêt |
| `Loan_Amount_Term` | Durée du prêt en mois |
| `Credit_History`   | Nombre de crédits antécédents |
| `Property_Area`    | Type de zone (Urban/Semi-Urban/Rural) |
| `Loan_Status`      | Statut du prêt (Approuvé/Non approuvé) |

## 🔧 Technologies Utilisées
- **Python** 🐍
- **Pandas, NumPy** pour le traitement des données 🏗
- **Scikit-learn** pour l’apprentissage automatique 🤖
- **Matplotlib, Seaborn** pour la visualisation 📊

## 🚀 Étapes du Projet
1️⃣ **Exploration et nettoyage des données**
- Remplacement des valeurs manquantes
- Encodage des variables catégoriques

2️⃣ **Prétraitement et sélection des variables**
- Suppression des colonnes inutiles
- Standardisation des données

3️⃣ **Entraînement et évaluation des modèles**
- **Support Vector Machine (SVM)**
- **Régression Logistique**
- Comparaison des modèles avec **accuracy_score** et **classification_report**

4️⃣ **Visualisation des résultats**
- Analyse du revenu du demandeur en fonction de divers critères
- Visualisation des tendances avec **Matplotlib et Seaborn**
