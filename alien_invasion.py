import sys
import pygame
from settings import Settings

class Alien_invasion:
    """class for managing the game on the whole"""
    def __init__(self) :
        """initilizae the game and create resources"""
        pygame.init()
        self.clock = pygame.time.Clock()
        
        pygame.display.set_caption("Aliens invade the Earth!")
        self.settings = Settings()
        #self.screen = pygame.display.set_mode((1200,800))
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
    
    def run_game(self):
        """main loop"""
        while True:
            """response to movement of the mouse and keyboard"""   
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # redraw the background every loop
            self.screen.fill(self.settings.bg_color)
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    ai = Alien_invasion()
    ai.run_game()