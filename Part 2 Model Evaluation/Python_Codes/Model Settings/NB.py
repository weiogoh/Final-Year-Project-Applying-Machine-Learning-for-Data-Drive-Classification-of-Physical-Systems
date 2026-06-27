from sklearn.naive_bayes import GaussianNB

def create_model():
    """
    Creates and returns a Gaussian Naive Bayes model.

    Gaussian Naive Bayes is a supervised learning algorithm based on
    Bayes' theorem. It assumes that features follow a Gaussian (normal)
    distribution and is commonly used for classification tasks.

    Returns:
        GaussianNB: An untrained Naive Bayes classifier
    """

    # Initialize Gaussian Naive Bayes classifier
    model = GaussianNB()

    # Return the configured but untrained model
    return model