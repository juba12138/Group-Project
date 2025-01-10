import pygame
import random
from Player import EntityLike
from Player import Listener
from Player import Event
from NPCs import npc
from chatbot import chatnpc
from enemy import enemy
from door import door

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

def tuple_sub(a, b):
    return (a[0] - b[0], a[1] - b[1])


def tuple_mul(a, b):
    return (a[0] * b, a[1] * b)


def tuple_min(a, b):
    return (min(a[0], b[0]), min(a[1], b[1]))


def tuple_max(a, b):
    return (max(a[0], b[0]), max(a[1], b[1]))


class Wall(EntityLike):
    def __init__(self, rect: pygame.rect.Rect):
        super().__init__(
            image=pygame.transform.scale(
                pygame.image.load(".\sets\cityWall.png"), (40, 40)
            ),
            rect=rect,
        )


class Tile(
    EntityLike
):
    def __init__(self, image, rect: pygame.rect.Rect):
        super().__init__(
            image=image,
            rect=rect,
        )


class SceneLike(Listener):
    def __init__(self, player, npc:npc , chatbot:chatnpc, enemylist:list[enemy], doorlist:list[door]):

        super().__init__()
        self.walls = []
        self.tiles = []
        self.player = player
        self.npc = npc
        self.chatbot = chatbot
        self.enemylist = enemylist
        self.distance1 = (self.player.rect.x - self.npc.rect.x-110) ** 2 + (self.player.rect.y - self.npc.rect.y-120) ** 2
        self.distance2 = (self.player.rect.x - self.chatbot.rect.x-110) ** 2 + (self.player.rect.y - self.chatbot.rect.y-120) ** 2
        self.window_scale = (1000, 800)
        self.map_range = (4000, 800)
        self.carema = (0, 0) 
        self.doorlist = doorlist
        self.update_camera()
        self.iflisten = False
        self.enemychoice = []

        for i in range(self.map_range[0] // 40 + 1):
            for j in range(self.map_range[1] // 40 + 1):
                self.tiles.append(
                    Tile(pygame.transform.scale(
                pygame.image.load(".\sets\ground1.png"), (40, 40)), pygame.Rect(i * 40, j * 40, 40, 40))
                )
        
        self.tiles.append(
            Tile(pygame.transform.scale(
                pygame.image.load(".\sets\heart.png"), (40, 40)), pygame.Rect(self.player.rect.x - 400, 80, 40, 40))
        )
        
        for i in range(self.map_range[0]//40):
            self.walls.append(
                Wall(
                    pygame.Rect(
                        i*40,
                        0,
                        40,
                        40,
                    )
                )
            )
            self.walls.append(
                Wall(
                    pygame.Rect(
                        i*40,
                        self.map_range[1]-40,
                        40,
                        40,
                    )
                )
            )
        for i in range(self.map_range[1]//40):
            self.walls.append(
                Wall(
                    pygame.Rect(
                        0,
                        i*40,
                        40,
                        40,
                    )
                )
            )
            self.walls.append(
                Wall(
                    pygame.Rect(
                        self.map_range[0]-40,
                        i*40,
                        40,
                        40,
                    )
                )
            )
        for i in range(self.map_range[1]//120):
            self.walls.append(
                Wall(
                    pygame.Rect(
                        725,
                        i*120+120,
                        40,
                        40,
                    )
                )
            )
        for i in range(self.map_range[1]//40):
            if i < 16:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            1400,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i != 1 and i != 2 and i != 8 and i != 9 :
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            1520,
                            i*40,
                            40,
                            40,
                        )
                    )
                )

        self.walls.append(
            Wall(
                pygame.Rect(
                    1560,
                    3*40,
                    40,
                    40,
                )
            )
        )
        for i in range(8):
            self.walls.append(
                Wall(
                    pygame.Rect(
                        1560+40*i,
                        12*40,
                        40,
                        40,
                    )
                )
            )
        for i in range(self.map_range[1]//40):
            if i >=3 and i <= 11:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            1720,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i <= 15:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            1960,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i == 1 or i == 2 or i == 3:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            1600,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(7):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            1960-40-40*i,
                            15*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(3):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            1960-40-40*i,
                            9*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(3):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            1720+40+40*i,
                            6*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i !=4 and i != 5:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            2160,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(2):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2160-40-40*i,
                            6*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(2):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2160-120-40*i,
                            12*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(6):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2160+40+40*i,
                            3*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >=3 and i <=12:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            2440,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(8):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2440-40*4+40*i,
                            13*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(3):
              self.walls.append(
                    Wall(
                        pygame.Rect(
                            2440-40-40*i,
                            7*40,
                            40,
                            40,
                        )
                    )
                )  
        for i in range(3):
              self.walls.append(
                    Wall(
                        pygame.Rect(
                            2440-40*4-40*i,
                            10*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(12):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2440-40*4+40*i,
                            16*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >=4:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            2720,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(4):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2720-40-40*i,
                            4*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >= 7 and i <=12:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            2720-4*40,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        self.walls.append(
            Wall(
                pygame.Rect(
                    2720-2*40,
                    3*40,
                    40,
                    40,
                )
            )
        )
        self.walls.append(
            Wall(
                pygame.Rect(
                    2720-1*40,
                    3*40,
                    40,
                    40,
                )
            )
        )
        self.walls.append(
            Wall(
                pygame.Rect(
                    2720-3*40,
                    3*40,
                    40,
                    40,
                )
            )
        )
        self.walls.append(
            Wall(
                pygame.Rect(
                    2720-4*40,
                    3*40,
                    40,
                    40,
                )
            )
        )
        self.walls.append(
            Wall(
                pygame.Rect(
                    2720,
                    3*40,
                    40,
                    40,
                )
            )
        )
        for i in range(self.map_range[1]//40):
            if i >= 1 and i <= 11:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            2880,
                            i*40,
                            40,
                            40,
                        )
                    )
                )  
        for i in range(self.map_range[1]//40):
            if i >= 14 and i <= 16:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            2880,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(20):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2880+40+40*i,
                            16*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(3):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            2880+40+40*i,
                            11*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(2):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3000,
                            (12+i)*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(6):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3000+40+40*i,
                            13*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >= 1 and  i <= 15:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(6):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360-40-40*i,
                            10*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i == 9 or  i == 8:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360-6*40,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(3):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360-7*40-40*i,
                            8*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >= 3 and  i <= 7:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360-9*40,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(6):
            if i != 2:
                self.walls.append(
                        Wall(
                          pygame.Rect(
                               3360-9*40+40+40*i,
                               3*40,
                                40,
                             40,
                         )
                      )
                )
        for i in range(self.map_range[1]//40):
            if i >= 4 and  i <= 7:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360-3*40,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >= 4 and  i <= 5:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            3360-6*40,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(self.map_range[1]//40):
            if i >= 3 and  i <= 18:
                self.walls.append(
                    Wall(
                        pygame.Rect(
                            3800,
                            i*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(8):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3800-40-40*i,
                            13*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(8):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3800-40*3-40*i,
                            10*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(8):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3800-40-40*i,
                            7*40,
                            40,
                            40,
                        )
                    )
                )
        for i in range(8):
            self.walls.append(
                    Wall(
                        pygame.Rect(
                            3800-40*3-40*i,
                            4*40,
                            40,
                            40,
                        )
                    )
                )
    def update_camera(self):
        player_center_cord = (
            self.player.rect.center
        )
        self.camera = tuple_sub(
            player_center_cord, tuple_mul(self.window_scale, 0.5)
        )
        left_top = (0, 0)
        right_down = tuple_sub(
            self.map_range, self.window_scale
        )
        
        self.camera = tuple_min(right_down, self.camera)
        self.camera = tuple_max(left_top, self.camera)
        self.distance1 = (self.player.rect.x - self.npc.rect.x-110) ** 2 + (self.player.rect.y - self.npc.rect.y-120) ** 2
        self.distance2 = (self.player.rect.x - self.chatbot.rect.x-110) ** 2 + (self.player.rect.y - self.chatbot.rect.y-120) ** 2
        for door in self.doorlist:
            door.distance = (self.player.rect.x - door.rect.x) ** 2 + (self.player.rect.y - door.rect.y-30) ** 2
    def listen(self, event: Event): 
        super().listen(event)
        if self.iflisten:
            if event.code == REQUEST_MOVE: 
                can_move = 1  
                target_rect = pygame.Rect(
                    event.body["POS"][0], event.body["POS"][1], 60, 60
                )  
                for wall in self.walls:  
                    if wall.rect.colliderect(target_rect):  
                        can_move = 0  
                        break 
                if self.npc.show:
                    can_move = 0
                if self.chatbot.show:
                    can_move = 0
                if can_move:  
                    self.post(Event(CAN_MOVE, event.body))

            if event.code == STEP: 
                self.update_camera()
                
            if event.code == LEVEL1:
                self.enemychoice = [self.enemylist[3]]
                for enemy in self.enemychoice:
                    enemy.speed = 3
                
            if event.code == LEVEL2:
                self.enemychoice = [self.enemylist[0], self.enemylist[2]]
                for enemy in self.enemychoice:
                    enemy.speed = 4
                
            if event.code == LEVEL3:
                self.enemychoice = self.enemylist
            
            if event.code == RUN:
                for yourenemy in self.enemychoice:
                    yourenemy.iflisten = True
            
            if event.code == DRAW:  
                for tile in self.tiles:  
                    tile.draw(self.camera)
                for wall in self.walls:  
                    wall.draw(self.camera)
                #playerdraw
                if self.player.iflisten:
                    self.player.draw(self.camera)
                #npcdraw
                if self.npc.iflisten:
                    self.npc.draw(self.camera)
                    if (self.distance1) ** 0.5 <= 100:
                        self.npc.show_dial()
                #enemydraw
                for yourenemy in self.enemylist:
                    if yourenemy.iflisten:
                        yourenemy.draw(self.camera)
                        yourenemy.kill()
                #chatbotdraw
                if self.chatbot.iflisten:
                    self.chatbot.draw(self.camera)
                    if (self.distance2) ** 0.5 <= 100:
                        self.chatbot.show_chat()
                #doordraw
                for door in self.doorlist:
                    if door.iflisten:
                        door.draw(self.camera)
                        
            if event.code == END:
                self.iflisten = False
                self.player.iflisten = False
                self.npc.iflisten = False
                self.chatbot.iflisten = False
                for yourenemy in self.enemylist:
                    yourenemy.iflisten = False
                for door in self.doorlist:
                    door.iflisten = False