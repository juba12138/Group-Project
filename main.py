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
    DoorList = [Door1, Door2]
    scene = SceneLike(mob, NPC, chatNPC, ENEMYLIST, DoorList) 
    Menu = menuscene(mob, NPC, chatNPC, scene, DoorList)
    listeners = [Menu, mob, NPC, chatNPC, Enemy1, Enemy2, Enemy3, Enemy4, scene, Door1, End1, Door2, End2]
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
        