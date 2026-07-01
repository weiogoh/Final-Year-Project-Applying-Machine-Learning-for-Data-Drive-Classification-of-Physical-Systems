Part 1: Feature Selection and Feature Reduction
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This is the first stage of the chemical hazard classification project. The main objective of this part is to clean and preprocess the raw dataset, engineer meaningful features and identify the most important variables for predicting chemical hazard categories. This stage also includes feature importance analysis using a Random Forest model and final feature reduction to produce a compact and optimised feature set. The output of this part is used as the input for later stages such as model evaluation and data balancing analysis.

Libraries Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

pandas – Used for loading, cleaning, manipulating and exporting datasets
numpy – Used for numerical operations and handling infinite values
re (Regular Expression) – Used for cleaning feature values by removing non-numeric characters
scikit-learn (sklearn) – Used for machine learning tasks including:
train_test_split - splitting dataset
SimpleImputer - handling missing values
StandardScaler - feature normalisation
RandomForestClassifier - model training and feature importance extraction

Operations Performed
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Data Loading
The dataset is loaded using pandas and initial missing values are replaced with zero for consistency.

2. Data Cleaning
A custom cleaning function is applied to feature columns:-

- Removes non-numeric characters using regex
- Converts values into float format
- Replaces invalid values with zero

This ensures all input data is fully numerical.

3. Feature Selection
Feature columns are selected from index 2 to 69. Only numerical features are retained for model training.

4. Label Engineering (Multi-Label Classification)
The Pictogram(s) column is processed and converted into binary labels for the following categories:-

- Irritant
- Acute Toxic
- Flammable
- Corrosive
- Health Hazard
- Environmental Hazard
- Compressed Gas
- Explosive
- Oxidiser

5. Train-Test Split
The dataset is split into 80% training data and 20% testing data. The random state is fixed to ensure reproducibility.

6. Missing Value and Infinite Value Handling
Missing values are handled using mean imputation and infinite values are replaced with zero.

7. Feature Scaling
StandardScaler is applied to normalise feature values and ensure consistent scaling across all features.

8. Model Training (Baseline)
A Random Forest Classifier is trained as a baseline model to:

- Learn relationships between features and hazard labels
- Compute feature importance values

9. Feature Importance Analysis
Feature importance is computed separately for each hazard category. This identifies the contribution of each feature towards predicting each class.

10. Top Feature Extraction
The top 5 most important features are selected for each hazard category. This results in a total of 45 feature entries (9 GHS outputs × 5 features per class).

11. Feature Consolidation
After exporting top5_feature_importances.csv, a consolidation process is performed using Google Sheets with the formula =UNIQUE(B2:B100). This removes duplicate features across categories. The final result produces 7 main features. These features represent the most stable and consistently important variables across all hazard categories. The final reduced dataset is saved as features.csv.

Outputs of This Part
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

- top5_feature_importances.csv – Top 5 features per hazard category including importance scores
- features.csv – Final reduced feature set containing 7 optimised features

Summary
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section focuses on full data preparation, feature engineering and feature reduction. The dataset is cleaned, transformed and used to train a Random Forest model for feature importance analysis. The most important features are extracted per hazard category and then consolidated to remove redundancy. This process results in a final set of 7 key features which will be used as the input for the next stages of the project including model evaluation and balancing analysis.
