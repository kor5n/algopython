#Создай собственный Шутер!
from pygame import *
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
run = True
clock = time.Clock()
window = display.set_mode((700, 500))
display.set_caption("Шутер")
background = transform.scale(image.load("galaxy.jpg"), (700, 500))
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, height, width, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y)) 
        self.rect = self.image.get_rect()
        self.rect.x = height
        self.rect.y = width
        
    def show(self):
        
class Player(GameSprite):
    
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.x != 700:
            self.x += 5
        if key_pressed[K_RIGHT] and self.x != 0:
            self.x -= 5
player = Player( "rocket.png", 100, 100)

while run != False:
    
    window.blit(background, (0, 0))
    player.show()
    for e in event.get:
        if e.typer == QUIT:
            run = False
    display.update()
clock.tick(60)