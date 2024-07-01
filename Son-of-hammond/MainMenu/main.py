import pygame
import sys
import random
import time
import setupGame#setupGame being the file that is in charge of setting up the actual game or choosing the same game to continue from.

class Main_menu():
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        
        self.screen_width = 800
        self.screen_height = 600
        
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption("Son of Hammond")
        
        self.load_image_sprites()
        self.load_audio()
        
    def load_image_sprites(self):
        '''
        All images, background, and sprites are loaded here
        '''
        
        self.background = pygame.image.load('images/skyBlue.jpg')
        self.mountain = pygame.image.load('images/mountain.png')
        self.play_button = pygame.image.load('images/playButton.png').convert_alpha()
        self.settings_button = pygame.image.load('images/settingsButton.png').convert_alpha()
        self.quit_button = pygame.image.load('images/quitButton.png').convert_alpha()
        
        #background image
        self.background = pygame.transform.scale(self.background, (self.screen_width, self.screen_height))
        
        # Other sprites here
        self.mountain_scaled = pygame.transform.scale(self.mountain, (self.screen_width, self.screen_height))
        self.play_button_scaled = pygame.transform.scale(self.play_button, (self.play_button.get_width()/3, self.play_button.get_height()/3))
        self.settings_button_scaled = pygame.transform.scale(self.settings_button, (self.settings_button.get_width()/3, self.settings_button.get_height()/3))
        self.quit_button_scaled = pygame.transform.scale(self.quit_button, (self.quit_button.get_width()/3, self.quit_button.get_height()/3))
        

    def render_static_images(self):
        '''
        This is where all sprites are set scaled correctly and
        sprites are positioned and blit onto screen
        '''

        #position the sprites here
        self.mountain_rect = self.mountain_scaled.get_rect(bottomleft=(-325, self.screen_height+125))

        self.screen.blit(self.background, (0,0))
        self.screen.blit(self.mountain_scaled, self.mountain_rect)
        
    def render_other_images(self):
        '''
        This is for images that are interactable or moving
        '''
        pass
    
    def load_audio(self):
        pygame.mixer.music.load("audio/hidden crown.mp3")

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

class fadeInButton:
    def __init__(self, image, pos):
        self.image = image
        self.original_image = image
        self.rect = self.image.get_rect(topleft=pos)
        self.alpha = 0
        self.image.set_alpha(self.alpha)
        self.fade_in_speed = 8
        self.hovered = False
        self.hover_scale_factor = 1.2
        
    def update(self):
        if self.alpha < 255:
            self.alpha += self.fade_in_speed
            if self.alpha > 255:
                self.alpha = 255
            self.image.set_alpha(self.alpha)
            
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def mouse_hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            if not self.hovered:
                self.hovered = True
                self.image = pygame.transform.scale(self.original_image, 
                    (int(self.original_image.get_width() * self.hover_scale_factor), 
                     int(self.original_image.get_height() * self.hover_scale_factor)))
                self.rect = self.image.get_rect(center=self.rect.center)
        else:
            if self.hovered:
                self.hovered = False
                self.image = self.original_image
                self.rect = self.image.get_rect(center=self.rect.center)
    
    def key_bind(self, sizing):
        if sizing == "enlarge":
            self.image = pygame.transform.scale(self.original_image, 
                (int(self.original_image.get_width() * self.hover_scale_factor), 
                    int(self.original_image.get_height() * self.hover_scale_factor)))
            self.rect = self.image.get_rect(center=self.rect.center)
        elif sizing == "reduce":
            self.image = self.original_image
            self.rect = self.image.get_rect(center=self.rect.center)

def create_pixel_surface(width, height, pixel_size):
    surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pixel_list = [(x, y) for x in range(0, width, pixel_size) for y in range(0, height, pixel_size)]
    random.shuffle(pixel_list)
    return surface, pixel_list

def background_audio_fade_in(ms):
    pygame.mixer.music.play(loops=0, fade_ms=ms)
    pygame.mixer.music.set_volume(0.09)
    
def background_audio_fade_out_repeat(fade_out_duration, fade_in_duration, wait_duration):
    pygame.mixer.music.fadeout(fade_out_duration)
    pygame.time.wait(fade_out_duration + wait_duration)
    background_audio_fade_in(fade_in_duration)

def background_audio_fade_out(ms):
    pygame.mixer.music.fadeout(ms)
    pygame.time.wait(ms)

