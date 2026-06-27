from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def create_model():
    """
    Creates and returns a Linear Discriminant Analysis (LDA) model.

    LDA is a supervised learning algorithm used for classification and
    dimensionality reduction. It finds a linear combination of features
    that best separates different classes.

    Returns:
        LinearDiscriminantAnalysis: An untrained LDA model
    """

    # Initialize LDA classifier with regularization settings
    model = LinearDiscriminantAnalysis(
        solver='lsqr',        # Solver that supports shrinkage
        shrinkage='auto',     # Automatically applies regularization (helps with overfitting)
        priors=None,          # Class priors are learned from data
        n_components=None,    # Number of components (None = min(n_classes - 1, n_features))
        store_covariance=False, # Do not store covariance matrix (saves memory)
        tol=1e-4              # Convergence tolerance for solver
    )

    # Return the configured but untrained model
    return model