import pygame


pygame.init()
size = x, y = 800, 600


def load_img(path):



class Entity(pygame.sprite.Sprite):
    def __init__(self, coords, path, *group):
        super().__init__(*group)
        self.image = load_img(path)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = coords

