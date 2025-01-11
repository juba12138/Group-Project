import pygame
from game_events import *
from Player import Event
from Player import EntityLike
from chat import aichat
from Player import Player

g_window = pygame.display.set_mode((1000, 800))
DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
DIAL = 5
RUN = 6
END = 7
white = (255, 255, 255)
black = (0, 0, 0)
gray = (200, 200, 200)

class chatnpc(EntityLike):
    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        super().__init__(image, rect)
        self.font = pygame.font.Font(None, 30)
        self.input = ''
        self.output = ''
        self.chat_box = pygame.Rect(200, 525, 700,250)
        self.active = False
        self.show = False
        self.boxcolour = black
        self.iflisten = False
        self.distance = 1145141919810
    def show_chat(self):
        if self.show:
            pygame.draw.rect(g_window, self.boxcolour, self.chat_box)
            pygame.draw.rect(g_window, white, self.chat_box, 2)
            if len(self.input) <= 52:
                message_Surface = self.font.render(self.input, True, black)
                message_Rect = (250, 540)
                g_window.blit(message_Surface, message_Rect)
            elif len (self.input) <=104:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
            elif len (self.input) <=52*3:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
            elif len (self.input) <=52*4:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:156], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
                message_Surface4 = self.font.render(self.input[156:], True, black)
                message_Rect4 = (250, 600)
                g_window.blit(message_Surface4, message_Rect4)
            elif len (self.input) <=52*5:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:156], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
                message_Surface4 = self.font.render(self.input[156:208], True, black)
                message_Rect4 = (250, 600)
                g_window.blit(message_Surface4, message_Rect4)
                message_Surface5 = self.font.render(self.input[208:], True, black)
                message_Rect5 = (250, 620)
                g_window.blit(message_Surface5, message_Rect5)
            elif len (self.input) <=52*6:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:156], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
                message_Surface4 = self.font.render(self.input[156:208], True, black)
                message_Rect4 = (250, 600)
                g_window.blit(message_Surface4, message_Rect4)
                message_Surface5 = self.font.render(self.input[208:208+52], True, black)
                message_Rect5 = (250, 620)
                g_window.blit(message_Surface5, message_Rect5)
                message_Surface6 = self.font.render(self.input[260:], True, black)
                message_Rect6 = (250, 640)
                g_window.blit(message_Surface6, message_Rect6)
            elif len (self.input) <=52*7:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:156], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
                message_Surface4 = self.font.render(self.input[156:208], True, black)
                message_Rect4 = (250, 600)
                g_window.blit(message_Surface4, message_Rect4)
                message_Surface5 = self.font.render(self.input[208:208+52], True, black)
                message_Rect5 = (250, 620)
                g_window.blit(message_Surface5, message_Rect5)
                message_Surface6 = self.font.render(self.input[260:260+52], True, black)
                message_Rect6 = (250, 640)
                g_window.blit(message_Surface6, message_Rect6)
                message_Surface7 = self.font.render(self.input[312:], True, black)
                message_Rect7 = (250, 660)
                g_window.blit(message_Surface7, message_Rect7)
            elif len (self.input) <=52*8:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:156], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
                message_Surface4 = self.font.render(self.input[156:208], True, black)
                message_Rect4 = (250, 600)
                g_window.blit(message_Surface4, message_Rect4)
                message_Surface5 = self.font.render(self.input[208:208+52], True, black)
                message_Rect5 = (250, 620)
                g_window.blit(message_Surface5, message_Rect5)
                message_Surface6 = self.font.render(self.input[260:260+52], True, black)
                message_Rect6 = (250, 640)
                g_window.blit(message_Surface6, message_Rect6)
                message_Surface7 = self.font.render(self.input[312:312+52], True, black)
                message_Rect7 = (250, 660)
                g_window.blit(message_Surface7, message_Rect7)
                message_Surface8 = self.font.render(self.input[364:], True, black)
                message_Rect8 = (250, 680)
                g_window.blit(message_Surface8, message_Rect8)
            else:
                message_Surface1 = self.font.render(self.input[0:52], True, black)
                message_Rect1 = (250, 540)
                g_window.blit(message_Surface1, message_Rect1)
                message_Surface2 = self.font.render(self.input[52:104], True, black)
                message_Rect2 = (250, 560)
                g_window.blit(message_Surface2, message_Rect2)
                message_Surface3 = self.font.render(self.input[104:156], True, black)
                message_Rect3 = (250, 580)
                g_window.blit(message_Surface3, message_Rect3)
                message_Surface4 = self.font.render(self.input[156:208], True, black)
                message_Rect4 = (250, 600)
                g_window.blit(message_Surface4, message_Rect4)
                message_Surface5 = self.font.render(self.input[208:208+52], True, black)
                message_Rect5 = (250, 620)
                g_window.blit(message_Surface5, message_Rect5)
                message_Surface6 = self.font.render(self.input[260:260+52], True, black)
                message_Rect6 = (250, 640)
                g_window.blit(message_Surface6, message_Rect6)
                message_Surface7 = self.font.render(self.input[312:312+52], True, black)
                message_Rect7 = (250, 660)
                g_window.blit(message_Surface7, message_Rect7)
                message_Surface8 = self.font.render(self.input[364:364+52], True, black)
                message_Rect8 = (250, 680)
                g_window.blit(message_Surface8, message_Rect8)
                message_Surface9 = self.font.render(self.input[364+52:], True, black)
                message_Rect9 = (250, 700)
                g_window.blit(message_Surface9, message_Rect9)
            
    def listen(self, event: Event):
        if self.iflisten:
            if event.code == pygame.KEYDOWN and self.distance <=10000:
                self.intochat()
            if event.code == pygame.MOUSEBUTTONDOWN and self.show:
                self.start_chat()
        super().listen(event)
    
    def intochat(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]:
            self.show = not self.show
        elif keys[pygame.K_a] and self.active:
            self.input += 'a' 
        elif keys[pygame.K_b] and self.active:
            self.input += 'b'
        elif keys[pygame.K_c] and self.active:
            self.input += 'c'
        elif keys[pygame.K_d] and self.active:
            self.input += 'd'
        elif keys[pygame.K_e] and self.active:
            self.input += 'e'
        elif keys[pygame.K_f] and self.active:
            self.input += 'f'
        elif keys[pygame.K_g] and self.active:
            self.input += 'g'
        elif keys[pygame.K_h] and self.active:
            self.input += 'h'
        elif keys[pygame.K_i] and self.active:
            self.input += 'i'
        elif keys[pygame.K_j] and self.active:
            self.input += 'j'
        elif keys[pygame.K_k] and self.active:
            self.input += 'k'
        elif keys[pygame.K_l] and self.active:
            self.input += 'l'
        elif keys[pygame.K_m] and self.active:
            self.input += 'm'
        elif keys[pygame.K_n] and self.active:
            self.input += 'n'
        elif keys[pygame.K_o] and self.active:
            self.input += 'o'
        elif keys[pygame.K_p] and self.active:
            self.input += 'p'
        elif keys[pygame.K_q] and self.active:
            self.input += 'q'
        elif keys[pygame.K_r] and self.active:
            self.input += 'r'
        elif keys[pygame.K_s] and self.active:
            self.input += 's'
        elif keys[pygame.K_t] and self.active:
            self.input += 't'
        elif keys[pygame.K_u] and self.active:
            self.input += 'u'
        elif keys[pygame.K_v] and self.active:
            self.input += 'v'
        elif keys[pygame.K_w] and self.active:
            self.input += 'w'
        elif keys[pygame.K_x] and self.active:
            self.input += 'x'
        elif keys[pygame.K_y] and self.active:
            self.input += 'y'
        elif keys[pygame.K_z] and self.active:
            self.input += 'z'
        elif keys[pygame.K_SPACE] and self.active:
            self.input += ' '
        elif keys[pygame.K_BACKSPACE] and self.active:
            self.input = self.input[:-1]
        elif keys[pygame.K_RETURN]:
            self.input = aichat(self.input)
        elif keys[pygame.K_QUESTION]:
            self.input += '?'
        elif keys[pygame.K_QUOTE]:
            self.input += '"'
        elif keys[pygame.K_COMMA]:
            self.input += ','
        elif keys[pygame.K_PERIOD]:
            self.input += '.'
        elif keys[pygame.K_1]:
            self.input += '1'
        elif keys[pygame.K_2]:
            self.input += '2'
        elif keys[pygame.K_3]:
            self.input += '3'
        elif keys[pygame.K_4]:
            self.input += '4'
        elif keys[pygame.K_5]:
            self.input += '5'
        elif keys[pygame.K_6]:
            self.input += '6'
        elif keys[pygame.K_7]:
            self.input += '7'
        elif keys[pygame.K_8]:
            self.input += '8'
        elif keys[pygame.K_9]:
            self.input += '9'
        elif keys[pygame.K_0]:
            self.input += '0'
        elif keys[pygame.K_PLUS]:
            self.input += '+'
        elif keys[pygame.K_MINUS]:
            self.input += '-'
        elif keys[pygame.K_DELETE]:
            self.input = ''
        
    def start_chat(self):
        self.active = not self.active
        if self.active:
            self.boxcolour = gray
        else:
            self.boxcolour = black
