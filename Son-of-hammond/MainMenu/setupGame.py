import pygame 

class gameSetup:
    def __init__(self, screen, clock):
        self.screen = screen
        self.clock = clock
        
    def loop(self):
        run_game = True
        
        while run_game is True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                     run_game = False
                     
            self.screen.fill((255,0,0))
            pygame.display.flip()
            self.clock.tick(30)
