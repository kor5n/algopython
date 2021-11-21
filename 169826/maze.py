#создай игру "Лабиринт"!
from pygame import *
from pygame.sprite import *
x1 = 595
x2 = 500
mixer.init()
mixer.music.load("jungles.ogg")
boost = 10

ww = 700
wh = 500
game_over = False
window = display.set_mode((ww, wh))
background = transform.scale(image.load("background.jpg"), (ww, wh))
mixer.music.play()
class GameSprite(Sprite):
   def __init__(self, x, y, image):
       super().__init__()
       self.image = image
       self.x = x
       self.y = y
   def create(self):
       self.sprite = transform.scale(image.load(self.image), (100, 100))
   def show(self):
       window.blit(self.sprite,(self.x, self.y))
class Player(GameSprite):
    def __init__(self, x, y, image):
        super().__init__(x=x, y=y, image=image)
    def update(self):
        if keys_pressed[K_UP] and self.y > 5:
            self.y -= 1
        elif self.y == 5: 
            self.x = 100
            self.y = 250
        if keys_pressed[K_DOWN] and self.x > 5:
            self.y += 1
        elif self.x == 5: 
            self.x = 100
            self.y = 250
        if keys_pressed[K_LEFT] and self.x < 595:
            self.x -= 1
        elif self.x == 595: 
            self.x = 100
            self.y = 250
        if keys_pressed[K_RIGHT] and self.y < 395:
            self.x += 1
        elif self.y == 395: 
            self.x = 100
            self.y = 250
      
class Enemy(GameSprite):
    def __init__(self, x, y, image):
        super().__init__(x=x, y=y, image=image)
    def update(self):
        if self.x == 595:
            for i in range(145):
                self.x += 1
        if self.x == 450:
            for i in range(145):
                self.x -= 1
class Wall(Sprite):
    def __init__(self, width, length, color1, color2, color3):
        super().__init__()
        self.width = width
        self.lenght = length
        self.color1 = color1
        self.color2 = color2 
        self.color3 = color3
    def draw(self, x, y):
        self.image = Surface((self.width, self.lenght))
        self.image.fill((self.color1, self.color2, self.color3))
        self.rect = self.image.get_rect() 
        window.blit(self.image, (x, y))
        #draw.rect(self.image, "blue", self.rect)
clock = time.Clock()

wall = Wall(200, 10, 0, 0, 0 )
enemy = Enemy(450, 250, "cyborg.png")
player = Player(100, 250, "hero.png")
treasure = GameSprite(500, 350, "treasure.png")
enemy.create()
player.create()
treasure.create()
while game_over == False:
    keys_pressed = key.get_pressed()
    window.blit(background, (0, 0))
    enemy.show()
    player.show()
    treasure.show()
    player.update()
    wall.draw(100, 100)
    #enemy.update
    display.update()
    for e in event.get():
       if e.type == QUIT:
           game_over = True
clock.tick(60)
  
 

