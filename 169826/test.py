from pygame import *
from pygame.sprite import *
window = display.set_mode((700, 500))
class newsprite(Sprite):
    def __init__(self, hello):
        self.hello = hello