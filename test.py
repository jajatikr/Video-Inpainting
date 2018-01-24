# Auto-encoder testing code

import numpy as np
from keras.models import Model
from keras.layers import Input, Conv3D, MaxPooling3D, UpSampling3D
from keras.callbacks import TensorBoard
import matplotlib.pyplot as plt
import h5py
from dataset.disp_fig import disp_fig
import random

input_vid = Input(shape=(8, 152, 152, 1))

# Encoder
x = Conv3D(5, (3, 3, 3), activation='relu', padding='same')(input_vid)
x = MaxPooling3D((2, 2, 2), padding='same')(x)
x = Conv3D(5, (3, 3, 3), activation='relu', padding='same')(x)
encoded = MaxPooling3D((2, 2, 2), padding='same')(x)

# Video Encoded

# Decoder
x = Conv3D(5, (3, 3, 3), activation='relu', padding='same')(encoded)
x = UpSampling3D((2, 2, 2))(x)
x = Conv3D(5, (3, 3, 3), activation='relu', padding='same')(x)
x = UpSampling3D((2, 2, 2))(x)
decoded = Conv3D(1, (3, 3, 3), activation='sigmoid', padding='same')(x)

autoencoder = Model(input_vid, decoded)
autoencoder.compile(optimizer='adam', loss='mean_squared_error')

# Print autoencoder details
autoencoder.summary()

# Load model weights
autoencoder.load_weights('autoencoder_weights.h5')

# Get any 50th video to test
with h5py.File('./X_train/49.h5', 'r') as hf:
    X_test = hf['49'][:]

# Get decoded video frames from autoencoder
decoded_imgs = autoencoder.predict(X_test)

# Display source and decoded video frames
disp = disp_fig(X_test)
disp.figure()

disp = disp_fig(decoded_imgs)
disp.figure()

plt.show()
