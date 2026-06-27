from sklearn.ensemble import RandomForestClassifier

def create_model():
    """
    Creates and returns a Random Forest Classifier model.

    Random Forest is an ensemble learning method that builds multiple
    decision trees and combines their outputs to improve accuracy and
    reduce overfitting.

    Returns:
        RandomForestClassifier: An untrained random forest model
    """

    # Initialize Random Forest classifier
    model = RandomForestClassifier(
        n_estimators=100,  # Number of decision trees in the forest
        random_state=42    # Ensures reproducible results
    )

    # Return the configured but untrained model
    return model