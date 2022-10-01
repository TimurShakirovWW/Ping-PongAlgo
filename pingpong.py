from pygame import *
from random import randint

win_width = 500
window = display.set_mode((700, win_width))
display.set_caption("PingPong")

background = transform.scale(image.load("FON.jpg"), (700, 500))

clock = time.Clock()
fps = 30
clock.tick(fps)
game = True
finish = False
no = 1
randnum = randint(0,1)
speed_x = 2
speed_y = 2
font.init()
font = font.SysFont("Arial", 43)
lose1 = font.render("Игрок 1 - ЛУЗЕР", True, (175, 0, 0))
lose2 = font.render("Игрок 2 - ЛУЗЕР", True, (175, 0, 0))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_y, player_x,size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self): 
        if keys[K_DOWN] and self.rect.y < 320:
            self.rect.y += self.speed
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
class PlayerSec(GameSprite):
    def update(self): 
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 320:
            self.rect.y += self.speed

class Ball(GameSprite):
    def update(self):
        #if randnum == 1 and no == 1:
            #self.rect.x -= self.speed
            #no = no - 1
        #if randnum == 0 and no == 1:
            #self.rect.x += self.speed
            #no = no - 1
        ball.rect.x += speed_x
        ball.rect.y += speed_y

raketka1 = Player("raketka12.png", 200, 50, 45, 180, 4)
raketka2 = PlayerSec("raketka13.png", 150, 600, 45, 180, 4)
ball = Ball("ballalgo.png", 350, 300, 45, 45, 1)


while game != False:
    for e in event.get():
        if e.type == QUIT:
            game = False  
    if finish != True:
        keys = key.get_pressed()
        window.blit(background, (0, 0))
        raketka1.update() 
        raketka1.reset()
        raketka2.update() 
        raketka2.reset()
        ball.update()
        ball.reset() 
        
        if sprite.collide_rect(raketka1, ball):
            speed_x *= -1
        if sprite.collide_rect(raketka2, ball):
            speed_x *= -1
        if ball.rect.y > win_width - 50 or ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (250, 250))
        if ball.rect.x > 700:
            finish = True
            window.blit(lose2, (250, 250))

    display.update()