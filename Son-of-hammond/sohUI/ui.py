from configparser import InterpolationMissingOptionError
import pygame
import pygame.locals
import pyperclip
import os

working_dir = os.path.dirname(os.path.abspath(__file__))

class Button:
    def __init__(self, x, y, width, height, color=None, 
                 image=working_dir + '\\images\\button.png', 
                 text="", text_color=(0,0,0), font_size=12, 
                 font_path=None, padding=10):
        self.rect = pygame.Rect(x, y, width, height)
        self.original_rect = self.rect.copy()
        self.color = color
        self.text = text
        self.text_color = text_color
        self.active = True
        self.padding = padding
        self.alpha = 255
        self.fade_in_speed = 0
        self.use_fade = False
        self.hovered = False
        
        # Font loading
        if font_path:
            full_font_path = os.path.join(working_dir, font_path)
        else:
            full_font_path = os.path.join(working_dir, 'font', 'PixelifySans-VariableFont_wght.ttf')
        
        try:
            self.font = pygame.font.Font(full_font_path, font_size)
        except pygame.error:
            self.font = pygame.font.Font(None, font_size)
        
        # Image loading
        if image:
            try:
                self.original_image = pygame.image.load(image).convert_alpha()
                self.image = self.original_image.copy()
            except pygame.error:
                self.original_image = None
                self.image = None
        else:
            self.original_image = None
            self.image = None

    def fade_appear(self, fade_in_speed=8):
        self.alpha = 0
        self.fade_in_speed = fade_in_speed
        self.use_fade = True

    def update_fade(self):
        if self.use_fade and self.alpha < 255:
            self.alpha += self.fade_in_speed
            if self.alpha > 255:
                self.alpha = 255
            if self.image:
                self.image = self.original_image.copy()
                self.image.set_alpha(self.alpha)

    def wrap_text(self, text, font, max_width):
        words = text.split(' ')
        lines = []
        current_line = ""
        
        for word in words:
            # If a single word is too long, split it
            while font.size(word)[0] > max_width:
                split_index = len(word)
                while font.size(word[:split_index])[0] > max_width:
                    split_index -= 1
                lines.append(word[:split_index])
                word = word[split_index:]
            
            test_line = current_line + word + " "
            if font.size(test_line)[0] <= max_width:
                current_line = test_line
            else:
                if current_line:
                    lines.append(current_line.strip())
                current_line = word + " "
        
        if current_line:
            lines.append(current_line.strip())
        
        return lines

    def draw(self, surface):
        # Create a temporary surface for the button content
        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        
        if self.image: 
            scaled_image = pygame.transform.smoothscale(self.original_image, (self.rect.width, self.rect.height))
            button_surface.blit(scaled_image, (0, 0))
        elif self.color:
            button_surface.fill((*self.color, 255))
        
        if self.text:
            available_width = self.rect.width - 2 * self.padding
            wrapped_lines = self.wrap_text(self.text, self.font, available_width)
            line_height = self.font.get_linesize()
            total_text_height = line_height * len(wrapped_lines)
            
            y_offset = (self.rect.height - total_text_height) // 2
            
            for line in wrapped_lines:
                text_surface = self.font.render(line, True, self.text_color)
                text_rect = text_surface.get_rect(center=(self.rect.width // 2, y_offset + line_height // 2))
                button_surface.blit(text_surface, text_rect)
                y_offset += line_height
        
        # Apply alpha to the entire button surface only if using fade effect
        if self.use_fade:
            button_surface.set_alpha(self.alpha)
        
        # Blit the button surface onto the main surface
        surface.blit(button_surface, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)

    def activate(self):
        self.active = True
    
    def deactivate(self):
        self.active = False
        
    def update(self, mouse_pos):
        self.hovered = self.rect.collidepoint(mouse_pos)
        if self.hovered:
            self.enlarge()
        else:
            self.shrink()

    def enlarge(self):
        target_width = self.original_rect.width + 12
        target_height = self.original_rect.height +  7
        self.rect.size = (target_width, target_height)
        self.rect.center = self.original_rect.center

    def shrink(self):
        self.rect.size = self.original_rect.size
        self.rect.center = self.original_rect.center
            
    def handle_event(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.enlarge()
        else:
            self.shrink()

class Label:
    def __init__(self, x, y, text_color=(0,0,0), text="", 
                 font_size=12, font_path=None, width=None):
        self.text_color = text_color
        self.text = text
        self.font_size = font_size
        self.alpha = 255
        self.fade_in_speed = 0
        self.use_fade = False
        self.width = width
        self.x = x
        self.y = y
        
        if font_path:
            full_font_path = os.path.join(working_dir, font_path)
        else:
            full_font_path = os.path.join(working_dir, 'font', 'PixelifySans-VariableFont_wght.ttf')
            
        try:
            self.font = pygame.font.Font(full_font_path, font_size)
        except pygame.error:
            self.font = pygame.font.Font(None, font_size)

    def fade_appear(self, fade_in_speed=8):
        self.alpha = 0
        self.fade_in_speed = fade_in_speed
        self.use_fade = True
        
    def update_fade(self):
        if self.use_fade and self.alpha < 255:
            self.alpha += self.fade_in_speed
            if self.alpha > 255:
                self.alpha = 255

    def wrap_text(self, text, font, max_width):
        words = text.split()
        lines = []
        current_line = []

        for word in words:
            word_width, _ = font.size(word)
            if word_width > max_width:
                # If a single word is too long, split it
                for char in word:
                    current_line.append(char)
                    line_width, _ = font.size(' '.join(current_line))
                    if line_width > max_width:
                        lines.append(' '.join(current_line[:-1]))
                        current_line = [current_line[-1]]
            else:
                test_line = current_line + [word]
                line_width, _ = font.size(' '.join(test_line))
                if line_width <= max_width:
                    current_line = test_line
                else:
                    lines.append(' '.join(current_line))
                    current_line = [word]

        if current_line:
            lines.append(' '.join(current_line))

        return lines

    def draw(self, surface):
        if self.width:
            wrapped_lines = self.wrap_text(self.text, self.font, self.width)
            line_height = self.font.get_linesize()
            y_offset = self.y
            
            for line in wrapped_lines:
                text_surface = self.font.render(line, True, self.text_color)
                text_surface.set_alpha(self.alpha)  # Set the alpha for fade effect
                surface.blit(text_surface, (self.x, y_offset))
                y_offset += line_height
        else:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_surface.set_alpha(self.alpha)  # Set the alpha for fade effect
            surface.blit(text_surface, (self.x, self.y))
            
class InputBox:
    def __init__(self, x, y, width, height, font_size=12, 
                 text_color=(0, 0, 0), bg_color=(217, 160, 102), 
                 font_path=None, max_length=2000, 
                 border_color=(109, 80, 51), border_radius=10, 
                 border_width=2, multi_line=False, placeholder='', 
                 placeholder_color=(140, 80, 60)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = bg_color
        self.border_color = border_color
        self.text_color = text_color
        self.font_size = font_size
        self.text = ""
        self.active = False
        self.alpha = 255
        self.fade_in_speed = 0
        self.use_fade = False
        self.scroll_offset = 0
        self.selection_start = None
        self.selection_end = None
        self.dragging = False
        self.last_click_time = 0
        self.click_count = 0
        self.key_repeat_counters = {}
        self.last_key_time = 0
        self.key_repeat_delay = 500 # milliseconds
        self.key_repeat_interval = 150 # milliseconds
        self.border_radius = border_radius
        self.border_width = border_width
        self.multi_line = multi_line
        self.scroll_offset_x = 0
        self.scroll_offset_y = 0
        self.placeholder = placeholder
        self.placeholder_color = placeholder_color
        self.focus = False

        if font_path:
            full_font_path = os.path.join(working_dir, font_path)
        else:
            full_font_path = os.path.join(working_dir, 'font', 'PixelifySans-VariableFont_wght.ttf')

        try:
            self.font = pygame.font.Font(full_font_path, font_size)
        except pygame.error:
            self.font = pygame.font.Font(None, font_size)
            
        self.line_height = self.font.get_linesize()
        self.visible_lines = self.rect.height // self.line_height
        self.cursor_visible = True
        self.cursor_timer = 0
        self.cursor_position = len(self.text)
        self.max_length = max_length
        self.selected_text = ''
        self.selection_start = None
        self.selection_end = None

    def should_show_placeholder(self):
        return len(self.text) == 0 and not self.active

    def fade_appear(self, fade_in_speed=8):
        self.alpha = 0
        self.fade_in_speed = fade_in_speed
        self.use_fade = True

    def update_fade(self):
        if self.use_fade and self.alpha < 255:
            self.alpha += self.fade_in_speed
            if self.alpha > 255:
                self.alpha = 255

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.focus = True
                x = event.pos[0] - self.rect.x - 5
                y = event.pos[1] - self.rect.y
                self.cursor_position = self.get_cursor_position_from_mouse(x, y)
            
                if event.button == 1:  # Left mouse button
                    current_time = pygame.time.get_ticks()
                    if current_time - self.last_click_time < 400:  # 400ms for double-click
                        self.click_count += 1
                    else:
                        self.click_count = 1
                    self.last_click_time = current_time

                    if self.click_count == 1:
                        if not (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                            self.clear_selection()
                        self.selection_start = self.cursor_position
                        self.selection_end = self.cursor_position
                    elif self.click_count == 2:
                        self.select_word_at_cursor()
                    elif self.click_count == 3:
                        self.select_all()
            else:
                self.active = False
                self.focus = False
                self.clear_selection()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            if event.button == 1:  # Left mouse button
                self.selection_end = self.cursor_position

        elif event.type == pygame.MOUSEMOTION:
            if event.buttons[0]:  # Left mouse button
                x = event.pos[0] - self.rect.x - 5 + self.scroll_offset
                self.cursor_position = self.get_cursor_position_from_mouse(x, 0)
                self.selection_end = self.cursor_position

        elif event.type == pygame.KEYDOWN:
            if self.focus:
                key_press = self.handle_key_press(event)
                self.key_repeat_counters[event.key] = 0
                
                if key_press == False:
                    return key_press

        elif event.type == pygame.KEYUP:
            if event.key in self.key_repeat_counters:
                del self.key_repeat_counters[event.key]
                
        return self.focus

    def handle_key_press(self, event):
        if not self.focus:
            return False
        
        try:
            ctrl_pressed = pygame.key.get_mods() & pygame.KMOD_CTRL
            shift_pressed = pygame.key.get_mods() & pygame.KMOD_SHIFT

            if event.key in (pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN):
                self.move_cursor(event.key, ctrl_pressed, shift_pressed)
            elif event.key == pygame.K_BACKSPACE and self.active:
                self.handle_backspace(ctrl_pressed)
            elif event.key == pygame.K_DELETE and self.active:
                self.handle_delete()
            elif event.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                if self.multi_line:
                    self.insert_character('\n')
                else:
                    self.active = False
                    self.focus = False
                    return self.active
            elif ctrl_pressed:
                if event.key == pygame.K_a:
                    self.select_all()
                elif event.key == pygame.K_c:
                    self.copy()
                elif event.key == pygame.K_x:
                    self.cut()
                elif event.key == pygame.K_v:
                    self.paste()
            elif not ctrl_pressed and event.unicode:
                self.insert_character(event.unicode)

            self.adjust_scroll_offset()
            self.last_key_time = pygame.time.get_ticks()
            return True
        except AttributeError:
            return False


    def handle_key_hold(self):
        keys = pygame.key.get_pressed()
        current_time = pygame.time.get_ticks()
        if current_time - self.last_key_time > self.key_repeat_delay:
            if keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]:
                self.move_cursor(pygame.K_LEFT if keys[pygame.K_LEFT] else pygame.K_RIGHT,
                                 pygame.key.get_mods() & pygame.KMOD_CTRL,
                                 pygame.key.get_mods() & pygame.KMOD_SHIFT)
            if keys[pygame.K_BACKSPACE]:
                self.handle_backspace(pygame.key.get_mods() & pygame.KMOD_CTRL)
            if keys[pygame.K_DELETE]:
                self.handle_delete()
            self.last_key_time = current_time - self.key_repeat_interval
                
    def move_cursor(self, direction, ctrl_pressed, shift_pressed):
        old_position = self.cursor_position
        lines = self.text.split('\n')
        current_line_index = self.text[:self.cursor_position].count('\n')
        current_line = lines[current_line_index]
        current_line_start = sum(len(l) + 1 for l in lines[:current_line_index])
        current_line_cursor = self.cursor_position - current_line_start

        if direction == pygame.K_LEFT:
            if ctrl_pressed:
                self.cursor_position = self.find_previous_word()
            elif self.cursor_position > 0:
                self.cursor_position -= 1
        elif direction == pygame.K_RIGHT:
            if ctrl_pressed:
                self.cursor_position = self.find_next_word()
            elif self.cursor_position < len(self.text):
                self.cursor_position += 1
        elif direction == pygame.K_UP and current_line_index > 0:
            prev_line = lines[current_line_index - 1]
            new_line_cursor = min(current_line_cursor, len(prev_line))
            self.cursor_position = current_line_start - len(prev_line) - 1 + new_line_cursor
        elif direction == pygame.K_DOWN and current_line_index < len(lines) - 1:
            next_line = lines[current_line_index + 1]
            new_line_cursor = min(current_line_cursor, len(next_line))
            self.cursor_position = current_line_start + len(current_line) + 1 + new_line_cursor
            
        if shift_pressed:
            if self.selection_start is None:
                self.selection_start = old_position
            self.selection_end = self.cursor_position
        elif not ctrl_pressed:
            self.clear_selection()
            
        self.adjust_scroll_offset()

    def find_previous_word(self):
        for i in range(self.cursor_position - 1, -1, -1):
            if i == 0 or (not self.text[i-1].isalnum() and self.text[i].isalnum()):
                return i
        return 0

    def find_next_word(self):
        for i in range(self.cursor_position + 1, len(self.text)):
            if i == len(self.text) - 1 or (not self.text[i].isalnum() and self.text[i+1].isalnum()):
                return i + 1
        return len(self.text)

    def select_word_at_cursor(self):
        if not self.text[self.cursor_position].isalnum():
            self.selection_start = self.cursor_position
            self.selection_end = self.cursor_position + 1
        else:
            start = self.cursor_position
            while start > 0 and self.text[start - 1].isalnum():
                start -= 1
            end = self.cursor_position
            while end < len(self.text) and self.text[end].isalnum():
                end += 1
            self.selection_start = start
            self.selection_end = end
        self.cursor_position = self.selection_end
    
    def handle_backspace(self, ctrl_pressed):
        if self.has_selection():
            self.delete_selection()
        elif ctrl_pressed and self.cursor_position > 0:
            new_position = self.find_previous_word()
            self.text = self.text[:new_position] + self.text[self.cursor_position:]
            self.cursor_position = new_position
        elif self.cursor_position > 0:
            self.text = self.text[:self.cursor_position - 1] + self.text[self.cursor_position:]
            self.cursor_position -= 1
            
    def has_selection(self):
        return self.selection_start is not None and self.selection_end is not None and self.selection_start != self.selection_end

    def clear_selection(self):
        self.selection_start = None
        self.selection_end = None

    def delete_selection(self):
        if self.has_selection():
            start, end = min(self.selection_start, self.selection_end), max(self.selection_start, self.selection_end)
            self.text = self.text[:start] + self.text[end:]
            self.cursor_position = start
            self.clear_selection()

    def handle_delete(self):
        if self.has_selection():
            self.delete_selection()
        elif self.cursor_position < len(self.text):
            self.text = self.text[:self.cursor_position] + self.text[self.cursor_position + 1:]

    def insert_character(self, char):
        if self.has_selection():
            self.delete_selection()
        if len(self.text) < self.max_length:
            self.text = self.text[:self.cursor_position] + char + self.text[self.cursor_position:]
            self.cursor_position += 1

    def get_cursor_position_from_mouse(self, x, y):
        lines = self.text.split('\n')
        target_line = min(max(0, (y - self.rect.y) // self.line_height + self.scroll_offset_y), len(lines) - 1)
    
        line_start = sum(len(l) + 1 for l in lines[:target_line])
        line_text = lines[target_line]
    
        for i, char in enumerate(line_text):
            if self.font.size(line_text[:i+1])[0] > x + self.scroll_offset_x:
                return line_start + i
    
        return line_start + len(line_text)
    
    def update_selection(self):
        if self.selection_start is not None and self.selection_end is not None:
            self.selection_start = min(self.selection_start, self.selection_end)
            self.selection_end = max(self.selection_start, self.selection_end)

    def backspace(self):
        if self.cursor_position > 0:
            self.text = self.text[:self.cursor_position - 1] + self.text[self.cursor_position:]
            self.cursor_position -= 1

    def delete_word_before_cursor(self):   
        if self.cursor_position > 0:
            # Find the start of the current word
            start = self.cursor_position
            # First, skip any spaces immediately before the cursor
            while start > 0 and self.text[start - 1].isspace():
                start -= 1
            # Then, continue skipping non-space characters
            while start > 0 and not self.text[start - 1].isspace():
                start -= 1
                
            # Delete from start to cursor_position
            self.text = self.text[:start] + self.text[self.cursor_position:]
            self.cursor_position = start
        
    def select_all(self):
        self.selection_start = 0
        self.selection_end = len(self.text)
        self.cursor_position = len(self.text)

    def copy(self):
        if self.has_selection():
            start, end = min(self.selection_start, self.selection_end), max(self.selection_start, self.selection_end)
            pyperclip.copy(self.text[start:end])

    def cut(self):
        if self.has_selection():
            self.copy()
            self.delete_selection()

    def paste(self):
        clipboard_text = pyperclip.paste()
        if self.selection_start is not None and self.selection_end is not None:
            self.text = self.text[:self.selection_start] + clipboard_text + self.text[self.selection_end:]
            self.cursor_position = self.selection_start + len(clipboard_text)
            self.selection_start = None
            self.selection_end = None
        else:
            self.text = self.text[:self.cursor_position] + clipboard_text + self.text[self.cursor_position:]
            self.cursor_position += len(clipboard_text)

    def adjust_scroll_offset(self):
        if not self.multi_line:
            text_width = self.font.size(self.text[:self.cursor_position])[0]
            if text_width > self.rect.width - 10:
                self.scroll_offset_x = max(0, text_width - (self.rect.width - 10))
            else:
                self.scroll_offset_x = 0
        else:
            lines = self.text.split('\n')
            cursor_line = self.text[:self.cursor_position].count('\n')
        
            # Vertical scrolling
            if cursor_line >= self.scroll_offset_y + self.visible_lines:
                self.scroll_offset_y = cursor_line - self.visible_lines + 1
            elif cursor_line < self.scroll_offset_y:
                self.scroll_offset_y = cursor_line
        
            # Horizontal scrolling
            current_line = lines[cursor_line]
            cursor_x = self.font.size(current_line[:self.cursor_position - sum(len(l) + 1 for l in lines[:cursor_line])])[0]
            if cursor_x > self.rect.width - 10:
                self.scroll_offset_x = max(0, cursor_x - (self.rect.width - 10))
            else:
                self.scroll_offset_x = 0

        # Ensure scroll offsets are not negative
        self.scroll_offset_x = max(0, self.scroll_offset_x)
        self.scroll_offset_y = max(0, self.scroll_offset_y)

    def update(self):
        self.cursor_timer += 1
        if self.cursor_timer >= 10:
            self.cursor_timer = 0
            self.cursor_visible = not self.cursor_visible

        self.update_fade()
        
        if self.focus:
            current_time = pygame.time.get_ticks()
            keys = pygame.key.get_pressed()
        
            for key in [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_BACKSPACE, pygame.K_DELETE]:
                if keys[key]:
                    if key not in self.key_repeat_counters:
                        self.key_repeat_counters[key] = 0
                
                    if self.key_repeat_counters[key] == 0 or current_time - self.key_repeat_counters[key] > self.key_repeat_interval:
                        self.handle_key_press(pygame.event.Event(pygame.KEYDOWN, {'key': key}))
                        self.key_repeat_counters[key] = current_time
                elif key in self.key_repeat_counters:
                    del self.key_repeat_counters[key]

    def draw(self, surface):
        # Draw the input box with rounded corners
        box_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(box_surface, (*self.color, self.alpha), box_surface.get_rect(), border_radius=self.border_radius)
        pygame.draw.rect(box_surface, self.border_color, box_surface.get_rect(), self.border_width, border_radius=self.border_radius)
        surface.blit(box_surface, self.rect.topleft)

        # Create a mask for the text
        text_mask = pygame.Surface((self.rect.width - 10, self.rect.height), pygame.SRCALPHA)
        text_mask.fill((0, 0, 0, 0))

        # Draw the highlighted area
        if self.has_selection():
            start, end = min(self.selection_start, self.selection_end), max(self.selection_start, self.selection_end)
            highlight_start = self.font.size(self.text[:start])[0] - self.scroll_offset_x
            highlight_end = self.font.size(self.text[:end])[0] - self.scroll_offset_x
            highlight_rect = pygame.Rect(highlight_start, 0, highlight_end - highlight_start, self.rect.height)
            pygame.draw.rect(text_mask, (0, 120, 215, 128), highlight_rect)  # Light blue highlight

        # Render the text with scroll offset or placeholder
        if self.should_show_placeholder():
            placeholder_surface = self.font.render(self.placeholder, True, self.placeholder_color)
            placeholder_surface.set_alpha(self.alpha)
            text_mask.blit(placeholder_surface, (0, 0))
        elif self.multi_line:
            lines = self.text.split('\n')
            y_offset = -self.scroll_offset_y * self.line_height
            for i, line in enumerate(lines):
                if self.scroll_offset_y <= i < self.scroll_offset_y + self.visible_lines:
                    if 0 <= y_offset < self.rect.height:
                        text_surface = self.font.render(line, True, self.text_color)
                        text_surface.set_alpha(self.alpha)
                        text_mask.blit(text_surface, (-self.scroll_offset_x, y_offset))
                    y_offset += self.line_height
        else:
            text_surface = self.font.render(self.text, True, self.text_color)
            text_surface.set_alpha(self.alpha)
            text_mask.blit(text_surface, (-self.scroll_offset_x, 0))
    
        clip_rect = pygame.Rect(0, 0, self.rect.width - 10, self.rect.height - 10)
        text_mask.set_clip(clip_rect)
    
        # Blit the masked text onto the box surface
        surface.blit(text_mask, (self.rect.x + 5, self.rect.y + 5), area=clip_rect)

        # Draw the cursor
        if self.active and self.cursor_visible and not self.should_show_placeholder():
            if self.multi_line:
                lines = self.text[:self.cursor_position].split('\n')
                cursor_y = self.rect.y + 5 + (len(lines) - 1 - self.scroll_offset_y) * self.line_height
                cursor_x = self.rect.x + 5 + self.font.size(lines[-1])[0] - self.scroll_offset_x
            else:
                cursor_x = self.rect.x + 5 + self.font.size(self.text[:self.cursor_position])[0] - self.scroll_offset_x
                cursor_y = self.rect.y + 5
    
            if 0 <= cursor_y - self.rect.y < self.rect.height:
                cursor_height = self.font.get_height()
                pygame.draw.line(surface, self.text_color, (cursor_x, cursor_y), (cursor_x, cursor_y + cursor_height))  

class ListBox:
    def __init__(self, x, y, width, height, items, font_size=12,
                 text_color=(0,0,0), bg_color=(255, 255, 255), selected_color=(0, 120, 215),
                 border_color=(100, 100, 100), hover_color=(230, 230, 230), font_path=None,
                 multi_select=False, show_scrollbar=True, item_click_callback=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.items = items
        self.text_color = text_color
        self.bg_color = bg_color
        self.selected_color = selected_color
        self.border_color = border_color
        self.hover_color = hover_color
        self.font_size = font_size
        self.multi_select = multi_select
        self.selected_indices = set()
        self.scroll_offset = 0
        self.item_height = font_size + 8
        self.hover_index = -1
        self.dragging_scrollbar = False
        self.show_scrollbar = show_scrollbar
        self.item_click_callback = item_click_callback
        self.drag_start_y = 0
        self.focus = False
        
        if font_path:
            self.font = pygame.font.Font(font_path, font_size)
        else:
            self.font = pygame.font.Font(None, font_size)
        
        self.scrollbar_width = 15
        self.visible_items = self.rect.height // self.item_height
    
    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos) or self.scrollbar_rect.collidepoint(event.pos):
                self.focus = True
                if self.scrollbar_rect.collidepoint(event.pos):
                    self.dragging_scrollbar = True
                    self.drag_start_y = event.pos[1]
                    self.drag_start_scroll = self.scroll_offset
                elif self.rect.collidepoint(event.pos):
                    y = event.pos[1] - self.rect.y + self.scroll_offset
                    index = y // self.item_height
                    if index < len(self.items):
                        if self.multi_select:
                            if index in self.selected_indices:
                                self.selected_indices.remove(index)
                            else:
                                self.selected_indices.add(index)
                        else:
                            self.selected_indices = {index}
                    
                        if self.item_click_callback:
                            self.item_click_callback(index, self.items[index])
                return True
            else:
                self.focus = False
            
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            self.dragging_scrollbar = False
        
        elif event.type == pygame.MOUSEMOTION:
            if self.dragging_scrollbar:
                drag_distance = event.pos[1] - self.drag_start_y
                scroll_ratio = drag_distance / (self.rect.height - self.get_scrollbar_height())
                total_scroll_height = max(0, (len(self.items) * self.item_height) - self.rect.height)
                self.scroll_offset = int(self.drag_start_scroll + scroll_ratio * total_scroll_height)
                self.clamp_scroll_offset()
            elif self.rect.collidepoint(event.pos):
                y = event.pos[1] - self.rect.y + self.scroll_offset
                self.hover_index = y // self.item_height
            else:
                self.hover_index = -1
            
        elif event.type == pygame.MOUSEWHEEL:
            if self.rect.collidepoint(pygame.mouse.get_pos()):
                self.scroll_offset -= event.y * self.item_height
                self.clamp_scroll_offset()
                return True
        
        elif self.focus and event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.selected_indices:
                    selected_index = max(self.selected_indices)
                    if self.item_click_callback:
                        self.item_click_callback(selected_index, self.items[selected_index])
                return True
            elif event.key == pygame.K_UP:
                self.move_selection(-1)
                return True
            elif event.key == pygame.K_DOWN:
                self.move_selection(1)
                return True
            elif event.key == pygame.K_SPACE:
                if self.multi_select and self.selected_indices:
                    last_selected = max(self.selected_indices)
                    if last_selected in self.selected_indices:
                        self.selected_indices.remove(last_selected)
                    else:
                        self.selected_indices.add(last_selected)
                return True
    
        return False
    
    def move_selection(self, direction):
        if not self.selected_indices:
            new_index = 0 if direction > 0 else len(self.items) - 1
        else:
            last_selected = max(self.selected_indices)
            new_index = (last_selected + direction) % len(self.items)
        
        if self.multi_select and pygame.key.get_mods() & pygame.KMOD_SHIFT:
            self.selected_indices.add(new_index)
        else:
            self.selected_indices = {new_index}
        
        self.ensure_selection_visible(new_index)
    
    def ensure_selection_visible(self, index):
        if index * self.item_height < self.scroll_offset:
            self.scroll_offset = index * self.item_height
        elif (index + 1) * self.item_height > self.scroll_offset + self.rect.height:
            self.scroll_offset = (index + 1) * self.item_height - self.rect.height
        self.clamp_scroll_offset()
    
    def clamp_scroll_offset(self):
        max_offset = max(0, (len(self.items) * self.item_height) - self.rect.height)
        self.scroll_offset = max(0, min(self.scroll_offset, max_offset))
    
    def update_scroll_from_mouse(self, mouse_y):
        available_scroll = max(0, (len(self.items) * self.item_height) - self.rect.height)
        scrollbar_height = self.get_scrollbar_height()
        scrollable_height = self.rect.height - scrollbar_height
        scroll_pos = (mouse_y - self.rect.y - scrollbar_height / 2) / scrollable_height
        self.scroll_offset = int(scroll_pos * available_scroll)
        self.clamp_scroll_offset()
    
    def get_scrollbar_height(self):
        visible_ratio = min(1, self.visible_items / len(self.items))
        return max(20, int(self.rect.height * visible_ratio))
    
    def draw(self, surface):
        # Draw background and border
        pygame.draw.rect(surface, self.bg_color, self.rect)
        pygame.draw.rect(surface, self.border_color, self.rect, 2)
        
        # Draw items
        y_offset = -self.scroll_offset
        for index, item in enumerate(self.items):
            item_rect = pygame.Rect(self.rect.x, self.rect.y + y_offset, self.rect.width - self.scrollbar_width, self.item_height)
            if item_rect.y + self.item_height > self.rect.y and item_rect.y < self.rect.y + self.rect.height:
                if index in self.selected_indices:
                    pygame.draw.rect(surface, self.selected_color, item_rect)
                elif index == self.hover_index:
                    pygame.draw.rect(surface, self.hover_color, item_rect)
                
                text_surface = self.font.render(item, True, self.text_color)
                surface.blit(text_surface, (self.rect.x + 5, self.rect.y + y_offset + 4))
            
            y_offset += self.item_height
        
        if self.show_scrollbar:
            # Draw scrollbar
            self.scrollbar_rect = pygame.Rect(
                self.rect.right - self.scrollbar_width,
                self.rect.y,
                self.scrollbar_width,
                self.rect.height
            )
            pygame.draw.rect(surface, (200, 200, 200), self.scrollbar_rect)
        
            scrollbar_height = self.get_scrollbar_height()
            scrollbar_pos = int(self.scroll_offset / ((len(self.items) * self.item_height) - self.rect.height) * (self.rect.height - scrollbar_height))
            scrollbar_handle_rect = pygame.Rect(
                self.rect.right - self.scrollbar_width,
                self.rect.y + scrollbar_pos,
                self.scrollbar_width,
                scrollbar_height
            )
            pygame.draw.rect(surface, (150, 150, 150), scrollbar_handle_rect)
    
    def get_selected_items(self):
        return [self.items[i] for i in self.selected_indices]

class Slider:
    pass

class CheckBox:
    pass

class Switch:
    pass

class Menu:
    pass

class DropDown:
    pass

class RadioButton:
    pass

class SearchBar:
    pass

class ProgressBar:
    pass

class Icon:
    pass

class ToolTip:
    pass
##################
### CONTAINERS ###
##################

class Panel:
    '''
    This panel can be used as a container or just as a decoration piece to a menu for example.
    
    The panel will have an overflow option that allows a horizontal and/or vertical scrollbar to appear if
    any other elements are placed outside of the X or Y boundaries of the panel
    '''
    pass

class Grid:
    '''
    The grid is used as a container to organise all given elements into a suitable row and column like structure.
    
    The grid will have an overflow option that allows a horizontal and/or vertical scrollbar to appear if any other 
    elements are placed outside of the X or Y boundaries of the grid.
    '''
    pass

class TabPages:
    '''
    Tab pages will be a group of panels that can be switched between by using a tabs. 
    
    The TabPages will have an overflow option that allows a horizontal and/or vertical scrollbar to appear if any other
    elements are placed outside of the X or Y boundaries of the grid
    '''
    pass

#######################################################
### Other things that aren't a UI element initatlly ###
#######################################################

class Notification:
    pass

class ModelWindow:
    '''
    This is basically a pop up window telling the user information about something.
    The user will not be able to continue interacting with the game until they have confirmed this window.
    '''
    pass

class RightClickMenu:
    pass

#all the UI elements should have tab functionality to highlight or make it obvious which element has been selected
#all elements should be fully usable by just the keyboard or just the mouse.
#all elements shouldn't be able to be interactable if there's another element above it

#need to make the ListBox look more like the rest of the UI elements
#Need the actual scrollbar to be dragable
#the scrollbar (if using scroll) can be scrolled from any point within the window, this isn't wanted, it's only if the mouse is within the boudnaries of the elements
#Make the scrollbar more effiecnt to contain more items.
#Have an option for each individual item in a list to have an icon with it. This should be as a list of lists or as a dictionary of a list, where not all items has to have icons.
#optional scrollbar apperance.
#make the scrollbar look nicer rather than just plan flat
#need to add an event listener to each item to see if they are left clicked or highlighted and return key pressed