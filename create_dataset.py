 # Program to create 50 video dataset
# Change number to create more videos

from dataset.resize import resize
from dataset.video import video
from dataset.create_bw_pickle import create_bw_pickle

# Original images folder
src_img_folder = './src-images/'

# Resized images folder
resized_src_img_folder = './resized_src-images/'

# Video folder
video_folder = './video-images/'

# Pickle folder
features = './X_train/'
labels = './y_train/'

# Instance
img_data = resize(src_folder=src_img_folder,
                  dest_folder=resized_src_img_folder,
                  num_imgs=50) # Total images = 31784

# Resize images
img_data.resize_images()

# Generate video images
# Instance
video_data = video(src_folder=resized_src_img_folder,
                   dest_folder=video_folder,
                   num_vids=50)

# Create video
video_data.create_videos()

# Create minibatch file
# Create 50 minibatches, each minibatch containing 1 video
create_bw_pickle(feature_src_folder=video_folder,
                 feature_dest_folder=features,
                 label_src_folder=resized_src_img_folder,
                 label_dest_folder=labels,
                 num_vids_in_batch=1,
                 num_of_minibatches=50)
