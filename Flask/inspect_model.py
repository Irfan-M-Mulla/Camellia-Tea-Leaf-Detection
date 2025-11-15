from tensorflow.keras.models import load_model

model_path = "VGG16-Tea-Leaves-disease-model.h5"
model = load_model(model_path)

# Print model architecture
model.summary()
