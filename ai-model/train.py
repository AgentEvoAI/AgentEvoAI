from model import create_model
import tensorflow as tf

model = create_model()
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
# Add training dataset and train
