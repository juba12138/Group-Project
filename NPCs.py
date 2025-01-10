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
LEVEL1 = 8
LEVEL2 = 9
LEVEL3 = 10
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

class npc(EntityLike):
    def __init__(self, image: pygame.Surface, rect: pygame.Rect, diag:list = []):
        super().__init__(image, rect)
        self.font = pygame.font.Font(None, 50)
        self.i = 0
        self.diag_list = diag
        self.diag = self.diag_list[self.i]
        self.diag_Surface = self.font.render(self.diag, True, white)
        self.diag_Rect = (245, 550)
        self.button_Surface1 = self.font.render('Level 1', True, (255, 255, 255))
        self.button_Rect1 = self.button_Surface1.get_rect(center = (800, 630))
        self.button_Surface2 = self.font.render('Level 2', True, (255, 255, 255))
        self.button_Rect2 = self.button_Surface2.get_rect(center = (800, 680))
        self.button_Surface3 = self.font.render('Level 3', True, (255, 255, 255))
        self.button_Rect3 = self.button_Surface3.get_rect(center = (800, 730))
        self.buttonshow = False
        self.show = False
        self.iflisten = False
        self.distance = 1145141919810
        
        
    def listen(self, event: Event):
        if self.iflisten:
            if event.code == pygame.KEYDOWN:
                self.intodiag()
            if event.code == pygame.MOUSEBUTTONDOWN and self.buttonshow:
                self.levelchoice()  
        super().listen(event)
        
    def show_dial(self):
        if self.show:
            pygame.draw.rect(g_window, black, pygame.Rect(200, 525, 700,250))
            pygame.draw.rect(g_window, white, pygame.Rect(200, 525, 700, 250), 2)
            g_window.blit(self.diag_Surface, self.diag_Rect)
        if self.show and self.buttonshow:
            g_window.blit(self.button_Surface1, self.button_Rect1)
            g_window.blit(self.button_Surface2, self.button_Rect2)
            g_window.blit(self.button_Surface3, self.button_Rect3)
            
    def intodiag(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_f] and self.distance <= 2000:
            self.show = not self.show
        if keys[pygame.K_SPACE] and self.show:
            if self.i < len(self.diag_list) - 3:
                self.i = (self.i + 1) % len(self.diag_list)
                self.diag = self.diag_list[self.i]
                self.diag_Surface = self.font.render(self.diag, True, (255, 255, 255))
            elif self.i == len(self.diag_list) - 3:
                self.i = (self.i + 1) % len(self.diag_list)
                self.diag = self.diag_list[self.i]
                self.diag_Surface = self.font.render(self.diag, True, (255, 255, 255))
                self.buttonshow = not self.buttonshow
            elif self.i == len(self.diag_list) - 1:
                self.show = not self.show
                self.post(Event(RUN))
                self.i = 0
                self.diag_Surface = self.font.render(self.diag_list[0], True, (255, 255, 255))
                self.iflisten = False
                pygame.mixer.music.load('.\sets\ooss.mp3')
                pygame.mixer.music.play(-1)
                
    def levelchoice(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.button_Rect1.collidepoint(mouse_pos):
            self.post(Event(LEVEL1))
        elif self.button_Rect2.collidepoint(mouse_pos):
            self.post(Event(LEVEL2))
        elif self.button_Rect3.collidepoint(mouse_pos):
            self.post(Event(LEVEL3))
        self.buttonshow = not self.buttonshow
        self.i = (self.i + 1) % len(self.diag_list)
        self.diag = self.diag_list[self.i]
        self.diag_Surface = self.font.render(self.diag, True, (255, 255, 255))
     