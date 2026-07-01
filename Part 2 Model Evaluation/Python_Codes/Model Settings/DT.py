from sklearn.tree import DecisionTreeClassifier

def create_model():
    """
    Creates and returns a Decision Tree Classifier model.

    The model is configured with default settings except for:
    - random_state: ensures reproducible results
      (same output every time the model is trained with the same data)

    Returns:
        DecisionTreeClassifier: An untrained decision tree model
    """
    
    # Initialize the Decision Tree Classifier with reproducible behavior
    model = DecisionTreeClassifier(
        max_depth=None,          # No limit on tree depth (fully grown tree)
        min_samples_split=2,     # Minimum samples required to split a node
        min_samples_leaf=1,      # Minimum samples required at a leaf node
        random_state=42          # Ensures consistent results across runs
    )

    # Return the configured but untrained model
    return model