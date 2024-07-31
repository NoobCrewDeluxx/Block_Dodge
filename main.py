import pygame                       # import modules
from pygame.locals import *

FPS=60                              # game fps

FRAMEDIM = 1920,1080                # game constants
FRAMECENTRE= 960,540

BUTTONSIZE = (200,50)

WHITE = (255,255,255)
BLACK = (0,0,0)

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
                    self.surf.fill((20,20,30))
            
            if event.type == MOUSEBUTTONUP:
                if self.rect.collidepoint(event.pos):
                    self.surf.fill((10,10,20))
                    global page
                    if self.description == "quit":
                        global running
                        running = False
                    
                    elif self.description == "singleplayer":
                        page = PAGES[1]
                        
                    elif self.description == "multiplayer":
                        page = PAGES[2]
                        
                    elif self.description == "settings":
                        page = PAGES[3]
                        
                    elif self.description == "credits":
                        page = PAGES[4]

                    elif self.description == "return":
                        page = PAGES[0]

                    else: print("lol idk what ur clicking")

screen = pygame.display.set_mode(FRAMEDIM)

# MENU LABEL ASSIGN

mainTitleLabel = Label((960,240),"Block Dodge","L")

# MENU BUTTON ASSIGN
mainMenuButtons =[
    Button((960,400),"Singleplayer"),
    Button((960,500),"Multiplayer"),
    Button((960,600),"Settings"),
    Button((960,700),"Credits"),
    Button((960,800),"Quit")
]

#CREDITS LABEL ASSIGN
creditsMenuLabels =[
    Label((960,240),"Credits","L"),
    Label((960,400),"Lead Development: Joseph Wilson","M"),
    Label((960,500),"Visuals: Joseph Wilson","M"),
    Label((960,600),"Music: RE-Logic","M"),
    Label((960,700),"Programming: Joseph Wilson","M"),
]

#GENERAL RETURN BUTTON ASSIGN
returnButton = Button((100,980),"Return")

#SINGLEPLAYER LABEL ASSIGN
splayMenuTitle = Label((960,140),"Singleplayer","L")

#SINGPLEPLAYER FRAME ASSIGN
#Complex pages such as singplayer menu with many different elements
#will use "frames" to hold stuff that are similar but are repitively used

class mapPreview():
    def __init__(self,text) -> None:
        self.FRAMESIZE = (300,350)

        self.surf = pygame.Surface(self.FRAMESIZE) #Frame Size
        self.surf.fill((10,10,10))
        self.rect = self.surf.get_rect(center=(960,400))

        
        self.mapImage = pygame.image.load(f"assests/visual/MapIcons/Terran.png")
        self.mapImage_Rect = self.mapImage.get_rect(center=(960,375))
        
        self.text=mediumFont.render(str(text),True,WHITE)
        self.text_Rect = self.text.get_rect(center=(960,500))

        #self.PreviewNextButton = pygame.Surface()

    def blitSelf(self):
        screen.blit(self.surf,self.rect)
        screen.blit(self.mapImage,self.mapImage_Rect)
        screen.blit(self.text,self.text_Rect)
        
    def update(self,events,infocus):
        pass





page = PAGES[0]
mapSelections = [
    mapPreview("Nova"),
    mapPreview("Solaris"),
    mapPreview("Terran"),
    mapPreview("Glacio"),
    mapPreview("Lithos"),

]

while running:
    events = pygame.event.get()
    running = eventHandler(events)
    screen.fill((0,0,0))

    if page == "main":
        mainTitleLabel.blitSelf()
        for i in mainMenuButtons:
            i.blitSelf()
            i.update(events)
            
    elif page == "credits":
        for i in creditsMenuLabels:
            i.blitSelf()

    elif page == "singleplayer":
        splayMenuTitle.blitSelf()
        mapSelections[2].blitSelf()

    if page != "main":
        returnButton.blitSelf()
        returnButton.update(events)

    
            

    pygame.display.flip()
    clock.tick(FPS)