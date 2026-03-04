import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import GlobalAveragePooling2D, Dense, Dropout
from tensorflow.keras.models import Model


def build_model(input_shape=(224, 224, 3), num_classes=38, fine_tune_layers=30):
    """
    Builds a transfer learning model using MobileNetV2.

    Parameters:
    input_shape : tuple
        Image input size.
    num_classes : int
        Number of disease classes.
    fine_tune_layers : int
        Number of last layers to unfreeze for fine tuning.

    Returns:
    model : tensorflow.keras Model
    """

    # Load pretrained MobileNetV2
    base_model = MobileNetV2(
        input_shape=input_shape,
        include_top=False,
        weights="imagenet"
    )

    # Freeze initial layers
    for layer in base_model.layers[:-fine_tune_layers]:
        layer.trainable = False

    # Custom classification head
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dropout(0.35)(x)

    x = Dense(256, activation="relu")(x)
    x = Dropout(0.25)(x)

    outputs = Dense(num_classes, activation="softmax")(x)

    model = Model(inputs=base_model.input, outputs=outputs)

    return model