main_menu = Main_menu()
cloud = Cloud((main_menu.screen_width, 100), -0.15, main_menu.screen_width, main_menu.screen_height)
scroll = Scroll(main_menu.screen)

#play audio
background_audio_fade_in(2000)

#sprites that fade into existance
play_button = fadeInButton(main_menu.play_button_scaled, (350, 275))
settings_button = fadeInButton(main_menu.settings_button_scaled, (350, 360))
quit_button = fadeInButton(main_menu.quit_button_scaled, (350, 445))

pixel_size = 10
overlay_surface, pixel_list = create_pixel_surface(main_menu.screen_width, main_menu.screen_height, pixel_size)
pixels_per_frame = 100
pixelation_index = 0
pixelation_timer = 0
pixelation_interval = 0.01  # Time between updates in seconds
max_alpha = 255
current_alpha = 0
alpha_increase = 100  # Increase this value to make the effect faster

run_main_menu = True
quit_game = False
play_game = False
clock = pygame.time.Clock()

while run_main_menu is True:
    current_time = time.time()
    
    for event in pygame.event.get():
        mouse_pos = pygame.mouse.get_pos()
        
        if event.type == pygame.QUIT:
            run_main_menu = False
        
        if event.type == pygame.KEYDOWN:
            #validation for p, s, q keys
            if event.key == pygame.K_p:
                play_button.key_bind("enlarge")
            if event.key == pygame.K_s:
                settings_button.key_bind("enlarge")
            if event.key == pygame.K_q:
                quit_button.key_bind("enlarge")
                
        if event.type == pygame.KEYUP:
            #validation for p, s, q keys
            if event.key == pygame.K_p:
                play_button.key_bind("reduce")
                play_game = True
            if event.key == pygame.K_s:
                settings_button.key_bind("reduce")
            if event.key == pygame.K_q:
                quit_button.key_bind("reduce")
                quit_game = True
                
        if event.type == pygame.MOUSEBUTTONUP:
            if play_button.rect.collidepoint(mouse_pos):
                print("play button pressed")
                play_game = True
            if quit_button.rect.collidepoint(mouse_pos):
                print("quit button pressed")
                quit_game = True
              
    if not pygame.mixer.music.get_busy():
        background_audio_fade_out_repeat(2000, 2000, 1750)
    
    #update cloud movement
    cloud.update()        

    #draw all sprites that are static and non-moving or non-interactive
    main_menu.render_static_images()
    
    #render sprites
    cloud.draw(main_menu.screen)

    # Update and render scroll animation
    scroll.update()
    scroll.draw()

    #Make the play, settings, and quit button only appear when the scroll has moved enough.
    if scroll.frame_index >= 4:
        play_button.update()
        play_button.draw(main_menu.screen)
    
    if scroll.frame_index >= 18:
        settings_button.update()
        settings_button.draw(main_menu.screen)
        
    if scroll.frame_index >= 28:
       quit_button.update()
       quit_button.draw(main_menu.screen)
       
    #constantly check if mouse is hovering over play, settings or quit button
    play_button.mouse_hover()
    settings_button.mouse_hover()
    quit_button.mouse_hover()

    if quit_game or play_game:
        if pixelation_index < len(pixel_list) or current_alpha < max_alpha:
            if current_time - pixelation_timer >= pixelation_interval:
                if pixelation_index < len(pixel_list):
                    end_index = min(pixelation_index + pixels_per_frame, len(pixel_list))
                    for x, y in pixel_list[pixelation_index:end_index]:
                        pygame.draw.rect(overlay_surface, (0, 0, 0, current_alpha), (x, y, pixel_size, pixel_size))
                    pixelation_index = end_index
                
                current_alpha = min(current_alpha + alpha_increase, max_alpha)
                overlay_surface.set_alpha(current_alpha)
                
                pixelation_timer = current_time
                
                main_menu.screen.blit(overlay_surface, (0, 0))
                pygame.display.flip()
        else:
            main_menu.screen.fill((0,0,0))
            run_main_menu = False

    pygame.display.flip()
    clock.tick(30)

if play_game:
    background_audio_fade_out(2000)
    setup = setupGame.gameSetup(main_menu.screen, clock)
    setup.loop()
else:
    background_audio_fade_out(2000)
    pygame.quit()
    sys.exit()


####things to do
#use the UI for buttons and such
#replace the mountain with something better
#Possible add another cloud
#Add a title to the screen
#add the splash text   