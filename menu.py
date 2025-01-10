import pygame
from Player import Event
from Player import Listener
from game_events import *
from NPCs import npc
from chatbot import chatnpc
from enemy import enemy
from Scene import SceneLike
from door import door
from appliance import appliance

g_window = pygame.display.set_mode((1000, 800))

DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
DIAL = 5
RUN = 6
END = 7

class menuscene(Listener):
    def __init__(self, player, npc:npc , chatbot:chatnpc, scene:SceneLike, doorlist:list[door], appliancelist:list[appliance]):
        super().__init__()
        self.menu = pygame.transform.scale(pygame.image.load('.\sets\menuscene.png'), (1200, 800))
        self.player = player
        self.npc = npc
        self.chatbot = chatbot
        self.scene = scene
        self.iflisten = True
        self.doorlist = doorlist
        self.appliancelist = appliancelist
        
    def listen(self, event:Event):
        if self.iflisten: 
            if event.code == DRAW:
                g_window.blit(self.menu, (-110, 10))
            if event.code == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_SPACE]:
                    self.iflisten = False
                    self.scene.iflisten = True
                    self.player.iflisten = True
                    self.npc.iflisten = True
                    self.chatbot.iflisten = True
                    for door in self.doorlist:
                        door.iflisten = True
                    for appliance in self.appliancelist:
                        appliance.iflisten = True
                    pygame.mixer.music.load('.\sets\city.mp3')
                    pygame.mixer.music.play(-1)
                if keys[pygame.K_ESCAPE]:
                    exit()