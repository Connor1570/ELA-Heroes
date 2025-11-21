import pygame
import math
from settings import COLOR_ACCENT, COLOR_HIGHLIGHT, COLOR_TEXT, FONT_MAIN, FONT_SIZE_TEXT

class Button:
    def __init__(self, x, y, width, height, text, action=None, color=COLOR_ACCENT, hover_color=COLOR_HIGHLIGHT):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.color = color
        self.hover_color = hover_color
        self.is_hovered = False
        self.font = pygame.font.SysFont(FONT_MAIN, FONT_SIZE_TEXT)

    def draw(self, surface):
        color = self.hover_color if self.is_hovered else self.color
        
        # Draw button with rounded corners
        pygame.draw.rect(surface, color, self.rect, border_radius=15)
        pygame.draw.rect(surface, COLOR_TEXT, self.rect, width=2, border_radius=15) # Border

        # Text rendering
        text_surf = self.font.render(self.text, True, COLOR_TEXT)
        
        # Scale text if too wide
        if text_surf.get_width() > self.rect.width - 20: # 20px padding
            scale = (self.rect.width - 20) / text_surf.get_width()
            new_width = int(text_surf.get_width() * scale)
            new_height = int(text_surf.get_height() * scale)
            text_surf = pygame.transform.smoothscale(text_surf, (new_width, new_height))
            
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.is_hovered = self.rect.collidepoint(event.pos)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.is_hovered and event.button == 1:
                if self.action:
                    self.action()
                return True
        return False

class TextLabel:
    def __init__(self, x, y, text, font_size=FONT_SIZE_TEXT, color=COLOR_TEXT, center=False):
        self.font = pygame.font.SysFont(FONT_MAIN, font_size)
        self.text = text
        self.color = color
        self.x = x
        self.y = y
        self.center = center

    def draw(self, surface):
        text_surface = self.font.render(self.text, True, self.color)
        text_rect = text_surface.get_rect(center=(self.x, self.y))
        surface.blit(text_surface, text_rect)
        if self.center:
            rect = text_surface.get_rect(center=(self.x, self.y))
            surface.blit(text_surface, rect)
        else:
            surface.blit(text_surface, (self.x, self.y))

def load_image(path, size=None):
    try:
        image = pygame.image.load(path).convert_alpha()
        if size:
            image = pygame.transform.scale(image, size)
        return image
    except (pygame.error, FileNotFoundError):
        # Return a placeholder surface (red square)
        surf = pygame.Surface(size if size else (100, 100))
        surf.fill((255, 0, 0))
        return surf

class CharacterSprite:
    def __init__(self, image_path, x, y, size=(150, 150)):
        self.original_image = load_image(image_path, size)
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        self.start_y = y
        self.animation_offset = 0
        self.animation_speed = 0.2
        self.is_jumping = False
        self.jump_height = 20
    
    def update(self):
        if self.is_jumping:
            self.animation_offset += self.animation_speed
            # Simple sine wave for a jump (0 to pi)
            if self.animation_offset >= math.pi:
                self.animation_offset = 0
                self.is_jumping = False
                self.rect.centery = self.start_y
            else:
                offset = math.sin(self.animation_offset) * self.jump_height
                self.rect.centery = self.start_y - offset

    def draw(self, surface):
        surface.blit(self.image, self.rect)
    
    def jump(self):
        if not self.is_jumping:
            self.is_jumping = True
            self.animation_offset = 0
