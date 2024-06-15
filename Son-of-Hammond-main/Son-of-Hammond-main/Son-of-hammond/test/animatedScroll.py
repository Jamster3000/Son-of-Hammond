import pygame
import sys

pygame.init()

# Define display dimensions
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

# Load spritesheet
spritesheet = pygame.image.load('images/spriteSheet/scroll.png')
sheet_width, sheet_height = spritesheet.get_size()

# Define frame dimensions and count
frame_width = sheet_width // 37  # Assuming 8 frames in the spritesheet
frame_height = sheet_height
frame_count = 37  # Adjust this according to your spritesheet

# Scale factor for resizing the frames
scale_factor = 0.5  # Adjust as needed

# Extract frames from spritesheet and scale them
frames = []
for i in range(frame_count):
    frame_x = i * frame_width
    frame_y = 0
    frame = spritesheet.subsurface(pygame.Rect(frame_x, frame_y, frame_width, frame_height))
    frame = pygame.transform.scale(frame, (int(frame_width * scale_factor), int(frame_height * scale_factor)))
    frames.append(frame)

# Define animation parameters
frame_index = 0
animation_speed = 60  # Adjust speed as needed (lower is faster)

# Main game loop
running = True
while running:
    screen.fill((255, 255, 255))  # Fill screen with white (change as needed)

    # Draw current frame
    screen.blit(frames[frame_index], (100, 100))  # Adjust position as needed

    # Update frame index for next iteration
    frame_index += 1
    if frame_index >= frame_count:
        frame_index = frame_count - 1  # Stop on the last frame

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    clock.tick(animation_speed)

pygame.quit()
sys.exit()
