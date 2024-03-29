# button class
import pygame

class Button():
    def __init__(self, **config):
        # button graphic
        self.image = config['image']
        self.image = pygame.transform.scale(self.image, (config['size'][0], config['size'][1]))
        self.hover_image = config['hover_image']
        self.hover_image = pygame.transform.scale(self.hover_image, (config['size'][0], config['size'][1]))
        # button position
        self.x_pos = config['pos'][0]
        self.y_pos = config['pos'][1]
        # title font
        self.font = config['font']
        # text color
        self.color = config['color']
        # title text
        self.text_input = config['text_input']
        # click effect
        self.click_effect = config['click_effect']
        self.effect_args = config['effect_args']
        # rendered text
        self.text = self.font.render(self.text_input, True, self.color)
        # button bounding box (PyGame Rect)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    # method @display
    # draws the button at the specified 'screen' at the specified 'position'
    def display(self, screen, position):
        if self.isInside(position):
            screen.blit(self.hover_image, self.rect)
        else:
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)

    # method @isInside
    # checks if a point (muose) is inside of the button
    def isInside(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
    
    # invokes the click effect
    def clicked(self):
        self.click_effect(self.effect_args)