import pygame
from Player import Event
from Player import EntityLike
from Player import Player
from game_events import *

g_window = pygame.display.set_mode((1000, 800))
DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
RUN = 6

class enemy(EntityLike):
    def __init__(self, image:pygame.Surface, rect:pygame.Rect, player:Player):
        super().__init__(image, rect)
        self.player = player
        self.speed = 5
        self.distance = (self.player.rect.x - self.rect.x) ** 2 + (self.player.rect.y - self.rect.y) ** 2
        self.chase = True
        self.iflisten = False
        
    def listen(self, event: Event):
        if self.iflisten:
            if event.code == STEP:
                self.pursue() 
                self.distance = (self.player.rect.x - self.rect.x) ** 2 + (self.player.rect.y - self.rect.y) ** 2 
        super().listen(event)
    
    def pursue(self):
        if self.chase:
            if self.rect.x < self.player.rect.x:
                self.rect.x += self.speed
            if self.rect.x > self.player.rect.x:
                self.rect.x -= self.speed
            if self.rect.y > self.player.rect.y:
                self.rect.y -= self.speed
            if self.rect.y < self.player.rect.y:
                self.rect.y += self.speed
        
    def kill(self):
        if self.distance <= 100:
            exit()