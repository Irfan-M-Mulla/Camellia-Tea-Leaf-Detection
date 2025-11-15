from tensorflow.keras.models import load_model

model = load_model("VGG16-Tea-Leaves-disease-model.h5")
model.summary()
