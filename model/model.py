# Load MobileNetV2
base_model = MobileNetV2(
    input_shape=(224,224,3),
    include_top=False,
    weights='imagenet'
)

# Freeze layers
for layer in base_model.layers[:-30]:
    layer.trainable = False

# Architecture
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.35)(x)
x = Dense(256, activation='relu')(x)
x = Dropout(0.25)(x)
outputs = Dense(38, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=outputs)