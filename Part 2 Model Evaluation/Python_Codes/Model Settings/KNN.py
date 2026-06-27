from sklearn.neighbors import KNeighborsClassifier

def create_model():
    """
    Creates and returns a K-Nearest Neighbors (KNN) classifier model.

    KNN is a supervised learning algorithm that classifies a data point
    based on the majority class of its nearest neighbors in the feature space.

    Returns:
        KNeighborsClassifier: An untrained KNN model
    """

    # Initialize K-Nearest Neighbors classifier
    model = KNeighborsClassifier(
        n_neighbors=25,     # Number of nearest neighbors to consider for voting
        metric="minkowski", # Distance metric used (general form of Euclidean/Manhattan)
        p=2                 # p=2 means Euclidean distance
    )

    # Return the configured but untrained model
    return model