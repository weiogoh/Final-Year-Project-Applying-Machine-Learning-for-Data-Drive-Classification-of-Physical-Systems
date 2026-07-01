Part 3: Balancing Analysis & Cross-Validation Stability
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This part focuses on dataset balancing and model stability analysis for GHS pictogram classification. The main goal is to evaluate how different data ratios (small, medium, large) affect class distribution balance, model performance stability and cross-validation consistency. This stage emphasizes experimental comparison across dataset scales derived from different sampling ratios, rather than building a final predictive system.

Libraries Used
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

pandas - Used for data loading, manipulation and CSV handling
numpy - Used for numerical operations and array processing
re (Regular Expression) – Used for extract numeric values from text fields
matplotlib - Used for visualisation class distribution and performance plots
os - Used for file and directory management
sklearn.impute.SimpleImputer - Used for handling missing values
sklearn.preprocessing.LabelEncoder - Used for encoding categorical variables
sklearn.ensemble.RandomForestClassifier - Used as classification model
sklearn.metrics - Used for accuracy and F1-score evaluation
sklearn.model_selection.KFold - Used for cross-validation splitting
sklearn.model_selection.RepeatedKFold - Used for stability analysis via repeated folds
sklearn.multioutput.MultiOutputClassifier - Used for multi-label classification support

Operations Performed
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Data Loading and Distribution Analysis
The raw GHS dataset is loaded and the Pictogram(s) column is extracted. Multi-label entries are split into individual rows. The frequency of each GHS class is then computed to understand dataset imbalance and the distribution is visualised using a bar chart.

2. Data Filtering
The dataset is filtered into relevant GHS categories and saved into separate files for controlled sampling. The GHS categories include:-

- Corrosive
- Environmental Hazard
- Acute Toxic
- Health Hazard
- Flammable
- Irritant
- Compressed Gas
- Explosive
- Oxidizer

3. Dataset Construction Based on Ratio
Datasets are constructed using different sampling ratios resulting in three experimental groups:-

Small Ratio Dataset: low sample size per class
Medium Ratio Dataset: moderately balanced sample size
Large Ratio Dataset: high sample size

This design allows systematic evaluation of how data availability affects model behaviour and stability.

4. Data Preprocessing
Numeric values are extracted from mixed text fields using regular expressions. Missing values are handled using:-

Median imputation for numerical features
Most frequent value imputation for categorical features

Categorical variables are encoded using Label Encoding.

5. Model Training and Cross-Validation
A Random Forest Classifier is trained using K-Fold Cross Validation and Repeated K-Fold Cross Validation. Model performance is evaluated across multiple folds and repetitions to assess stability.

6. Performance Evaluation
The evaluation metrics used are accuracy and F1-score. Results are recorded for each fold and each dataset ratio group.

7. Visualisation
The following visualisations are produced: -

- Class distribution plot to show initial imbalance
- F1-score distribution plots for each ratio group
- Stability comparison across folds and repetitions
- Balanced vs imbalanced dataset comparison plot

8. Average Performance Analysis
Mean values are computed across all folds to obtain average accuracy and average F1-score.These are used to compare performance across small, medium and large ratio datasets.

Outputs of This Part
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

- result_imbalance.csv: Cross-validation result (imbalance dataset)
- plots_f1: {output}_f1_plot_imbalanced.png (output name for each output)
- average_accuracy_imbalance.csv: Average accuracy (imbalance dataset)
- average_f1score_imbalance.csv: Average F1-score (imbalance dataset)
- pictogram_counts.csv: Frequency of each GHS class
- pictogram_counts.jpg: Visualization of dataset imbalance
- filtered_acute_toxic.csv: Filtered dataset for acute toxic
- filtered_compressed_gas.csv: Filtered dataset for compressed gas
- filtered_corrosive.csv: Filtered dataset for corrosive
- filtered_environmental_hazard.csv: Filtered dataset for environmental hazard
- filtered_explosive.csv: Filtered dataset for explosive
- filtered_flammable.csv: Filtered dataset for flammable
- filtered_health_hazard.csv: Filtered dataset for health hazard
- filtered_irritant.csv: Filtered dataset for irritant
- filtered_oxidizer.csv: Filtered dataset for oxidizer
- result_small.csv: Cross-validation results (small ratio dataset)
- plots_f1_S: {output}_f1_plot_balanced_S.png (output name for each output)
- result_medium.csv: Cross-validation results (medium ratio dataset)
- plots_f1_M: {output}_f1_plot_balanced_M.png (output name for each output)
- result_large.csv: Cross-validation results (large ratio dataset)
- plots_f1_L: {output}_f1_plot_balanced_L.png (output name for each output)
- average_accuracy_small.csv: Average accuracy (small ratio dataset)
- average_f1score_small.csv: Average F1-score (small ratio dataset)
- average_accuracy_medium.csv: Average accuracy (medium ratio dataset)
- average_f1score_medium.csv: Average F1-score (medium ratio dataset)
- average_accuracy_large.csv: Average accuracy (large ratio dataset)
- average_f1score_large.csv: Average F1-score (large ratio dataset)
- imvsbal.png: Plot visualise imbalance and balance dataset f1 score

Summary
-------------------------------------------------------------------------------------------------------------------------------------------------------------------

This section of the project focuses on evaluating how different data ratios influence the stability and performance of a machine learning model for GHS pictogram classification. The process begins with analysing the original dataset to understand class imbalance through pictogram frequency distribution. The dataset is then filtered into relevant hazard categories and reorganised into ratio-based experimental groups to simulate different levels of data availability. Each group undergoes preprocessing including handling missing values extracting numeric information from mixed data types and encoding categorical variables. A Random Forest classifier is trained using K-Fold and Repeated K-Fold cross-validation to assess performance consistency across multiple splits. The results are evaluated using accuracy and F1-score followed by average performance calculations and visualisations of model stability. Overall this section demonstrates that dataset ratio has a significant impact on model reliability where smaller datasets tend to show higher variability while larger datasets generally produce more stable and consistent performance outcomes.
