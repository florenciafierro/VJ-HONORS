import pygame
import random
from pygame.locals import (RLEACCEL)



bosspng = pygame.image.load('assets/boss.png')
bosspng_scaled = pygame.transform.scale(bosspng, (180, 180))

class Boss(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH, SCREEN_HEIGHT,player):
        # nos permite invocar métodos o atributos de Sprite
        super(Boss, self).__init__()
        self.surf = bosspng_scaled
        self.surf.set_colorkey((0, 0, 0), RLEACCEL)
        self.vidas= 20
        self.speed= 4.5
        self.rect = self.surf.get_rect(center=(SCREEN_WIDTH + 150,random.randint(0, SCREEN_HEIGHT),))
        self.entrar=True
        self.player=player
        self.screen_width = SCREEN_WIDTH
        self.screen_height = SCREEN_HEIGHT

    def update(self):
        #para que entre desde la derecha y no solo aparezca, hacemos que se mueva a la izquierda cuando esta fuera de la pantalla, luego empieza a perseguir
        if self.entrar==True:
            self.rect.x-=self.speed
            if self.rect.right<=self.screen_width-50:
                self.entrar=False
            return
        
        #su moviento es perseguir al jugador
        coordx=self.player.rect.centerx-self.rect.centerx
        coordy=self.player.rect.centery-self.rect.centery
        dist=max((coordx**2+coordy**2)**0.5,1)

        #si se acerca mucho al jugador hacemos que se aleje para que no se queden pegados
        if dist<60:
            self.rect.x-=int((self.speed*coordx)/dist*5)
            self.rect.y-=int((self.speed*coordy)/dist*5)
        #de lo contrario, lo persigue
        elif self.rect.right>self.screen_width-150:
            self.rect.x-=self.speed
        else:
            self.rect.x+=int(self.speed*coordx/dist)
            self.rect.y+=int(self.speed*coordy/dist)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_width:
            self.rect.right = self.screen_width
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > self.screen_height:
            self.rect.bottom = self.screen_height
        

    def perder_vida(self):
        self.vidas-=1
        if self.vidas<=0:
            self.kill()
        
    

