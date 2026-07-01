from sklearn.linear_model import LogisticRegression

def create_model():
    """
    Creates and returns a Logistic Regression model.

    Logistic Regression is a supervised learning algorithm used for
    binary or multi-class classification problems. It estimates the
    probability of class membership using a logistic function.

    Returns:
        LogisticRegression: An untrained logistic regression model
    """

    # Initialize Logistic Regression model with specified hyperparameters
    model = LogisticRegression(
        penalty='l2',        # L2 regularization to prevent overfitting
        C=1.0,               # Inverse of regularization strength (smaller = stronger regularization)
        solver='lbfgs',      # Optimization algorithm suitable for small/medium datasets
        max_iter=1000,       # Maximum number of iterations for convergence
        class_weight=None,   # No weighting applied to classes
        random_state=42      # Ensures reproducible results
    )

    # Return the configured but untrained model
    return model