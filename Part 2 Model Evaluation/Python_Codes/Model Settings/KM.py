from sklearn.cluster import KMeans

def create_model():
    """
    Creates and returns a K-Means clustering model.

    K-Means is an unsupervised learning algorithm used to group data
    into clusters based on similarity (distance between points).

    Returns:
        KMeans: An untrained K-Means clustering model
    """

    # Initialize K-Means clustering model
    model = KMeans(
        n_clusters=2,     # Number of clusters to form
        random_state=42   # Ensures reproducible cluster assignments
    )

    # Return the configured but untrained model
    return model