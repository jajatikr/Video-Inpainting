import os
import pygame
import random
import time

SCREEN_LENGTH = 152
SCREEN_WIDTH = 152
num_of_frames = 8

class Rectangle:

    """
    Class to initialise rectangle

    Output: Returns rectangle object
    """

    def __init__(self):
        self.x = 0           # x position
        self.y = 0           # y position
        self.change_x = 0    # dx
        self.change_y = 0    # dy
        self.col = (0, 0, 0)  # color
        self.rect_len = 0    # rectange length
        self.rect_wid = 0    # rectange width


class video(object):

    """
    Class to display and save Pygame video

    Args:
    src_folder, dest_folder: String variables to accept folder containing images and
    folder to save the color video frames

    Output: Saves Pygame generated 8 video frames in dest_folder
    """

    def __init__(self, src_folder, dest_folder, num_vids=1500):
        self.src_dir = src_folder
        self.dest_dir = dest_folder
        self.num_of_vids = num_vids
        
        # Create destination folder if it is absent
        if not os.path.exists(self.dest_dir):
            os.makedirs(self.dest_dir)

    def make_obj(self):

        # Initialize rectangle object
        obj = Rectangle()

        # Starting position of the ball.
        # Object position and check to not initialize it at edge
        obj.x = random.randrange(obj.rect_len, SCREEN_LENGTH - obj.rect_len)
        obj.y = random.randrange(obj.rect_wid, SCREEN_WIDTH - obj.rect_wid)

        # Speed and direction of rectangle object
        obj.change_x = random.choice([-4, 3, 4])
        obj.change_y = random.choice([-4, 3, 4])

        # Color of rectangle object
        obj.col = (random.randint(0, 255),
                   random.randint(0, 255),
                   random.randint(0, 255))

        # Object length and width
        obj.rect_len = random.choice([12, 15])
        obj.rect_wid = random.choice([12, 15])

        return obj

    def create_videos(self):
        # For each image in folder
        for img_num in range(self.num_of_vids):
            
            # Delay for 2 seconds to free resources
            time.sleep(2)

            # Initialize Pygame
            pygame.init()

            # Set the height and width of the screen
            size = [SCREEN_LENGTH, SCREEN_WIDTH]
            screen = pygame.display.set_mode(size)

            # Used to manage how fast the screen updates
            clock = pygame.time.Clock()

            # Set position of background image
            background_position = [0, 0]


            img_name = self.src_dir + str(img_num) + ".jpg"
            img = pygame.image.load(img_name)

            # Load and set up graphics.
            background_image = img.convert()

            # Create 5 rectangles
            obj_list = []
            for i in range(5):
                obj = self.make_obj()
                obj_list.append(obj)

            start_ticks = pygame.time.get_ticks()
            running = True
            count = 0

            # Main Program Loop
            while running:

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False

                # Calculate how many seconds
                seconds = (pygame.time.get_ticks() - start_ticks) / 1000.0

                if seconds > 1:  # if more than 10 seconds close the game
                    running = False

                # Logic
                for obj in obj_list:

                    # Move the rectangle center
                    obj.x += obj.change_x
                    obj.y += obj.change_y

                    # Bounce the ball on edges and change width randomly
                    if obj.x > SCREEN_LENGTH - obj.rect_len or obj.x < obj.rect_len:
                        obj.change_x *= -1
                    if obj.y > SCREEN_WIDTH - obj.rect_wid or obj.y < obj.rect_wid:
                        obj.change_y *= -1
                        obj.rect_wid += random.choice([-2, 2])


                # Set the image as screen background
                screen.blit(background_image, background_position)

                # Draw the balls
                for obj in obj_list:
                    pygame.draw.rect(screen,
                                     obj.col,
                                     [obj.x, obj.y, obj.rect_len, obj.rect_wid])

                filenm = self.dest_dir + str(img_num) + '_' + str(count) + '.jpg'
                pygame.image.save(screen, filenm)
                count += 1

                # Limit to 8 frames per second
                clock.tick(num_of_frames-2)

                # Update the screen new images
                pygame.display.flip()

            # Close and free resources
            print 'Created video: %d/%d' % (img_num + 1, self.num_of_vids)
            pygame.quit()

        # Print created videos status
        print 'Created %d videos\n' % (self.num_of_vids)

if __name__ == '__main__':
    pass 
