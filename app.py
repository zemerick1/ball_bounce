import sys, pygame, random as r
from pygame.locals import *
from ball import Ball

pygame.init()
WIN_WIDTH = 800
WIN_HEIGHT = 600
size = WIN_WIDTH, WIN_HEIGHT
WIN = pygame.display.set_mode(size)

BLACK = pygame.Color("black")

LIFESPAN = 225
FRAMECOUNT = 0
clock = pygame.time.Clock()

balls = []
for i in range(20):
    balls.append(Ball(WIN))  

running = True
while running:
    clock.tick(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                for ball in balls:
                    ball.applyForce((-1, 0))
            elif event.key == pygame.K_RIGHT:
                for ball in balls:
                    ball.applyForce((1, 0))
            elif event.key == pygame.K_SPACE:
                for ball in balls:
                    ball.applyForce((r.randint(0, 20), -20))
    WIN.fill(BLACK)      

    for ball in balls:
        ball.update()
        ball.draw()
    
    
    pygame.display.update()