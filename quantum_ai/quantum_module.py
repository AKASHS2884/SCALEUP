import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers, models
import pandas as pd

# Load dataset
dataset_path = "datasetdrug.xlsx"
drug_data = pd.read_excel(dataset_path, sheet_name="Sheet1")

# Quantum Property Input (e.g., Molecular Dimension, Structural Angle)
quantum_input = layers.Input(shape=(94,))  # Adjusted shape to ensure correct input format

# Example: Processing quantum properties
x = layers.Dense(64, activation="relu")(quantum_input)
x = layers.Dense(32, activation="relu")(x)
quantum_model = models.Model(inputs=quantum_input, outputs=x)

# DFT Image Input
image_input = layers.Input(shape=(256, 256, 1))  # Grayscale molecular image

# CNN-based feature extraction for DFT representation
y = layers.Conv2D(32, (3, 3), activation="relu")(image_input)
y = layers.MaxPooling2D((2, 2))(y)
y = layers.Conv2D(64, (3, 3), activation="relu")(y)
y = layers.MaxPooling2D((2, 2))(y)
y = layers.Conv2D(128, (3, 3), activation="relu")(y)
y = layers.Flatten()(y)
y = layers.Dense(128, activation="relu")(y)
image_model = models.Model(inputs=image_input, outputs=y)

# Merging the outputs of quantum model and image model
combined_output = layers.concatenate([quantum_model.output, image_model.output])

# Final prediction layers
z = layers.Dense(64, activation="relu")(combined_output)
z = layers.Dense(32, activation="relu")(z)
output = layers.Dense(1, activation="sigmoid")(z)  # Output: Desired vs. Undesired Drug

# Create the final drug evaluation model
drug_model = models.Model(inputs=[quantum_model.input, image_model.input], outputs=output)

# Compile the model with optimization settings
drug_model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])

# Display model architecture
drug_model.summary()

# Assuming quantum_data, dft_images, and labels are preprocessed datasets
history = drug_model.fit([quantum_data, dft_images], labels, epochs=50, batch_size=32, validation_split=0.2)

# Predict drug properties using new dataset samples
predictions = drug_model.predict([new_quantum_data, new_dft_images])
