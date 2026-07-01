from sklearn.svm import SVC

def create_model():
    """
    Creates and returns a Support Vector Machine (SVM) classifier model.

    SVM is a supervised learning algorithm that finds the optimal
    hyperplane to separate classes. The RBF kernel allows it to handle
    non-linear decision boundaries.

    Returns:
        SVC: An untrained SVM classifier model
    """

    # Initialize Support Vector Machine classifier
    model = SVC(
        kernel="rbf",        # Radial Basis Function kernel for non-linear classification
        C=1.0,               # Regularization parameter (controls margin vs classification error)
        gamma="scale",      # Kernel coefficient (automatically scaled based on data)
        probability=False,  # Disable probability estimates (faster training)
        random_state=42     # Ensures reproducible results
    )

    # Return the configured but untrained model
    return model