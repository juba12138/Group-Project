import pygame
from game_events import *
from Player import Event
from Player import EntityLike
from Player import Player
from ending import endscene

g_window = pygame.display.set_mode((1000, 800))
DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
DIAL = 5
RUN = 6
END = 7

class door(EntityLike):
    def __init__(self, image: pygame.Surface, rect: pygame.Rect, ending:endscene, player:Player):
        super().__init__(image, rect)
        self.ending = ending
        self.player = player
        self.iflisten = False
        self.distance = (self.player.rect.x - self.rect.x) ** 2 + (self.player.rect.y - self.rect.y-30) ** 2
        self.dooropen = False
        
    def listen(self, event: Event):
        if self.iflisten:
            if event.code == pygame.KEYDOWN and self.distance <= 1000:
                self.intoending()
        super().listen(event)
        
    def intoending(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f]:
            self.post(Event(END))
            pygame.mixer.music.pause()
            self.ending.iflisten = True
            
    