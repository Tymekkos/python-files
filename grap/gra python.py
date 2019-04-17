
# -*- coding: utf-8 -*-

import sys, pygame
from pygame.locals import *
import random
WIDTH = 800	
HEIGHT = 600
PALETKA_SPEED = 4

pygame.init()


pygame.display.set_mode((800, 600))
pygame.display.set_caption("Gra Tymeczka")

okno = pygame.display.get_surface()

okno.fill((244, 173, 66))
paletka = pygame.Surface((15,90))
paletka.fill((0,0,255))
paXY = paletka.get_rect()
paXY.x=200
paXY.y=100

pilka = pygame.image.load("./grey-3.gif")
pilka = pygame.transform.scale(pilka,( 30, 30))
bXY = pilka.get_rect()
bXY.x = 500
bXY.y = 500

fps = pygame.time.Clock()
bx,by=4,4
px = PALETKA_SPEED

pygame.display.flip()



while 1:
    for zdarzenie in pygame.event.get():
        
        if zdarzenie.type == QUIT:
            sys.exit(0)
        if zdarzenie.type == KEYDOWN:
            if zdarzenie.key == K_UP:
                px=-PALETKA_SPEED
            if zdarzenie.key == K_DOWN:
                px=PALETKA_SPEED
            if zdarzenie.key == K_RIGHT:
                px=0
    if paXY.colliderect(bXY):
        bx = random.randint(3,6)
        by = random.randint(3,6)
    okno.fill((244, 173, 66))
    paXY.y+=px
    if paXY.y < 0:
        px = PALETKA_SPEED
    if paXY.y > HEIGHT-90:
        px = -PALETKA_SPEED
    okno.blit(paletka,paXY)
    bXY.x += bx
    if bXY.x>WIDTH-30 or bXY.x<0:
        bx *= -1
    if bXY.y>HEIGHT-30 or bXY.y<0:
        by *= -1
    bXY.y += by
    okno.blit(pilka,bXY)
    pygame.display.update()
    fps.tick(60)




