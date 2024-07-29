import pygame                       # import modules
from pygame.locals import *

FPS=60                              # game fps


FRAMEDIM = 1920,1080                # game constants
FRAMECENTRE= 960,540

BUTTONSIZE = (200,50)

WHITE = (255,255,255)

running = True

pygame.font.init()
largeFont = pygame.font.SysFont("courier-new",50)
mediumFont = pygame.font.SysFont("courier-new",25)
smallFont = pygame.font.SysFont("courier-new",15)

pygame.init()
clock=pygame.time.Clock()


def eventHandler()-> bool:          # Event handler                                              
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                return False
            
        if event.type == QUIT:
            return False
        
    return True


class Error(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Label():
    def __init__(self,pos,text,fontType) -> None:
        if fontType == "L":
            self.text = largeFont.render(str(text),True,WHITE)

        elif fontType == "M":
            self.text = mediumFont.render(str(text),True,WHITE)
        
        elif fontType == "S":
            self.text = smallFont.render(str(text),True,WHITE)

        else:raise Error('Incorrect parameters for "fontType"')
            

        self.text_rect = self.text.get_rect(center=pos)
        
    def blitSelf(self):             # Method to render text onto the screen to reduce cluttering in essential areas
        screen.blit(self.text,self.text_rect)





class Button():
    def __init__(self,pos,text) -> None:
        self.surf = pygame.Surface(BUTTONSIZE)
        self.surf.fill((10,10,10))
        self.rect = self.surf.get_rect(center=pos)
        self.text = mediumFont.render(str(text),True,WHITE)
        self.text_Rect = self.text.get_rect(center=pos)

    def blitSelf(self):
        
        screen.blit(self.text,self.text_Rect)
        



screen = pygame.display.set_mode(FRAMEDIM)


# MENU LABEL ASSIGN

titleLabel = Label((960,240),"Block Dodge","L")


# MENU BUTTON ASSIGN
menuButtons =[
Button((960,400),"Singleplayer"),
Button((960,500),"Multiplayer"),
Button((960,600),"Settings"),
Button((960,700),"Credits"),
Button((960,800),"Quit")
]


while running:

    running = eventHandler()
    screen.fill((0,0,0))

    titleLabel.blitSelf()

    for i in menuButtons:
        i.blitSelf()

    



    pygame.display.flip()
    clock.tick(FPS)