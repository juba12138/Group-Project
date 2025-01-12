import pygame
from game_events import *
from Player import Event
from Player import EntityLike
from Player import Player

g_window = pygame.display.set_mode((1000, 800))

DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
DIAL = 5
RUN = 6
END = 7

class coin(EntityLike):
    def __init__(self, image: pygame.Surface, rect: pygame.Rect, player:Player):
        super().__init__(image, rect)
        self.player = player
        self.iflisten = False
        self.distance = (self.player.rect.x - self.rect.x + 10) ** 2 + (self.player.rect.y - self.rect.y) ** 2
        
    def listen(self, event: Event):
        if self.iflisten:
            if event.code == STEP and self.distance <= 900:
                self.addcoin()
        super().listen(event)
                
    def addcoin(self):
        self.player.coins += 1
        self.iflisten = not self.iflisten