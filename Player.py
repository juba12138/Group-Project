import pygame 
from game_events import *

g_window = pygame.display.set_mode((1000, 800))
DRAW = 1
STEP = 2
REQUEST_MOVE = 3
CAN_MOVE = 4
RUN = 6
END = 7


class Event:
    def __init__(self, code: int, body={}):
        self.code = code
        self.body = body
        
class Listener:
    def __init__(self):
        pass

    def post(self, event: Event):
        add_event(event)

    def listen(self, event: Event): ...
        
    
class EntityLike(Listener):
    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        self.image = image
        self.rect = rect

    def listen(self, event: Event): ...

    def draw(
        self, camera: tuple[int, int]
    ):
        rect = self.rect.move(
            *(-i for i in camera)
        )
        g_window.blit(self.image, rect)

class Player(EntityLike):

    def __init__(self, image: pygame.Surface, rect: pygame.Rect):
        super().__init__(image, rect)
        self.hp = 100
        self.speed = 10
        self.iflisten = False

    def listen(self, event: Event):
        if self.iflisten:
            if event.code == STEP:
                self.keydown()
            elif event.code == CAN_MOVE:
                self.rect.x = event.body["POS"][0]
                self.rect.y = event.body["POS"][1]
        super().listen(event)

    def keydown(self):
        keys = pygame.key.get_pressed()

        nx = self.rect.x
        ny = self.rect.y

        if keys[pygame.K_w]: 
            ny -= self.speed
        if keys[pygame.K_a]:
            nx -= self.speed
        if keys[pygame.K_s]:
            ny += self.speed
        if keys[pygame.K_d]:
            nx += self.speed
        if keys[pygame.K_ESCAPE]:
            exit()
        self.post(Event(REQUEST_MOVE, {"POS": (nx, ny)}))