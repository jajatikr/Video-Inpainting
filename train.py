# Auto encoder training code

import numpy as np
from keras.models import Model
from keras.layers import Input, Conv3D, MaxPooling3D, UpSampling3D
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

# Train for 50 epochs
nb_epoch = 50
for e in range(nb_epoch):
    print "\n\n\nEpoch ------- %d \n\n\n" % e
    
    # Get a list of random sequence for 49 videos to train
    # Test on 50th video

    rand_list = random.sample(range(49),49)

    for i in rand_list:
        X_name = './X_train/' + str(i) + '.h5'
        y_name = './y_train/' + str(i) + '.h5'
        
        with h5py.File(X_name, 'r') as hf:
            X_train = hf[str(i)][:]

        with h5py.File(y_name, 'r') as hf:
            y_train = hf[str(i)][:]

        # Run autoencoder
        autoencoder.fit(X_train, 
        	            y_train,
        	            verbose=1, 
        	            epochs=1,
        	            batch_size=2, 
        	            shuffle=False,
        	            callbacks=None)


# Save model weights
autoencoder.save_weights('autoencoder_weights.h5') 
