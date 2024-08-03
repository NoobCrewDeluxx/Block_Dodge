import pygame                       # import modules
from pygame.locals import *
import time
import threading

FPS=60                              # game fps

FRAMEDIM = 1920,1080                # game constants
FRAMECENTRE= 960,540

BUTTONSIZE = (200,50)

WHITE = (255,255,255)
BLACK = (0,0,0)



class Error(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

class Label():
    def __init__(self,pos: tuple,text: str,font: pygame.font.Font) -> None:
            
        self.text = font.render(text,True,WHITE)
        self.text_rect = self.text.get_rect(center=pos)
        
    def render(self):             # Method to render text onto the screen to reduce cluttering in essential areas
        Game.screen.blit(self.text,self.text_rect)

class Button():
    def __init__(self,pos: tuple,text: str) -> None:

        self.surf = pygame.Surface(BUTTONSIZE)
        self.surf.fill((5,5,5))
        self.rect = self.surf.get_rect(center=pos)

        self.description = text.lower()

        self.text = Game.mediumFont.render(text,True,WHITE)
        self.text_Rect = self.text.get_rect(center=pos)

    def render(self) -> None:
        Game.screen.blit(self.surf,self.rect)
        Game.screen.blit(self.text,self.text_Rect)
             
    def run(self ,game ,events: list) -> None:
        global running
        mousepos = pygame.mouse.get_pos()
        mousepressed = pygame.mouse.get_pressed()[0]
        
        if not self.rect.collidepoint(mousepos):
            self.surf.fill((0,0,0))

        for event in events:
            if self.description == "quit":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    running = False
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))
        
            elif self.description == "singleplayer":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.currentMenu = game.menus[1]
                    self.surf.fill((0,0,0))
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.description == "multiplayer":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.currentMenu = game.menus[2]
                    self.surf.fill((0,0,0))
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.description == "settings":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.currentMenu = game.menus[3]
                    self.surf.fill((0,0,0))
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.description == "credits":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.currentMenu = game.menus[4]
                    self.surf.fill((0,0,0))
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.description == "return":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.currentMenu = game.menus[0]
                    self.surf.fill((0,0,0))
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.description =="next" and game.currentMenu == "singleplayer":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.singleplayerMenu.prevMapCard += 1
                    game.singleplayerMenu.selMapCard += 1
                    game.singleplayerMenu.nextMapCard += 1
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.description =="previous" and game.currentMenu == "singleplayer":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.singleplayerMenu.prevMapCard -= 1
                    game.singleplayerMenu.selMapCard -= 1
                    game.singleplayerMenu.nextMapCard -= 1
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))


