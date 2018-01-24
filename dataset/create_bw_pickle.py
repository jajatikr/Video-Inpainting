import numpy as np
import cv2
import h5py
import os

SCREEN_LENGTH = 152
SCREEN_WIDTH = 152
num_of_frames = 8
channels = 1

class create_bw_pickle:

    """
    Class to create video minibatches
    
    Args:
    feature_src_folder
    feature_dest_folder
    label_src_folder
    label_dest_folder
    -- Variables to accept folder names to read video frames and
       save the mini-batches

    Output:
    Saves the black and white video minibatches in provided folder

    """

    def __init__(self,
                 feature_src_folder,
                 feature_dest_folder,
                 label_src_folder,
                 label_dest_folder,
                 num_vids_in_batch=2,
                 num_of_minibatches=2):
        self.fea_src_dir = feature_src_folder
        self.fea_dest_dir = feature_dest_folder
        self.lab_src_dir = label_src_folder
        self.lab_dest_dir = label_dest_folder
        self.num_vid_in_batch = num_vids_in_batch
        self.num_of_minibatches = num_of_minibatches


        # Create destination folders if it is absent
        if not os.path.exists(self.fea_dest_dir):
            os.makedirs(self.fea_dest_dir)

        if not os.path.exists(self.lab_dest_dir):
            os.makedirs(self.lab_dest_dir)

        # Call functions to read video frames and save images
        self.create_feature()
        self.create_label()

    def create_feature(self):
        count = 0
        for minibatch in range(self.num_of_minibatches):
            fea = []
            for i in range(count, self.num_vid_in_batch + count):
                for j in range(num_of_frames):
                    fname = self.fea_src_dir + str(i) + '_' + str(j) + '.jpg'
                    # Read images as grayscale
                    destRGB = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
                    # Normalize and save it in numpy array
                    destRGB = destRGB.astype('float32') / 255.
                    fea.append(destRGB)
            count += self.num_vid_in_batch

            # Resize numpy dimensions according to tensorflow input dimenstions
            fea = np.resize(fea, (self.num_vid_in_batch, num_of_frames, SCREEN_LENGTH, SCREEN_WIDTH, channels))
            
            # Save minibatch
            minibatch_name = self.fea_dest_dir + str(minibatch) + '.h5'
            with h5py.File(minibatch_name, 'w') as hf:
                hf.create_dataset(str(minibatch), data=fea)
            
            # Print status
            print 'Created feature minibatch: %s' % (str(minibatch) + '.h5')
        print '\n'

    def create_label(self):
        count = 0
        for minibatch in range(self.num_of_minibatches):
            lab = []
            for i in range(count, self.num_vid_in_batch + count):
                fname = self.lab_src_dir + str(i) + '.jpg'
                # Read images as grayscale
                destRGB = cv2.imread(fname, cv2.IMREAD_GRAYSCALE)
                # Normalize and save it in numpy array
                destRGB = destRGB.astype('float32') / 255.
                for j in range(num_of_frames):
                    lab.append(destRGB)
            count += self.num_vid_in_batch

            # Resize numpy dimensions according to tensorflow input dimenstions
            lab = np.resize(lab, (self.num_vid_in_batch, num_of_frames, SCREEN_LENGTH, SCREEN_WIDTH, channels))
            
            # Save minibatch
            minibatch_name = self.lab_dest_dir + str(minibatch) + '.h5'
            with h5py.File(minibatch_name, 'w') as hf:
                hf.create_dataset(str(minibatch), data=lab)
            
            # Print status
            print 'Created label minibatch: %s' % (str(minibatch) + '.h5')
        print '\n'

if __name__ == '__main__':
    pass
