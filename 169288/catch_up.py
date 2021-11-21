from pygame import *

#создай окно игры
window = display.set_mode((700, 500))
display.set_caption("Догонялки")
#задай фон сцены
background = transform.scale(image.load("background.png"), (700, 500))
#создай 2 спрайта и размести их на сцене
sprite1 = transform.scale(image.load("sprite1.png"), (100, 100))
sprite2 = transform.scale(image.load("sprite2.png"), (100, 100))

#обработай событие «клик по кнопке "Закрыть окно"»
x1 = 
y1 = 
x2 = 100
x2 = 100
boost = 10

game = True
clock = time.Clock()
while game:
    window.blit(background, (0, 0))
    window.blit(sprite1, (x1, y1))
    window.blit(sprite2), (x2, y2)
    keys_pressed = key.get_pressed

    for e in event.get:
        if e.type == QUIT:
            game = False
    
    #sprite1
    if keys_pressed[K_UP]:
        y1 += boost
    if keys_pressed[K_DOWN]:
        y1 -= boost
    if keys_pressed[K_LEFT]:
        x1 -= boost
    if keys_pressed[K_RIGHT]:
        x1 += boost
    #behind background sprite1
    if x1 == 595:
        x1 -= 5
    if y1 == 395:
        y1 -= 5
    if y1 <= 0:
        y1 += 5
    if x1 <= 0:
        x1 += 5
    #sprite2
    if keys_pressed[K_w]:
        y2 += boost
    if keys_pressed[K_s]:
        y2 -= boost
    if keys_pressed[K_a]:
        x2 -= boost
    if keys_pressed[K_d]:
        x2 += boost
    #behind background sprite2
    if x2 >= 595:
        x2 -= 5
    if y2 >= 395:
        y2 -= 5
    if y2 <= 0:
        y2 += 5
    if x2 <= 0:
        x2 += 5
    display.update()
    clock.tick(60)