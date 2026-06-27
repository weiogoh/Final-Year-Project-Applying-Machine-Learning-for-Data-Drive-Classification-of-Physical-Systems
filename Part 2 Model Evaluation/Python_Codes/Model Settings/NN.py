from sklearn.neural_network import MLPClassifier

def create_model():
    """
    Creates and returns a Multi-Layer Perceptron (MLP) classifier model.

    MLPClassifier is a type of artificial neural network used for
    supervised learning tasks such as classification. It learns complex
    non-linear relationships using multiple hidden layers.

    Returns:
        MLPClassifier: An untrained neural network model
    """

    # Initialize the MLP classifier (feedforward neural network)
    model = MLPClassifier(
        hidden_layer_sizes=(64, 32),  # Two hidden layers: 64 neurons then 32 neurons
        activation="relu",            # ReLU activation function for non-linearity
        solver="adam",                # Adam optimizer for efficient training
        max_iter=2000,                # Maximum training iterations for convergence
        random_state=42               # Ensures reproducible results
    )

    # Return the configured but untrained model
    return model