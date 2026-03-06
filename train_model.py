import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense
from tensorflow.keras.optimizers import Adam

# Generate dummy training data
# heart_rate, temperature, blood_pressure
data = np.random.normal(loc=[80, 37, 120], scale=[10, 0.5, 15], size=(1000,3))

# Normalize data
data = data / np.max(data, axis=0)

# Autoencoder architecture
input_dim = data.shape[1]

input_layer = Input(shape=(input_dim,))
encoded = Dense(8, activation="relu")(input_layer)
encoded = Dense(4, activation="relu")(encoded)

decoded = Dense(8, activation="relu")(encoded)
decoded = Dense(input_dim, activation="sigmoid")(decoded)

autoencoder = Model(inputs=input_layer, outputs=decoded)

autoencoder.compile(
    optimizer=Adam(learning_rate=0.001),
    loss="mse"
)

# Train model
autoencoder.fit(
    data,
    data,
    epochs=30,
    batch_size=32,
    shuffle=True
)

# Save model
autoencoder.save("models/autoencoder_model.h5")

print("Model saved in models/autoencoder_model.h5")
