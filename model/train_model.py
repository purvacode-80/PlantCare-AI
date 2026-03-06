# train_model.py
# Activity 3.3 - Train the Model
# Uses MobileNetV2 Transfer Learning on New Plant Diseases Dataset

import os
import sys
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.optimizers import Adam

# Import team's model builder
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from model_builder import build_model

# ── Settings ──────────────────────────────────────────────────────
DATASET_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../dataset")
MODEL_SAVE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../plant_disease_model.h5")

IMAGE_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 10
LEARNING_RATE = 0.0001
NUM_CLASSES = 38

# ── 1. Load Data ───────────────────────────────────────────────────
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True,
    shear_range=0.2
)
val_datagen = ImageDataGenerator(rescale=1./255)

train_gen = train_datagen.flow_from_directory(
    os.path.join(DATASET_PATH, "train"),
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)
val_gen = val_datagen.flow_from_directory(
    os.path.join(DATASET_PATH, "valid"),
    target_size=IMAGE_SIZE,
    batch_size=BATCH_SIZE,
    class_mode="categorical"
)

NUM_CLASSES = len(train_gen.class_indices)
print(f"\n✅ Classes found: {NUM_CLASSES}\n")

# ── 2. Build Model (using team's model_builder) ────────────────────
model = build_model(
    input_shape=(224, 224, 3),
    num_classes=NUM_CLASSES,
    fine_tune_layers=30
)

# ── 3. Compile ─────────────────────────────────────────────────────
model.compile(
    optimizer=Adam(learning_rate=LEARNING_RATE),
    loss="categorical_crossentropy",
    metrics=["accuracy"]
)
model.summary()

# ── 4. Train ───────────────────────────────────────────────────────
print("\n🚀 Starting training...\n")
history = model.fit(
    train_gen,
    epochs=EPOCHS,
    validation_data=val_gen
)

# ── 5. Save ────────────────────────────────────────────────────────
model.save(MODEL_SAVE_PATH)
print(f"\n✅ Model saved as: {MODEL_SAVE_PATH}")
print("Training complete!")