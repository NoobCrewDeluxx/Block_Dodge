import pygame                       # import modules
from pygame.locals import *
import time
import threading
import os


FPS=60                              # game fps

FRAMEDIM = 1920,1080                # game constants
FRAMECENTRE= 960,540

WHITE = (255,255,255)
BLACK = (0,0,0)

def getImages(folderPath): # this function is from some random guy on stackoverflow, too much effiency for my standards lmao
    filenames = [f for f in os.listdir(folderPath) if f.endswith('.png')]
    images = {}
    for name in filenames:
        imagename = os.path.splitext(name)[0] 
        images[imagename] = pygame.image.load(os.path.join(folderPath, name)).convert_alpha()

    return images


class Label():   # the Label and Button objects are similar to that of the tkinter Label and
                 # button objects in such a way that they can be used anywhere and with extremely
                 # generalised parameters. This also helps with consistency throughout the game so
                 # that my buttons don't look like how I was feeling when I coded them that day

                 # by default the anchor for the label and button is center

    def __init__(self,pos,text,**largs) -> None: 
            
        self.text = largs.get("font",Game.mediumFont).render(text,True,(255,255,255)) # defaults to medium font
        self.text_rect = self.text.get_rect()
        setattr(self.text_rect,largs.get("anchor","center"),pos)
        
    def render(self):                              
        Game.screen.blit(self.text,self.text_rect)




class Button():
    
    def __init__(self,pos,text,**bargs) -> None:
        

        self.anchor = bargs.get("anchor","center")              # Default Anchor = Center
        self.buttonsize = bargs.get("size",(200,50))            # Default Size = 200 wide ,50 high
        self.name = bargs.get("name", None)                     # Default Name = None
        self.alpha = bargs.get("alpha", 255)                    # Default Alpha = 255

        self.surf = pygame.Surface(self.buttonsize)
        self.surf.fill((5,5,5))
        self.rect = self.surf.get_rect()
        setattr(self.rect,self.anchor,pos)

        self.description = text.lower()

        self.text = Game.mediumFont.render(text,True,(255,255,255))
        self.text_rect = self.text.get_rect()
        setattr(self.text_rect,self.anchor,pos)

        self.surf.set_alpha(self.alpha)

    def render(self) -> None:
        Game.screen.blit(self.surf,self.rect)
        Game.screen.blit(self.text,self.text_rect)
             
    def run(self ,game ,events: list) -> None:
        mousepos = pygame.mouse.get_pos()
        
        if not self.rect.collidepoint(mousepos):
            self.surf.fill((0,0,0))

        for event in events: # the great wall of button events, could be made SO much more efficient
                             # however, it works how it is and if I touch one thing it just completely breaks everything
                             # each button identifier has its own set of statements and conditionals so everybutton doesnt
                             # do the same thing, if I put the mouse hover highlight outside of an Identifier then it would 
                             # highlight all buttons rather than just the one the user is hovering.

            if self.description == "quit": # Button identifier
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1: # Event conditional statement
                    pygame.mixer.music.play()                               
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1: # Event conditional statement
                    game.running = False
                if self.rect.collidepoint(mousepos):                                                    # Mouse hover highlight
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

            elif self.description =="select" and game.currentMenu == "singleplayer":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.ingame_running = True
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif (self.description =="next" and game.currentMenu == "singleplayer") or self.name == "sPlay_right":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.singleplayerMenu.prevMapCard += 1
                    game.singleplayerMenu.selMapCard += 1
                    game.singleplayerMenu.nextMapCard += 1
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif (self.description =="previous" and game.currentMenu == "singleplayer") or self.name == "sPlay_left":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                    self.surf.fill((20,20,30))
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    game.singleplayerMenu.prevMapCard -= 1
                    game.singleplayerMenu.selMapCard -= 1
                    game.singleplayerMenu.nextMapCard -= 1
                if self.rect.collidepoint(mousepos):
                    self.surf.fill((10,10,20))

            elif self.name=="sPlay_center":
                if event.type == MOUSEBUTTONDOWN and self.rect.collidepoint(mousepos) and event.button==1:
                    pygame.mixer.music.play()
                if event.type == MOUSEBUTTONUP and self.rect.collidepoint(mousepos) and event.button==1:
                    if game.singleplayerMenu.flipCard:
                        game.singleplayerMenu.flipCard =False
                    else: game.singleplayerMenu.flipCard = True







