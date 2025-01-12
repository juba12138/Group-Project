import pygame
from Player import *
from Scene import SceneLike
from game_events import *
from NPCs import npc
from chatbot import chatnpc
from enemy import enemy
from menu import menuscene
from door import door
from ending import endscene
from appliance import appliance
from coin import coin

pygame.init() 
g_window = pygame.display.set_mode((1000, 800))

clock = pygame.time.Clock()
fps = 600
DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
DIAL = 5
RUN = 6
END = 7

if __name__ == "__main__":
    NPC = npc(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\monster.png"), (300, 300)
        ),
        rect=pygame.Rect(1000, 230, 60, 60),
        diag= ['?', 'You want to ESCPAE FROM HERE?', 'Haha, you are so funny.', 'The road ahead is difficult', 'Moreover', 'there is more than one door to escape',  'You have to find the right one to get out', 'Please choose your level.', 'Good luck. Wish God bless you!']
    )
    mob = Player(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\Bob.png"), (60, 60)
        ),
        rect=pygame.Rect(80, 330, 60, 60),
    )
    chatNPC = chatnpc(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\pai.png"), (300, 300)
        ),
        rect=pygame.Rect(200, 250, 60, 60)
    )
    Enemy1 = enemy(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\ghost.png"), (60, 60)
        ),
        rect=pygame.Rect(600, 60, 60, 60),
        player=mob
    )
    Enemy2 = enemy(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\ghost.png"), (60, 60)
        ),
        rect=pygame.Rect(2500, 400, 60, 60),
        player=mob
    )
    Enemy3 = enemy(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\ghost.png"), (60, 60)
        ),
        rect=pygame.Rect(600, 700, 60, 60),
        player=mob
    )
    Enemy4 = enemy(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\ghost.png"), (60, 60)
        ),
        rect=pygame.Rect(100, 700, 60, 60),
        player=mob
    )
    ENEMYLIST = [Enemy1, Enemy2, Enemy3, Enemy4]
    End1 = endscene(
            image=pygame.transform.scale(
                pygame.image.load(".\sets\win.png"), (1200, 800)
            )
    )
    Door1 = door(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\portal.png"), (100, 100)
        ),
        rect=pygame.Rect(3860, 600, 60, 60),
        ending=End1,
        player=mob
    )
    End2 = endscene(
            image=pygame.transform.scale(
                pygame.image.load(".\sets\lose.png"), (1200, 800)
            )
    )
    Door2 = door(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\portal.png"), (100, 100)
        ),
        rect=pygame.Rect(3400, 40, 60, 60),
        ending=End2,
        player=mob
    )
    Door3 = door(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\portal.png"), (100, 100)
        ),
        rect=pygame.Rect(2780, 680, 60, 60),
        ending=End2,
        player=mob
    )
    Door4 = door(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\portal.png"), (100, 100)
        ),
        rect=pygame.Rect(3160, 180, 60, 60),
        ending=End2,
        player=mob
    )
    Door5 = door(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\portal.png"), (100, 100)
        ),
        rect=pygame.Rect(2210, 40, 60, 60),
        ending=End2,
        player=mob
    )
    Door6 = door(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\portal.png"), (100, 100)
        ),
        rect=pygame.Rect(1895, 40, 60, 60),
        ending=End2,
        player=mob
    )
    DoorList = [Door1, Door2, Door3, Door4, Door5, Door6]
    SPEEDPLUS = appliance(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\speedplus.png"), (60, 60)
        ),
        rect=pygame.Rect(2660, 700, 60, 60),
        player=mob
    )
    APPLY = [SPEEDPLUS]
    coin1 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1460, 570, 60, 60),
        player=mob
    )
    coin2 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1460, 430, 60, 60),
        player=mob
    )
    coin3 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1460, 300, 60, 60),
        player=mob
    )
    coin4 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1460, 140, 60, 60),
        player=mob
    )
    coin5 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1540, 40, 60, 60),
        player=mob
    )
    coin6 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1460, 700, 60, 60),
        player=mob
    )
    coin7 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1570, 420, 60, 60),
        player=mob
    )
    coin8 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1640, 420, 60, 60),
        player=mob
    )
    coin9 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1640, 330, 60, 60),
        player=mob
    )
    coin10 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1570, 330, 60, 60),
        player=mob
    )
    coin11 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1570, 170, 60, 60),
        player=mob
    )
    coin12 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1640, 170, 60, 60),
        player=mob
    )
    coin13 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1460, 40, 60, 60),
        player=mob
    )
    coin14 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1570, 250, 60, 60),
        player=mob
    )
    coin15 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1640, 250, 60, 60),
        player=mob
    )
    coin16 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1770, 170, 60, 60),
        player=mob
    )
    coin17 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1890, 170, 60, 60),
        player=mob
    )
    coin18 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1890, 290, 60, 60),
        player=mob
    )
    coin19 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1770, 290, 60, 60),
        player=mob
    )
    coin20 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1770, 410, 60, 60),
        player=mob
    )
    coin21 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1890, 410, 60, 60),
        player=mob
    )
    coin22 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1890, 540, 60, 60),
        player=mob
    )
    coin23 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1770, 540, 60, 60),
        player=mob
    )
    coin24 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1650, 540, 60, 60),
        player=mob
    )
    coin25 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1570, 540, 60, 60),
        player=mob
    )
    coin26 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(1570, 670, 60, 60),
        player=mob
    )
    coin27 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2000, 70, 60, 60),
        player=mob
    )
    coin28 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2100, 70, 60, 60),
        player=mob
    )
    coin29 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2360, 190, 60, 60),
        player=mob
    )
    coin30 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2220, 330, 60, 60),
        player=mob
    )
    coin31 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2360, 330, 60, 60),
        player=mob
    )
    coin32 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2360, 450, 60, 60),
        player=mob
    )
    coin33 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2210, 450, 60, 60),
        player=mob
    )
    coin34 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2210, 690, 60, 60),
        player=mob
    )
    coin35 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2310, 690, 60, 60),
        player=mob
    )
    coin36 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2410, 690, 60, 60),
        player=mob
    )
    coin37 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2510, 690, 60, 60),
        player=mob
    )
    coin38 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2925, 570, 60, 60),
        player=mob
    )
    coin39 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3045, 570, 60, 60),
        player=mob
    )
    coin40 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3195, 570, 60, 60),
        player=mob
    )
    coin41 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3280, 570, 60, 60),
        player=mob
    )
    coin42 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3280, 450, 60, 60),
        player=mob
    )
    coin43 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3195, 450, 60, 60),
        player=mob
    )
    coin44 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3045, 450, 60, 60),
        player=mob
    )
    coin45 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3045, 370, 60, 60),
        player=mob
    )
    coin46 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2925, 370, 60, 60),
        player=mob
    )
    coin47 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2925, 255, 60, 60),
        player=mob
    )
    coin48 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2925, 175, 60, 60),
        player=mob
    )
    coin49 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(2925, 55, 60, 60),
        player=mob
    )
    coin50 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3045, 55, 60, 60),
        player=mob
    )
    coin51 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3170, 55, 60, 60),
        player=mob
    )
    coin52 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3280, 55, 60, 60),
        player=mob
    )
    coin53 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3280, 175, 60, 60),
        player=mob
    )
    coin54 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3280, 330, 60, 60),
        player=mob
    )
    coin55 = coin(
        image=pygame.transform.scale(
            pygame.image.load(".\sets\coin.png"), (40, 40)
        ),
        rect=pygame.Rect(3195, 330, 60, 60),
        player=mob
    )
    COINLIST = [coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36, coin37, coin38, coin39, coin40, coin41, coin42, coin43, coin44, coin45, coin46, coin47, coin48, coin49, coin50, coin51, coin52, coin53, coin54, coin55]
    scene = SceneLike(mob, NPC, chatNPC, ENEMYLIST, DoorList, APPLY, COINLIST) 
    Menu = menuscene(mob, NPC, chatNPC, scene, DoorList, APPLY, COINLIST)
    listeners = [Menu, mob, NPC, chatNPC, Enemy1, Enemy2, Enemy3, Enemy4, scene, Door1, End1, Door2, End2, Door3, Door4, Door5, Door6, SPEEDPLUS, coin1, coin2, coin3, coin4, coin5, coin6, coin7, coin8, coin9, coin10, coin11, coin12, coin13, coin14, coin15, coin16, coin17, coin18, coin19, coin20, coin21, coin22, coin23, coin24, coin25, coin26, coin27, coin28, coin29, coin30, coin31, coin32, coin33, coin34, coin35, coin36, coin37, coin38, coin39, coin40, coin41, coin42, coin43, coin44, coin45, coin46, coin47, coin48, coin49, coin50, coin51, coin52, coin53, coin54, coin55]
    pygame.mixer.music.load('.\sets\Genshin Impact Main Theme.mp3')
    pygame.mixer.music.play(-1)
    while True:
        g_window.fill((0, 0, 0))  
        for event in pygame.event.get(): 
            add_event(Event(event.type))
        add_event(Event(STEP))
        add_event(Event(DRAW)) 
        
        while g_evene_queue:  
            event = g_evene_queue.pop(0)  
            for l in listeners:  
                l.listen(event)
        pygame.display.flip()
        
        clock.tick(fps) 
        