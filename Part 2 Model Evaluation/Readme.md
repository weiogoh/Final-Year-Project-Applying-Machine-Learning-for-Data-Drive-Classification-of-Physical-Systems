Part 2: Model Evaluation
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

This part focuses on evaluating multiple machine learning models using a structured pipeline. The system trains different models on various feature combinations, compares their performance using evaluation metrics, and identifies the best-performing model for each output class. It also provides visual analysis to help interpret results more effectively.

Libraries Used
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Machine Learning Models (scikit-learn):-
- sklearn.tree.DecisionTreeClassifier – builds a tree-based classification model
- sklearn.ensemble.RandomForestClassifier – ensemble of decision trees for improved accuracy
- sklearn.ensemble.GradientBoostingClassifier – sequential boosting model for reducing errors
- sklearn.svm.SVC – support vector machine for classification using hyperplanes
- sklearn.neighbors.KNeighborsClassifier – classifies based on nearest neighbors
- sklearn.naive_bayes.GaussianNB – probabilistic classifier assuming Gaussian distribution
- sklearn.linear_model.LogisticRegression – linear model for binary/multi-class classification
- sklearn.discriminant_analysis.LinearDiscriminantAnalysis – classification and dimensionality reduction method
- sklearn.neural_network.MLPClassifier – feedforward neural network for non-linear learning
- sklearn.cluster.KMeans – unsupervised clustering algorithm

Model Training & Evaluation:-
- sklearn.model_selection.train_test_split – splits dataset into training and testing sets
- sklearn.metrics.accuracy_score – measures overall prediction correctness
- sklearn.metrics.precision_score – measures correctness of positive predictions
- sklearn.metrics.recall_score – measures ability to detect actual positives
- sklearn.metrics.f1_score – harmonic mean of precision and recall

Preprocessing:-
- SimpleImputer – fills missing values in dataset
- StandardScaler – standardizes features for better model performance

Data Handling:-
- pandas – data loading and manipulation using DataFrames
- numpy – numerical operations and array processing
- itertools.combinations – generates all possible feature combinations

Visualisation:-
- matplotlib.pyplot – creates graphs, heatmaps and dartboard visualisations

Operations Performed
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Model Setup and Selection: Each machine learning model is implemented in separate .py files with predefined hyperparameters. These model files are imported into a central controller module. The user selects which models to run by entering corresponding numeric inputs mapped to each model.

2. Data Loading and Preprocessing: The system loads two datasets which are Main dataset and Feature selection dataset. Data preprocessing is performed including:-
- Data cleaning
- Missing value handling
- Feature scaling (StandardScaler)

3. Feature Combination and Model Training: Each GHS output class is processed individually. A fixed set of 7 main features is used. All possible feature combinations are generated using 7C1 to 7C7 (127 combinations total). Each feature combination is used to train and test the selected models. Predictions are evaluated and stored for every combination.

4. Result Storage and Performance Analysis:Results are saved into Results_{model_tag}.csv
(Recommended: run models one by one to avoid very large CSV files and long execution time when multiple models are selected.) The best-performing feature combination for each GHS output is extracted for each model. Two summary files are generated:-
- highest_fc_for_each_GHS_acc.csv (based on Accuracy)
- highest_fc_for_each_GHS_f1.csv (based on F1-score)

5. Visualization and Interpretation: A heatmap is generated to compare model performance across all GHS outputs. A dartboard plot (F1-score based) is created to visualize performance consistency:-
- Points near the center → high F1-score (strong performance)
- Mixed distribution → inconsistent performance across feature sets
- Points far from center → generally poor performance

Outputs Generated
------------------------------------------------------------------------------------------------------------------------------------------------------------------------

- Results_<MODEL>.csv: full evaluation results for each model
- highest_fc_for_each_GHS_acc.csv: best feature combination per class (accuracy-based)
- highest_fc_for_each_GHS_f1.csv: best feature combination per class (F1-based)
- heatmap_f1.png: model comparison heatmap (F1-based)
- heatmap_acc.png: model comparison heatmao (accuracy-based)
- Dartboard f1score <MODEL>.png: class-wise performance visualisation

Summary
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
This section provides a complete machine learning evaluation framework that compares multiple algorithms under different feature combinations. It identifies the best-performing models per class using F1-score and presents the results in both tabular and visual formats, enabling clear interpretation of model performance across the dataset.
