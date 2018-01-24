import matplotlib.pyplot as plt
import numpy as np

class disp_fig(object):

    """
    Class to display video frames

    Args:
    Accepts video frames numpy array to display using matplotlib

    Output:
    Displays 8 video frames using matplotlib window
    """

    def __init__(self, arr):
        self.array = arr
        
        # Reshape numpy video array
        self.video = arr.reshape(1,8,152,152)
        
        # Create new matplotlib figure
        plt.figure(figsize=(20, 2))

    def figure(self):
        # Display video frames using 8 subplot
        for i in range(8):
            ax = plt.subplot(1, 8, i+1)
            image = self.video[0][i]
            plt.imshow(image)
            plt.gray()
            ax.get_xaxis().set_visible(False)
            ax.get_yaxis().set_visible(False)

if __name__ == '__main__':
	pass
