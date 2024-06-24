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
        self.mountain = pygame.image.load('images/mountain.png')
        

    def render_static_images(self):
        '''
        This is where all sprites are set scaled correctly and
        sprites are positioned and blit onto screen
        '''
        
        #background image
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        
        # Other sprites here
        self.mountain_scaled = pygame.transform.scale(self.mountain, (self.screen_width, self.screen_height))

        #position the sprites here
        self.mountain_rect = self.mountain_scaled.get_rect(bottomleft=(-325, self.screen_height+125))

        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.mountain_scaled, self.mountain_rect)
        
    def render_other_images(self):
        '''
        This is for images that are interactable or moving
        '''
        pass

class Cloud(Main_menu):
    def __init__(self, start_pos, speed, width, height):
        self.image = pygame.image.load('images/Cloud.png')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()/3.75, self.image.get_height()/3.75))
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

class Scroll(Main_menu):
    def __init__(self, screen):
        self.scroll_sprite_sheet = pygame.image.load('images/spriteSheet/scroll.png')
        self.sheet_width, self.sheet_height = self.scroll_sprite_sheet.get_size()
        self.frame_counter = 37
        self.frame_width = self.sheet_width // self.frame_counter
        self.frame_height = self.sheet_height
        self.scale_factor = 0.55
        self.screen = screen

        self.frames = []  # List to store scaled frames
        self.load_frames()

        self.frame_index = 0
        self.animation_speed = 7  # Adjust speed(lower is faster)
        self.current_frame = self.frames[self.frame_index]

        self.is_animating = True

    def load_frames(self):
        for i in range(self.frame_counter):
            frame_x = i * self.frame_width
            frame_y = 0
            frame = self.scroll_sprite_sheet.subsurface(pygame.Rect(frame_x, frame_y, self.frame_width, self.frame_height))
            frame = pygame.transform.scale(frame, (int(self.frame_width * self.scale_factor), int(self.frame_height * self.scale_factor)))
            self.frames.append(frame)

    def update(self):
        if self.is_animating:
            self.frame_index += 1
            if self.frame_index >= self.frame_counter:
                self.frame_index = self.frame_counter - 1
                self.is_animating = False
            self.current_frame = self.frames[self.frame_index]

    def draw(self):
        self.screen.blit(self.current_frame, ((self.screen.get_width()//2)-(self.frame_width//4), 225))
        


main_menu = Main_menu()
cloud = Cloud((main_menu.screen_width, 100), -0.15, main_menu.screen_width, main_menu.screen_height)
scroll = Scroll(main_menu.screen)

run_main_menu = True
clock = pygame.time.Clock()

while run_main_menu is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_main_menu = False
       
    #update cloud movement
    cloud.update()        

    #draw all sprites that are static and non-moving or non-interactive
    main_menu.render_static_images()
    
    #render sprites
    cloud.draw(main_menu.screen)

    # Update and render scroll animation
    scroll.update()
    scroll.draw()
    
    pygame.display.flip()
    clock.tick(30)
    
pygame.quit()
sys.exit()


