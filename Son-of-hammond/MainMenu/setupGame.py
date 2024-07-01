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
            

'''
THis is to setup the game before the player starts.
======================================================

The following things will be part of the setup
- difficulty
- Character avatar creator/picker
- fullscreen tick box(whether the window is full screen or not)
- enable/disable tutorial
- name game
- start button
'''
