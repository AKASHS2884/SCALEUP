import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report

# Load drug effectiveness data
data_file = "drug_effectiveness_data.csv"
drug_df = pd.read_csv(data_file)

# Extract actual and predicted classifications
actual_classes = drug_df["True_Class"]
predicted_classes = drug_df["Predicted_Class"]

# Generate confusion matrix
conf_matrix = confusion_matrix(actual_classes, predicted_classes, labels=["Effective", "Not Effective"])

# Display evaluation metrics
print(f"Confusion Matrix:\n{conf_matrix}\n")
print(f"Accuracy Score: {accuracy_score(actual_classes, predicted_classes):.2f}\n")
print(f"Classification Report:\n{classification_report(actual_classes, predicted_classes)}\n")

# Function to plot confusion matrix
def display_confusion_matrix(matrix, title="Confusion Matrix"):
    """Generates a heatmap visualization of the confusion matrix."""
    plt.figure(figsize=(6, 4))
    sns.heatmap(matrix, annot=True, fmt="d", cmap="Blues",
                xticklabels=["Effective", "Not Effective"],
                yticklabels=["Effective", "Not Effective"])
    plt.xlabel("Predicted Label")
    plt.ylabel("Actual Label")
    plt.title(title)
    plt.show()

# Visualize the confusion matrix
display_confusion_matrix(conf_matrix)
