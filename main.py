import pygame                       # import modules
from pygame.locals import *

FPS=60                              # game fps

FRAMEDIM = 1920,1080                # game constants
FRAMECENTRE= 960,540

BUTTONSIZE = (200,50)

WHITE = (255,255,255)

PAGES = ("main","singleplayer","multiplayer","settings","credits","in_game")

running = True

pygame.font.init()
largeFont = pygame.font.SysFont("courier-new",50)
mediumFont = pygame.font.SysFont("courier-new",25)
smallFont = pygame.font.SysFont("courier-new",15)

pygame.init()
pygame.mixer.init()
clock=pygame.time.Clock()

pygame.mixer.music.load("assests/audio/click-15%.wav")

def eventHandler(events)-> bool:          # Event handler                                              
    for event in events:
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
        self.surf.fill((5,5,5))
        self.rect = self.surf.get_rect(center=pos)

        self.description = text.lower()

        self.text = mediumFont.render(str(text),True,WHITE)
        self.text_Rect = self.text.get_rect(center=pos)

    def blitSelf(self) -> None:
        
        screen.blit(self.surf,self.rect)
        screen.blit(self.text,self.text_Rect)
        
    def update(self,events) -> None:
        for event in events:
            if event.type == MOUSEMOTION:
                if self.rect.collidepoint(event.pos):
                    self.surf.fill((10,10,20))

                if not self.rect.collidepoint(event.pos):
                    self.surf.fill((0,0,0))

            if event.type == MOUSEBUTTONDOWN:
                if self.rect.collidepoint(event.pos):
                    pygame.mixer.music.play()
            
            if event.type == MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    if self.description == "quit":
                        global running
                        running = False
                    
                    if self.description == "singleplayer":
                        pass
                    if self.description == "multiplayer":
                        pass
                    if self.description == "settings":
                        pass
                    if self.description == "credits":
                        pass



screen = pygame.display.set_mode(FRAMEDIM)


# MENU LABEL ASSIGN

mainTitleLabel = Label((960,240),"Block Dodge","L")


# MENU BUTTON ASSIGN
menuButtons =[
Button((960,400),"Singleplayer"),
Button((960,500),"Multiplayer"),
Button((960,600),"Settings"),
Button((960,700),"Credits"),
Button((960,800),"Quit")
]

#CREITS LABEL ASSIN
creditsTitleLabel = Label((960,240),"Credits","L")




page = PAGES[0]
while running:
    events = pygame.event.get()
    running = eventHandler(events)
    screen.fill((0,0,0))

    

    

    if page == "main":
        mainTitleLabel.blitSelf()
        for i in menuButtons:
            i.blitSelf()
            i.update(events)

    pygame.display.flip()
    clock.tick(FPS)