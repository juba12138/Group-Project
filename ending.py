import pygame
from Player import Event
from Player import Listener
from game_events import *

g_window = pygame.display.set_mode((1000, 800))

DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
DIAL = 5
RUN = 6
END = 7

class endscene(Listener):
    def __init__(self, image: pygame.Surface):
        self.image = image
        self.iflisten = False
        self.start_time = 0
        self.time = 0
        self.showtime = False
        
    def listen(self, event:Event):
        if self.iflisten: 
            if event.code == DRAW:
                g_window.fill((0, 0, 0))
                g_window.blit(self.image, (-110, 10))
                if self.showtime:
                    g_window.blit(pygame.font.Font(None, 60).render(str(self.time)+' S ', True, (255, 255, 255)), (375, 610))
            if event.code == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.time = (pygame.time.get_ticks()/1000) - self.start_time
                    self.time = round(self.time, 3)
                    self.image =pygame.transform.scale(pygame.image.load(".\sets\ecord.png"), (1200, 800))
                    self.showtime = True
                if keys[pygame.K_ESCAPE]:
                    exit()
                    
        super().listen(event)
        
        