"""
LESSON: 5.1 - Sprites
EXERCISE: Code Your Own
"""
import pygame
pygame.init()
import tsk
import random
c = pygame.time.Clock()
window = pygame.display.set_mode([1018, 573])
background = tsk.Sprite("SkyScrolling.jpg", 0, 0)
image_sheet = tsk.ImageSheet("DragonFlying.png", 4, 6)
dragon = tsk.Sprite(image_sheet, 0, 0)
dragon.scale = .2
loop = True
coin1 = tsk.Sprite("Coin.png", 100, 100)
coin2 = tsk.Sprite("Coin.png", 100, 100)
coin3 = tsk.Sprite("Coin.png", 100, 100)
coin4 = tsk.Sprite("Coin.png", 100, 100)
coin5 = tsk.Sprite("Coin.png", 100, 100)
coin6 = tsk.Sprite("Coin.png", 100, 100)
coin7 = tsk.Sprite("Coin.png", 100, 100)
rock1 = tsk.Sprite("BigRock.png", 100, 100)
rock2 = tsk.Sprite("BigRock.png", 100, 100)
rock3 = tsk.Sprite("BigRock.png", 100, 100)
rock4 = tsk.Sprite("BigRock.png", 100, 100)
rock5 = tsk.Sprite("BigRock.png", 100, 100)
rock6 = tsk.Sprite("BigRock.png", 100, 100)
rock7 = tsk.Sprite("BigRock.png", 100, 100)
rock8 = tsk.Sprite("BigRock.png", 100, 100)
rock9 = tsk.Sprite("BigRock.png", 100, 100)
collidable_6 = True
collidable_7 = True
rock2.scale = .2
rock3.scale = .2
rock4.scale = .2
rock5.scale = .2
coin1.scale = .2
coin2.scale = .2
coin3.scale = .2
coin4.scale = .2
rock5.scale = .2
rock6.scale = .2
rock7.scale = .2
rock8.scale = .2
rock9.scale = .2
rock1.scale = .2
coin6.scale = .2
coin7.scale = .2
collidable_5 = True
coin5.scale = .2
inc = 5
count = 1
coins = 0
x = random.randint(0, 50)
y = random.randint(20, 550)
collidable_1 = True
collidable_2 = True
collidable_3 = True
collidable_4 = True
coin1.center_x = dragon.center_x + random.randint(250, 350)
coin1.center_y = random.randint(20, 550)
coin2.center_x = dragon.center_x + random.randint(550, 650)
coin2.center_y = random.randint(20, 550)
coin3.center_x = dragon.center_x + random.randint(850, 950)
coin3.center_y = random.randint(20, 550)
coin4.center_x = dragon.center_x + random.randint(1150, 1250)
coin4.center_y = random.randint(20, 550)
coin5.center_x = dragon.center_x + random.randint(1450, 1550)
coin5.center_y = random.randint(20, 550)
coin6.center_x = dragon.center_x + random.randint(1450, 1550)
coin6.center_y = random.randint(20, 550)
coin7.center_x = dragon.center_x + random.randint(1450, 1550)
coin7.center_y = random.randint(20, 550)
rock1.center_x = dragon.center_x + random.randint(350, 400)
rock1.center_y = random.randint(20, 550)
rock2.center_x = dragon.center_x + random.randint(450, 500)
rock2.center_y = random.randint(20, 550)
rock3.center_x = dragon.center_x + random.randint(550, 600)
rock3.center_y = random.randint(20, 550)
rock5.center_x = dragon.center_x + random.randint(650, 700)
rock5.center_y = random.randint(20, 550)
rock6.center_x = dragon.center_x + random.randint(750, 800)
rock6.center_y = random.randint(20, 550)
rock7.center_x = dragon.center_x + random.randint(850, 900)
rock7.center_y = random.randint(20, 550)
rock8.center_x = dragon.center_x + random.randint(950, 1000)
rock8.center_y = random.randint(20, 550)
rock9.center_x = dragon.center_x + random.randint(1050, 1100)
rock9.center_y = random.randint(20, 550)

