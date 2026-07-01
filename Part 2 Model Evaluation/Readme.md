Part 2: Model Evaluation
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This part focuses on evaluating multiple machine learning models using a structured pipeline. The system trains different models on various feature combinations, compares their performance using evaluation metrics and identifies the best-performing model for each output class. It also provides visual analysis to help interpret results more effectively.

Libraries Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Machine Learning Models (scikit-learn):
- DecisionTreeClassifier – Builds a tree-based classification model
- RandomForestClassifier – Ensemble of decision trees for improved accuracy
- GradientBoostingClassifier – Sequential boosting model for reducing errors
- SVC – Support vector machine for classification using hyperplanes
- KNeighborsClassifier – Classifies based on nearest neighbours
- GaussianNB – Probabilistic classifier assuming Gaussian distribution
- LogisticRegression – Linear model for binary and multi-class classification
- LinearDiscriminantAnalysis – Classification and dimensionality reduction method
- MLPClassifier – Feedforward neural network for non-linear learning
- KMeans – Unsupervised clustering algorithm
- Model Training and Evaluation
- train_test_split – Splits dataset into training and testing sets
- accuracy_score – Measures overall prediction correctness
- precision_score – Measures correctness of positive predictions
- recall_score – Measures ability to detect actual positives
- f1_score – Harmonic mean of precision and recall

Preprocessing
- SimpleImputer – Handles missing values in dataset
- StandardScaler – Standardises features for improved model performance

Data Handling
- pandas – Data loading and manipulation using DataFrames
- numpy – Numerical operations and array processing
- itertools.combinations – Generates all possible feature combinations

Visualisation
- matplotlib.pyplot – Creates graphs heatmaps and dartboard visualisations

Operations Performed
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Model Setup and Selection
Each machine learning model is implemented in separate Python files with predefined hyperparameters. These model files are imported into a central controller module. The user selects which models to run by entering corresponding numeric inputs mapped to each model.

2. Data Loading and Preprocessing
The system loads two datasets:-

- Main dataset
- Feature selection dataset

Data preprocessing includes:-

- Data cleaning
- Missing value handling
- Feature scaling using StandardScaler

3. Feature Combination and Model Training
Each GHS output class is processed individually. A fixed set of 7 main features is used. All possible feature combinations are generated using 7C1 to 7C7 (127 combinations in total). Each feature combination is used to train and test the selected models. Predictions are evaluated and stored for every combination.

4. Result Storage and Performance Analysis
Results are saved into Results_{model_tag}.csv. It is recommended to run models one at a time to avoid large file sizes and long execution times when multiple models are selected. The best-performing feature combination for each GHS output is extracted for each model. Two summary files are generated:-

- highest_fc_for_each_GHS_acc.csv (based on accuracy)
- highest_fc_for_each_GHS_f1.csv (based on F1-score)

5. Visualisation and Interpretation
A heatmap is generated to compare model performance across all GHS outputs. A dartboard plot (based on F1-score) is created to visualise performance consistency:-

- Points near the centre: high F1-score (strong performance)
- Mixed distribution: inconsistent performance across feature sets
- Points far from centre: poor performance

Outputs of This Part
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

Results_{model_tag}.csv – Full evaluation results for each model
highest_fc_for_each_GHS_acc.csv – Best feature combination per class (accuracy-based)
highest_fc_for_each_GHS_f1.csv – Best feature combination per class (F1-score-based)
heatmap_f1.png – Model comparison heatmap (F1-based)
heatmap_acc.png – Model comparison heatmap (accuracy-based)
dartboard_f1score.png – Class-wise performance visualisation

Summary
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section provides a complete machine learning evaluation framework that compares multiple algorithms under different feature combinations. It identifies the best-performing models per class using F1-score and presents the results in both tabular and visual formats, enabling clear interpretation of model performance across the dataset.