class main_menu():  # menu class type objects: they are the defining parts of the game that allow me to easily organise 
                    # different menus and objects. Generally speaking they are self-sufficient meaning they define and manage 
                    # their own variables only needing to be externally ran by the Game() class. An exception to this applies 
                    # to the in_game() class.

    def __init__(self) -> None:
        self.labels = [
            Label((960,240),"Block Dodge",font=Game.largeFont)

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
class Slider: # Slider, W.I.P similar to the Button and Labels in that they can be used anywhere with general parameters
              # iirc there is a similar class type object in tkinter. The majority of the code in __init__ was made by a
              # guy who did a tutorial on yt
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

    def move_slider(self,mouse_pos): 
        # moves slider button rect to mouse x position if mouse button 1 is down in the container rect and checks too see if slider button rect is outside container rect x value. Y value is unaffected

        if self.button_rect.left >= self.container_rect.left and self.button_rect.right <= self.container_rect.right:
                self.button_rect.centerx = mouse_pos[0]

        if self.button_rect.left < self.container_rect.left:
            self.button_rect.left = self.container_rect.left

        if self.button_rect.right > self.container_rect.right:
            self.button_rect.right = self.container_rect.right
        
    def render(self, screen):
        pygame.draw.rect(screen,"darkgray", self.container_rect)
        pygame.draw.rect(screen,"blue", self.button_rect)

    def get_value(self):
        val_range = self.slider_right_pos - self.slider_left_pos
        button_val  = self.button_rect.centerx - self.slider_left_pos 

        return (button_val/val_range)*(self.max-self.min)+self.min


class singleplayer_menu():
    class mapCard():               # Sub Class use: I use sub classes to organise code even further than before. i.e mapCard isn't used
                                   # by any other class in the whole file so why put it outside singpleplayer_menu().
        def __init__(self, map: str) -> None:
            self.mapName = map

            self.mapImage = pygame.image.load(f"Game/assets/visual/MapCards/Previews/Pixelated/{map}.png")
            self.mapDesc = pygame.image.load(f"Game/assets/visual/MapCards/Descriptions/{map}.png")
            self.scaledMapImage = pygame.image.load(f"Game/assets/visual/MapCards/Previews/Pixelated/{map}.png")
            
            self.scaledMapImage = pygame.transform.scale_by(self.scaledMapImage,0.75)

            self.scaledMapImage_Rect = self.scaledMapImage.get_rect()
            self.mapDesc_Rect = self.mapDesc.get_rect()
            self.mapImage_Rect = self.mapImage.get_rect()
            
            
            self.mapImageBG = pygame.image.load(f"Game/assets/visual/MenuBG/Blur/{map}.png")
            self.mapImageBG.set_alpha(90)
            self.mapImage_RectBG = self.mapImageBG.get_rect(center=FRAMECENTRE)

        # different render functions exist in the mapCard object purely to render scaled versions of the large image to different locations. It prevents a large amount of loading that could have been possible
        # if a different approach was taken. This method loads 18 images, 12 scaled down 0.75x, 6 kept normal resolution. It can be time consuming switching to different methods. If it works it works.
        
        def renderBG(self):
            Game.screen.blit(self.mapImageBG,self.mapImage_RectBG)
            self.desc = None

        def renderCenter(self):
            self.mapImage_Rect.center = (960,500)
            Game.screen.blit(self.mapImage,self.mapImage_Rect)
            
        def renderLeft(self):
            self.scaledMapImage_Rect.center = (660,500)
            Game.screen.blit(self.scaledMapImage,self.scaledMapImage_Rect)

        def renderRight(self):
            self.scaledMapImage_Rect.center = (1260,500)
            Game.screen.blit(self.scaledMapImage,self.scaledMapImage_Rect)

        def renderDesc(self):
            self.mapDesc_Rect.center = (960,500)
            Game.screen.blit(self.mapDesc,self.mapDesc_Rect)

    
    def __init__(self) -> None:
        # selectors will define which map 
        self.prevMapCard = 4
        self.selMapCard = 0
        self.nextMapCard = 1

        self.flipCard = False

        self.labels = [
            Label((960,100),"Select Map",font=Game.largeFont)

        ]

        self.buttons = [
            Button((1110,900),"Next"),
            Button((810,900),"Previous"),
            Button((100,980),"Return"),
            Button((960,1000),"Select"),
            Button((660,500),"",name="sPlay_left",size=(300,600),alpha=0),      # a "name" keyword argument was used to prevent text from being displayed, despite the fact mapCards are rendered ontop of the Buttons. 
            Button((1260,500),"",name="sPlay_right",size=(300,600),alpha=0),    # note the size keyword arguement, which I specifically implemented for this use case. It may be used in the future which is why I fully implemented it
            Button((960,500),"",name="sPlay_center",size=(300,600),alpha=0),    # also note that I used the **kwargs parameter method so I did not have to have to change the arguments for every Button and Label object.
        ]

        self.mapCards = [               # list of mapCard objects
            self.mapCard("Terran"),
            self.mapCard("Lithos"),
            self.mapCard("Glacio"),
            self.mapCard("Solaris"),
            self.mapCard("Nova")
        ]
         
    def boundaryFix(self,boundLeft: int,number: int, boundRight:int ): 
        # boundLeft is by default 0 (the start of every list), number is the number being checked, boundRight is the length of the list of which the number is being checked against
        if number < boundLeft:
            number = boundRight
            
        if number > boundRight:
            number = boundLeft

        return number

    def run(self,game,events):

        # to prevent list of out of bounds error we check that the selector isn't outside of the length of items inside self.mapCards list, which contains the mapCard objects
        self.prevMapCard = self.boundaryFix(0, self.prevMapCard, len(self.mapCards)-1)
        self.selMapCard = self.boundaryFix(0, self.selMapCard, len(self.mapCards)-1)
        self.nextMapCard = self.boundaryFix(0, self.nextMapCard, len(self.mapCards)-1)

        self.selMapName = str(self.mapCards[self.selMapCard].mapName)
        
        

        self.mapCards[self.selMapCard].renderBG()
        # to prevent abnormal visiuals we want the buttons to be rendered after the background but not before the mapCards

        for button in self.buttons:     
            button.render()

        self.mapCards[self.prevMapCard].renderLeft()
        self.mapCards[self.selMapCard].renderCenter()
        self.mapCards[self.nextMapCard].renderRight()


        # renders map description ontop of map preview if the flipCard value is set to true via the button conditional statements
        if self.flipCard:
            self.mapCards[self.selMapCard].renderDesc()
        


        # selMapCard, prevMapCard, and nextMapCard updaters must go after this or before boundary fixing to prevent list out of range error

        for button in self.buttons:
            button.run(game, events)

        for label in self.labels:
            label.render()


class multiplayer_menu():
    def __init__(self) -> None:
        self.labels = [
            Label((960,100),"Multiplayer",font=Game.largeFont),
            Label((960,200),"W.I.P",font=Game.largeFont)

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
            Label((300,100),"Settings",font=Game.largeFont),
            Label((300,200),"W.I.P",font=Game.largeFont)

        ]

        self.sliders = [
            Slider(pos=(960,500),size=(400,10),button_width=10,initial_val=0.5,min=0,max=100),
            Slider(pos=(960,600),size=(200,50),button_width=10,initial_val=0.5,min=0,max=100),
            Slider(pos=(960,700),size=(100,30),button_width=10,initial_val=0.5,min=0,max=100),
            Slider(pos=(960,800),size=(700,50),button_width=10,initial_val=0.5,min=0,max=100)


            ]
        
        self.buttons = [
            Button((100,980),"Return")

        ]
    def run(self,game,events):
        for label in self.labels:
            label.render()
        
        mouse_pos = pygame.mouse.get_pos()
        for slider in self.sliders:
            slider.render(Game.screen)
            if pygame.mouse.get_pressed()[0] and slider.container_rect.collidepoint(mouse_pos):
                slider.move_slider(mouse_pos)
                
                print(round(slider.get_value()))


        for button in self.buttons:
            button.run(game, events)
            button.render()
            

class credits_menu():
    def __init__(self) -> None:
        self.labels = [
            Label((960,240),"Credits",font=Game.largeFont),
            Label((960,400),"Lead Development: Joseph Wilson",font=Game.mediumFont),
            Label((960,500),"Visuals: Joseph Wilson",font=Game.mediumFont),
            Label((960,600),"Music: RE-Logic",font=Game.mediumFont),
            Label((960,700),"Programming: Joseph Wilson",font=Game.mediumFont),
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

class in_game():                        # I use subclasses to an extreme amount here, probably unnecessary, however I can define variables
                                        # for different movement methods without having to place large ugly if statements everywhere
                                        # the variable set for each movement method is also resuable.

    class Player(pygame.sprite.Sprite):

        class Human(pygame.sprite.Sprite):
            def __init__(self) -> None:
                pass

        class Rover(pygame.sprite.Sprite):
            speed = 10 # pixels per tick
            boostSpeed = 10 #pixels per tick boost
            health = 100 # hitpoints before death
            energy = 10 # MegaWatts of power
            armor = 50 # Armorpoints

            def __init__(self) -> None:
                pass

        class Ship(pygame.sprite.Sprite):
            def __init__(self) -> None:

                # base attributes:
                self.speed = 10 # pixels per tick
                self.boostSpeed = 10 #pixels per tick boost
                self.health = 100 # hitpoints before death
                self.fuel = 100 # Liters of fuel
                self.energy = 100 # MegaWatts of power
                self.energy_per_shield_weak_hit = 1 # MegaWatts pf power
                self.energy_per_shield_medium_hit = 5 # MegaWatts of power
                self.energy_per_shield_medium_hit = 10 # MegaWatts of power
                self.fuelUsage = 0.01 # L per second



                self.images = getImages("Game/assets/visual/Sprites/player/stream")
                for image in self.images:
                    surf = self.images[image]
                    surf = pygame.transform.scale_by(surf,0.25)
                    surf = pygame.transform.rotate(surf,-90)
                    surf_size = surf.get_size()

                    self.images[image] = surf
                self.rect = pygame.Rect(300,Game.screen.get_size()[1]/2,surf_size[0],surf_size[1])
            
        def __init__(self, game, map) -> None:
            
            if map == "Nova":
                self.Ship.__init__(self)

            self.gameoverText = Game.largeFont.render("Game Over", True, (255,255,255))
            self.gameoverText_rect = self.gameoverText.get_rect(center=(960,540))

        def run(self, game, screen, events) -> None:
            pressed_keys = pygame.key.get_pressed()
            
            frame = 'ship_thrust_off'
            frameSpeed = 'slow' # default ship speed
            shipSpeed = self.speed
            fuelUsage = self.fuelUsage
            
            if pressed_keys[K_SPACE]:
                frameSpeed = 'fast'
                shipSpeed = self.speed+self.boostSpeed
                fuelUsage = self.fuelUsage * 5

            if self.fuel > 0:
                if pressed_keys[K_RIGHT]:
                    frame = f'ship_thrust_{frameSpeed}_forward'
                    game.ingame.distanceTravelled += shipSpeed/10
                    self.fuel -= fuelUsage

                if pressed_keys[K_UP]:
                    self.rect.move_ip(0, -shipSpeed)
                    frame = f'ship_thrust_{frameSpeed}_right'
                    self.fuel -= fuelUsage

                if pressed_keys[K_DOWN]:
                    self.rect.move_ip(0, shipSpeed)
                    frame = f'ship_thrust_{frameSpeed}_left'
                    self.fuel -= fuelUsage

                self.fuel -= self.fuelUsage/10
                game.ingame.distanceTravelled += shipSpeed/100

            else: 
                screen.blit(self.gameoverText,self.gameoverText_rect)

            screen.blit(self.images[f'{frame}'],self.rect)

            if self.rect.left < 0:
                self.rect.left = 0
            if self.rect.right > screen.get_size()[0]:
                self.rect.right = screen.get_size()[0]
            if self.rect.top <= 0:
                self.rect.top = 0
            if self.rect.bottom >= screen.get_size()[1]:
                self.rect.bottom = screen.get_size()[1]

        def getImages(folderPath): # this function is from some random guy on stackoverflow, too much effiency for my standards lmao
            filenames = [f for f in os.listdir(folderPath) if f.endswith('.png')]
            images = {}
            for name in filenames:
                imagename = os.path.splitext(name)[0] 
                images[imagename] = pygame.image.load(os.path.join(folderPath, name)).convert_alpha()

            return images
        



    class Enemy():
        def __init__(self) -> None:
            pass


    def __init__(self,game, selectedMap: str) -> None:
        self.player = self.Player(game,selectedMap)
        self.screen = Game.screen
        self.distanceTravelled = 0
        self.fuelUsed = round(self.player.fuel,2)
        self.selectedMap = selectedMap
        self.running = True
        self.game = game

        self.background=pygame.image.load(f"Game/assets/visual/IngameBackgrounds/Pixelated/{selectedMap}.png")
        self.background.set_alpha(100)
        self.Labels = [
            Label((1900,1060),f"Distance: {self.distanceTravelled}"),
            Label((20,20),f"Fuel: {self.fuelUsed} %")


        ]

    def run(self):
        while self.running: # additionally to having a surplus of subclasses in_game() runs its own game loop that allows for better
                            # performance when playing in game, this is because the game does not have to run through additional
                            # irelavent objects and if statements before it reasches the ingame.run() statement
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN and event.key == K_ESCAPE or event.type== QUIT:
                    self.running=False
                    exit()

            self.screen.fill((0,0,0))
            self.screen.blit(self.background,(0,0))

            

            self.player.run(self.game,self.screen,events)

            self.distanceTravelled=round(self.distanceTravelled,1)
            self.fuelUsed = round(self.player.fuel,2)

            self.Labels

            dTSurf = Game.mediumFont.render(f"Distance: {self.distanceTravelled} Km", True, (255,255,255))
            dTSurf_rect = dTSurf.get_rect()
            dTSurf_rect.topright = (1900,20)

            fuelSurf = Game.mediumFont.render(f"Fuel: {self.fuelUsed} %", True, (255,255,255))
            fuelSurf_rect = fuelSurf.get_rect()
            fuelSurf_rect.topleft = (20,20)

            self.screen.blit(dTSurf,dTSurf_rect)
            self.screen.blit(fuelSurf,fuelSurf_rect)



            pygame.display.flip()
            Game.clock.tick(FPS)
        



class Game():  # all game constants are stored in this easier than globals class. It allows me to access any of the variables anywhere
               # in the file. Although it may be seen as contemporary, i see it as useful thus why it exists. (I was also running into
               # problems with the main game loop and varibles and such in the root class
    pygame.init()
    pygame.mixer.init()
    pygame.font.init()
    pygame.mixer.music.load("Game/assets/audio/click-75%.wav")
    largeFont = pygame.font.SysFont("courier-new",50)
    mediumFont = pygame.font.SysFont("courier-new",25)
    smallFont = pygame.font.SysFont("courier-new",20,True)
    screen = pygame.display.set_mode(size=(1920,1080),vsync=1,display=0)
    clock = pygame.time.Clock()
    Maps = ("Terran","Lithos","Glacio","Solaris","Nova")
    def __init__(self) -> None:
        
        self.running = True
        self.menus = ("main","singleplayer","multiplayer","settings","credits")
        self.currentMenu = self.menus[0]
        self.mainMenu = main_menu()
        self.singleplayerMenu = singleplayer_menu()
        self.settingsMenu = settings_menu()
        self.creditsMenu = credits_menu()
        self.multiplayerMenu = multiplayer_menu()
        self.ingame_running = False
        self.selectedMap = None


    def run(self):
        while self.running:
            self.events = pygame.event.get()
            for event in self.events:
                if event.type == KEYDOWN and event.key == K_ESCAPE or event.type== QUIT:
                    self.running=False
                    exit()
            self.screen.fill((0,0,0))

            if self.ingame_running == False:
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

            elif self.ingame_running and self.singleplayerMenu.selMapName == "Nova": #in self.Maps once other maps get added
                self.ingame = in_game(self,self.singleplayerMenu.selMapName)
                self.ingame.run()
                self.ingame_running = None
            
            else: self.ingame_running = False
            
            pygame.display.flip()
            self.clock.tick(FPS)

game = Game()
game.run()