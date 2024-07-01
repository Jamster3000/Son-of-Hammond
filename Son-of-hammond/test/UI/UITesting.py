import sys, os
import pygame

current_dir = os.path.dirname(os.path.abspath(__file__)) #gets this file's path
game_dir = os.path.dirname(current_dir) #gets the dir that this file is stored in
sohUI_dir = os.path.abspath(os.path.join(game_dir, '..', 'sohUI'))#goes down two levels to son-of-hammond then gets the path for sohUI
sys.path.append(sohUI_dir)

from ui import Button, Label, InputBox, ListBox, Slider, CheckBox, Switch, Menu, DropDown, RadioButton, SearchBar, ProgressBar, Icon, ToolTip, Panel, Grid, TabPages, Notification, ModelWindow, RightClickMenu

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

def item_click(index, item):
    print(f"Item clicked: {item} at index {index}")

button = Button(50, 50, 200, 100, text="Clicking this will close the test program", font_size=18 ,text_color=(0,0,0))
label = Label(260, 50, text="I have chosen to write my own User Interface for this game because I would have much much much more control over what I can and can't do.", font_size=25, width=500)
input_box = InputBox(50,160,200,40, font_size=20, placeholder="Enter name here", multi_line=True)

import time
start = time.time()
items = [f"Item {i}" for i in range(500)]
list_box = ListBox(50, 210, 200, 300, items, item_click_callback=item_click)
print(time.time()-start)

#fade
#button.fade_appear()
#label.fade_appear()
#input_box.fade_appear()

run = True
while run is True:
    mouse_pos = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
           
        input_box_event_handler = input_box.handle_event(event)
        list_box.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button.rect.collidepoint(mouse_pos):
                run = False
        
        if input_box_event_handler == False:
            print("Enter has beens pressed, input box finished with")
    
    input_box.update()
            
    screen.fill((255, 255, 255))
    
    #UI element handlers
    button.handle_event(mouse_pos)

    #fade
    #button.update_fade()
    #label.update_fade()
    #input_box.update_fade()

    #render
    list_box.draw(screen)
    button.draw(screen)
    label.draw(screen)
    input_box.draw(screen)
    
   
    clock.tick(30)
    pygame.display.flip()

pygame.quit()
sys.exit()
