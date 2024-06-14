import pygame
import sys

class Main_menu():
    def __init__(self):
        pygame.init()
        
        self.screen_width = 800
        self.screen_height = 600
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Son of Hammond")
        
        self.load_image_sprites()
        
    def load_image_sprites(self):
        '''
        All images, background, and sprites are loaded here
        '''
        
        self.background = pygame.image.load('images/skyBlue.jpg')
        self.mainCloud = pygame.image.load('images/Cloud.png')
        

    def renderStaticImages(self):
        '''
        This is where all sprites are set scaled correctly and
        sprites are positioned and blit onto screen
        '''
        
        #background image
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        
        # Other sprites here

        #position the sprites here
        #image1_rect = image1.get_rect(center=(self.screen_width//2, self.screen_height//2))

        self.screen.blit(self.background, (0,0))
        
    def renderOtherImages(self):
        '''
        This is for images that are interactable or moving
        '''
        
        pass

class Cloud(Main_menu):
    def __init__(self, start_pos, speed, width, height):
        self.image = pygame.image.load('images/Cloud.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/4, self.image.get_height()/4))
        self.rect = self.image.get_rect(topleft=start_pos)
        self.speed = speed
        self.screen_width, self.screen_height = width, height
        self.accumulated_movement = 0
        
    def update(self):
        self.accumulated_movement += self.speed
        if abs(self.accumulated_movement) >=1:
            self.rect.x += int(self.accumulated_movement)
            self.accumulated_movement -= int(self.accumulated_movement)
            

        if self.rect.right < 0:
            self.rect.left = self.screen_width
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        


main_menu = Main_menu()
cloud = Cloud((main_menu.screen_width, 100), -0.01, main_menu.screen_width, main_menu.screen_height)

run_main_menu = True
while run_main_menu is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_main_menu = False
       
    #update cloud movement
    cloud.update()        

    #draw all sprites that are static and non-moving or non-interactive
    main_menu.renderStaticImages()
    
    #render sprites
    cloud.draw(main_menu.screen)
    
    pygame.display.flip()
    
pygame.quit()
sys.exit()