class Slider:
    def __init__(self, pos: tuple, size: tuple, button_width: int, initial_val: float, min: int, max: int) -> None:
        self.pos = pos
        self.size = size 
        self.button_width = button_width

        self.max = max
        self.min = min
        
        self.slider_left_pos = self.pos[0] - (size[0]//2)
        self.slider_right_pos = self.pos[0] + (size[0]//2)
        self.slider_top_pos = self.pos[1] - (size[1]//2)

        self.initial_val = (self.slider_right_pos-self.slider_left_pos)*initial_val

        self.clicked = False

        self.container_rect = pygame.Rect(self.slider_left_pos, self.slider_top_pos, self.size[0], self.size[1])
        self.button_rect = pygame.Rect(self.slider_left_pos+self.initial_val - 5, self.slider_top_pos, self.button_width, self.size[1])

    def move_slider(self,events,mouse_pos,mouse_pressed):

        if self.clicked and self.button_rect.left >= self.container_rect.left and self.button_rect.right <= self.container_rect.right:
            self.button_rect.centerx = mouse_pos[0]

        if self.button_rect.left < self.container_rect.left-1:
            self.button_rect.left = self.container_rect.left-1

        if self.button_rect.right > self.container_rect.right+1:
            self.button_rect.right = self.container_rect.right+1

        if mouse_pressed and self.container_rect.collidepoint(mouse_pos):
            self.clicked = True
        
        for event in events:
            if event.type == MOUSEBUTTONUP:
                self.clicked = False

    def render(self, screen):
        pygame.draw.rect(screen,"darkgray", self.container_rect)
        pygame.draw.rect(screen,"blue", self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val  = self.button_rect.centerx - self.slider_left_pos 

        return (button_val/val_range)*(self.max-self.min)+self.min


class main_menu():
    def __init__(self) -> None:
        self.labels = [
            Label((960,240),"Block Dodge",Game.largeFont)

        ]
        
        self.buttons = [
            Button((960,400),"Singleplayer"),
            Button((960,500),"Multiplayer"),
            Button((960,600),"Settings"),
            Button((960,700),"Credits"),
            Button((960,800),"Quit")

        ]
    def run(self,game,events):
        for label in self.labels:
            label.render()

        for button in self.buttons:
            button.render()
            button.run(game,events)


class singleplayer_menu():
    class mapCard():
        def __init__(self,map: pygame.surface) -> None:

            self.mapImage = pygame.image.load(f"assets/visual/MapCards/Pixelated/{map}.png")
            self.scaledMapImage = pygame.image.load(f"assets/visual/MapCards/Pixelated/{map}.png")
            
            self.scaledMapImage = pygame.transform.scale_by(self.scaledMapImage,0.75)

            self.scaledMapImage_Rect = self.scaledMapImage.get_rect()
            self.mapImage_Rect = self.mapImage.get_rect()
            
            
            self.mapImageBG = pygame.image.load(f"assets/visual/MenuBG/Blur/{map}.png")
            self.mapImageBG.set_alpha(90)
            self.mapImage_RectBG = self.mapImageBG.get_rect(center=FRAMECENTRE)
        
        def renderBG(self):
            Game.screen.blit(self.mapImageBG,self.mapImage_RectBG)

        def renderCenter(self):
            self.mapImage_Rect.center = (960,500)
            Game.screen.blit(self.mapImage,self.mapImage_Rect)
            
        def renderLeft(self):
            self.scaledMapImage_Rect.center = (660,500)
            Game.screen.blit(self.scaledMapImage,self.scaledMapImage_Rect)

        def renderRight(self):
            self.scaledMapImage_Rect.center = (1260,500)
            Game.screen.blit(self.scaledMapImage,self.scaledMapImage_Rect)

        
    
    def __init__(self) -> None:
        self.prevMapCard = 4
        self.selMapCard = 0
        self.nextMapCard = 1

        self.labels = [
            Label((960,100),"Singleplayer",Game.largeFont)

        ]

        self.buttons = [
            Button((1110,900),"Next"),
            Button((810,900),"Previous"),
            Button((100,980),"Return")

        ]

        self.mapCards = [
            self.mapCard("Terran"),
            self.mapCard("Lithos"),
            self.mapCard("Glacio"),
            self.mapCard("Solaris"),
            self.mapCard("Nova"),
        ]

        self.backgrounds = [


        ]

    def boundaryFix(self,boundLeft: int,number: int, boundRight:int ):
        if number < boundLeft:
            number = boundRight
            
        if number > boundRight:
            number = boundLeft

        return number

    def run(self,game,events):
        self.prevMapCard = self.boundaryFix(0, self.prevMapCard, 4)
        self.selMapCard = self.boundaryFix(0, self.selMapCard, 4)
        self.nextMapCard = self.boundaryFix(0, self.nextMapCard, 4)

        self.mapCards[self.selMapCard].renderBG()
        self.mapCards[self.prevMapCard].renderLeft()
        self.mapCards[self.selMapCard].renderCenter()
        self.mapCards[self.nextMapCard].renderRight()
        

        for label in self.labels:
            label.render()

        for button in self.buttons:
            button.render()
            button.run(game, events)


class multiplayer_menu():
    def __init__(self) -> None:
        self.labels = [
            Label((960,100),"Multiplayer",Game.largeFont)

        ]
        self.buttons = [
            Button((100,980),"Return")

        ]
    
    def run(self,game,events):
        for label in self.labels:
            label.render()

        for button in self.buttons:
            button.run(game,events)
            button.render()


class settings_menu():
    def __init__(self) -> None:

        self.labels = [
            Label((300,100),"Settings",Game.largeFont)

        ]

        self.sliders = [
            Slider(pos=(300,500),size=(400,10),button_width=10,initial_val=0.5,min=0,max=100)

            ]
        
        self.buttons = [
            Button((100,980),"Return")

        ]
    def run(self,game,events):
        for label in self.labels:
            label.render()

        for slider in self.sliders:
            slider.move_slider(events,pygame.mouse.get_pos(),pygame.mouse.get_pressed()[0])
            slider.render(Game.screen)
            print(round(slider.get_value()))

        for button in self.buttons:
            button.run(game, events)
            button.render()
            

class credits_menu():
    def __init__(self) -> None:
        self.labels = [
            Label((960,240),"Credits",Game.largeFont),
            Label((960,400),"Lead Development: Joseph Wilson",Game.mediumFont),
            Label((960,500),"Visuals: Joseph Wilson",Game.mediumFont),
            Label((960,600),"Music: RE-Logic",Game.mediumFont),
            Label((960,700),"Programming: Joseph Wilson",Game.mediumFont),
        ]

        self.buttons = [
            Button((100,980),"Return")
        ]

    def run(self,game,events):
        for label in self.labels:
            label.render()

        for button in self.buttons:
            button.render()
            button.run(game, events)

    

class Game():
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer.music.load("assets/audio/click-75%.wav")
    largeFont = pygame.font.SysFont("courier-new",50)
    mediumFont = pygame.font.SysFont("courier-new",25)
    smallFont = pygame.font.SysFont("courier-new",20,True)
    screen = pygame.display.set_mode(size=(1920,1080),vsync=1,display=1)

    def __init__(self) -> None:
        
        self.running = True
        self.clock = pygame.time.Clock()
        self.menus = ("main","singleplayer","multiplayer","settings","credits","in_game")
        self.currentMenu = self.menus[0]
        self.mainMenu = main_menu()
        self.singleplayerMenu = singleplayer_menu()
        self.settingsMenu = settings_menu()
        self.creditsMenu = credits_menu()
        self.multiplayerMenu = multiplayer_menu()


    def run(self):
        while self.running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == KEYDOWN and event.key == K_ESCAPE or event.type== QUIT:
                    self.running=False
                    exit()
            self.screen.fill((0,0,0))

            if self.currentMenu == "main":
                self.mainMenu.run(self,self.events)
                            
            elif self.currentMenu == "singleplayer":
                self.singleplayerMenu.run(self,self.events)

            elif self.currentMenu == "multiplayer":
                self.multiplayerMenu.run(self,self.events)

            elif self.currentMenu == "settings":
                self.settingsMenu.run(self,self.events)

            elif self.currentMenu == "credits":
                self.creditsMenu.run(self,self.events)
            

            pygame.display.flip()
            self.clock.tick(FPS)

game = Game()
game.run()