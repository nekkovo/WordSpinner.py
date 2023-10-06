# import pygame and sys modules
import pygame
import sys


class Character:
    def __int__(self, image, position):
        self.image = image
        self.rectangle = image.get_rect()
        self.mask = pygame.mask.from_surface(image)


def main():
    # Set up pygame
    pygame.init()

    # width, height = (700, 700)
    # size = (width, height)
    # screen = pygame.display(size)
    screen = pygame.display.set_mode((700, 700))  # double braces because this is a tuple parameters

    # load images with pygame method
    # get mouse and draw the image we loaded
    # we need both image and a rectangle which is the same size as our image
    kirby = pygame.image.load("kirby.png").convert_alpha()
    kirby_rectangle = kirby.get_rect()
    kirby_mask =

    # Draw the kirby
    # Using a while loop or making a variable
    # while True:  or
    is_playing = True
    while is_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_playing = False  # so the loop will break

        # Making the events
        # 0. moving the object
        kirby_rectangle.move_ip(2, 1)  # inside the braces are speed
        # 1. clear the screen
        screen.fill((0, 0, 0))  # RGB color, this is black, and a tuple with double braces
        # 2. draw my object
        screen.blit(kirby, kirby_rectangle)  # blit the image, means the bit lock transfer
        # 3. display it on the window
        pygame.display.update()  # update the screen
        # 4. adjust the speed
        pygame.time.wait(100)

    # Once the game loop is done, close the window and quit
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
