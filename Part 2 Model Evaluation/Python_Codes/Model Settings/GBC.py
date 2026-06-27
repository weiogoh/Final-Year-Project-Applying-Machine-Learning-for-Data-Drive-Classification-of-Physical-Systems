from sklearn.ensemble import GradientBoostingClassifier

def create_model():
    """
    Creates and returns a Gradient Boosting Classifier model.

    Gradient Boosting is an ensemble learning method that builds models
    sequentially, where each new model corrects errors made by previous ones.

    Returns:
        GradientBoostingClassifier: An untrained gradient boosting model
    """

    # Initialize Gradient Boosting Classifier with tuned hyperparameters
    model = GradientBoostingClassifier(
        n_estimators=300,      # Number of boosting stages (trees)
        learning_rate=0.05,    # Step size contribution of each tree
        max_depth=3,           # Maximum depth of individual trees (controls complexity)
        subsample=0.8,         # Fraction of samples used per tree (adds randomness, reduces overfitting)
        max_features='sqrt',   # Number of features considered for splitting (helps generalization)
        random_state=42        # Ensures reproducible results
    )

    # Return the configured but untrained model
    return model