game = True
while game:
    while loop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                loop = False
        if  tsk.is_key_down(pygame.K_UP):
            dragon.center_y -= 7
        if  tsk.is_key_down(pygame.K_DOWN):
            dragon.center_y += 7
        if dragon.center_y > 630:
            dragon.center_y = 0
        if dragon.center_y < 0:
            dragon.center_y = 573
        if coins >= 5:
            inc = 5 + int(coins / 5) * 2
        coin1.center_x -= inc
        coin2.center_x -= inc
        coin3.center_x -= inc
        coin4.center_x -= inc
        coin5.center_x -= inc
        coin6.center_x -= inc
        coin7.center_x -= inc
        rock1.center_x -= inc
        rock2.center_x -= inc
        rock3.center_x -= inc
        rock5.center_x -= inc
        rock4.center_x -= inc
        rock6.center_x -= inc
        rock7.center_x -= inc
        rock8.center_x -= inc
        rock9.center_x -= inc
        background.center_x -= 5
        if background.center_x <= 0:
            background.center_x = 1018
        if coin1.center_x < -50:
            coin1.center_x = dragon.center_x + random.randint(1020, 1050)
            coin1.center_y = random.randint(20, 550)
            coin1.visible = True
            collidable_1 = True
        if coin2.center_x < -50:
            coin2.center_x = dragon.center_x + random.randint(1020, 1050)
            coin2.center_y = random.randint(20, 550)
            coin2.visible = True
            collidable_2 = True
        if coin3.center_x < -50:
            coin3.center_x = dragon.center_x + random.randint(1020, 1050)
            coin3.center_y = random.randint(20, 550) 
            coin3.visible = True
            collidable_3 = True
        if coin4.center_x < -50:
            coin4.center_x = dragon.center_x + random.randint(1020, 1050)
            coin4.center_y = random.randint(20, 550) 
            coin4.visible = True
            collidable_4 = True
        if coin5.center_x < -50:
            coin5.center_x = dragon.center_x + random.randint(1020, 1050)
            coin5.center_y = random.randint(20, 550) 
            coin5.visible = True
            collidable_5 = True
        if coin6.center_x < -50:
            coin6.center_x = dragon.center_x + random.randint(1020, 1050)
            coin6.center_y = random.randint(20, 550) 
            coin6.visible = True
            collidable_6 = True
        if coin7.center_x < -50:
            coin7.center_x = dragon.center_x + random.randint(1020, 1050)
            coin7.center_y = random.randint(20, 550) 
            coin7.visible = True
            collidable_7 = True
        if rock1.center_x < -50:
            rock1.center_x = dragon.center_x + 1018
            rock1.center_y = random.randint(20, 550)
        if rock2.center_x < -50:
            rock2.center_x = dragon.center_x + 1018
            rock2.center_y = random.randint(20, 550)
        if rock3.center_x < -50:
            rock3.center_x = dragon.center_x + 1018
            rock3.center_y = random.randint(20, 550)
        if rock4.center_x < -50:
            rock4.center_x = dragon.center_x + 1000
            rock4.center_y = random.randint(20, 550)
        if rock5.center_x < -50:
            rock5.center_x = dragon.center_x + 1000
            rock5.center_y = random.randint(20, 550)
        if rock6.center_x < -50:
            rock6.center_x = dragon.center_x + 1000
            rock6.center_y = random.randint(20, 550)
        if rock7.center_x < -50:
            rock7.center_x = dragon.center_x + 1000
            rock7.center_y = random.randint(20, 550)
        if rock8.center_x < -50:
            rock8.center_x = dragon.center_x + 1000
            rock8.center_y = random.randint(20, 550)
        if rock9.center_x < -50:
            rock9.center_x = dragon.center_x + 1000
            rock9.center_y = random.randint(20, 550)
        if pygame.sprite.collide_rect(dragon, coin1):
            coin1.visible = False
            if collidable_1:
                coins += 1
            collidable_1 = False
        if pygame.sprite.collide_rect(dragon, coin2):
            coin2.visible = False
            if collidable_2:
                coins += 1
            collidable_2 = False
        if pygame.sprite.collide_rect(dragon, coin3):
            coin3.visible = False
            if collidable_3:
                coins += 1
            collidable_3 = False
        if pygame.sprite.collide_rect(dragon, coin4):
            coin4.visible = False
            if collidable_4:
                coins += 1
            collidable_4 = False
        if pygame.sprite.collide_rect(dragon, coin5):
            coin5.visible = False
            if collidable_5:
                coins += 1
            collidable_5 = False
        if pygame.sprite.collide_rect(dragon, coin6):
            coin6.visible = False
            if collidable_6:
                coins += 1
            collidable_6 = False
        if pygame.sprite.collide_rect(dragon, coin7):
            coin7.visible = False
            if collidable_7:
                coins += 1
            collidable_7 = False
        if pygame.sprite.collide_rect(dragon, rock1):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock2):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock3):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock4):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock5):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock6):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock7):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock8):
            loop = False
            print("You Lose")
        if pygame.sprite.collide_rect(dragon, rock9):
            loop = False
            print("You Lose")
        background.draw()
        dragon.update(c.get_time())
        dragon.draw()
        rock1.draw()
        rock2.draw()
        rock3.draw()
        rock4.draw()
        rock5.draw()
        coin1.draw()
        coin2.draw()
        coin3.draw()
        coin4.draw()
        coin5.draw()
        rock6.draw()
        rock7.draw()
        rock8.draw()
        rock9.draw()
        coin6.draw()
        coin7.draw()
        pygame.display.flip()   
        c.tick(30)
    print ("You collected " + str(coins) + " coins!")
    print ("You made it to level " + str(int(coins/5) + 1))
    game = False
