import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

# Load dataset
data_path = "/content/drug_discovery_data.csv"

drug_data = pd.read_csv(data_path)

# Extract actual outcomes and predictions
actual_labels = drug_data["Actual_Label"]
predictions_traditional = drug_data["Traditional_Prediction"]
predictions_ai_quantum = drug_data["AI_Quantum_Prediction"]

# Compute confusion matrices for both models
conf_matrix_traditional = confusion_matrix(actual_labels, predictions_traditional)
conf_matrix_ai_quantum = confusion_matrix(actual_labels, predictions_ai_quantum)

# Function to visualize confusion matrix
def visualize_confusion_matrix(conf_matrix, method_name):
    """Generate a heatmap representation of the confusion matrix."""
    plt.figure(figsize=(5, 4))
    sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Failed Drug", "Successful Drug"],
                yticklabels=["Failed Drug", "Successful Drug"])
    plt.xlabel("Predicted Outcome")
    plt.ylabel("Actual Outcome")
    plt.title(f"Confusion Matrix: {method_name}")
    plt.show()

# Display the confusion matrices
visualize_confusion_matrix(conf_matrix_traditional, "Traditional Drug Identification")
visualize_confusion_matrix(conf_matrix_ai_quantum, "AI-Quantum Model")
