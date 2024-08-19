import pygame
import os


# FOR SPRITES THAT HAVE VARIOIUS ACTION FRAMES

def getImages(folderPath): # this function is from some random guy on stackoverflow, too much effiency for my standards lmao
    filenames = [f for f in os.listdir(folderPath) if f.endswith('.png')]
    images = {}
    for name in filenames:
        imagename = os.path.splitext(name)[0] 
        images[imagename] = pygame.image.load(os.path.join(folderPath, name)).convert_alpha()
    return images


# # # # # # ENEMY VARIANTS # # # # # #

class Small_Asteroid():
    def __init__(self,y_position, game):
        pygame.sprite.Sprite.__init__(self,)
        self.damage = 1
        self.speed = 20
        self.surf = pygame.image.load("Game/assets/visual/Sprites/Enemey/Asteroid1.png")
        self.surf = pygame.transform.scale_by(self.surf,0.2)
        self.rect = self.surf.get_rect(center=(game.screen.get_size()[0]+(self.surf.get_size()[0]/2),y_position))
        print(f"new small asteroid spawned with size:{self.surf.get_size()} and at position: {self.rect.center}")
        
class Medium_Asteroid():
    def __init__(self, y_position, game):
        pygame.sprite.Sprite.__init__(self)
        self.damage = 5
        self.speed = 15
        self.surf = pygame.image.load("Game/assets/visual/Sprites/Enemey/Asteroid1.png")
        self.surf = pygame.transform.scale_by(self.surf,0.4)
        self.rect = self.surf.get_rect(center=(game.screen.get_size()[0]+(self.surf.get_size()[0]/2),y_position))
        print(f"new medium asteroid spawned with size:{self.surf.get_size()} and at position: {self.rect.center}")
        
class Large_Asteroid():
    def __init__(self, y_position, game):
        pygame.sprite.Sprite.__init__(self)
        self.damage = 10
        self.speed = 10
        self.surf = pygame.image.load("Game/assets/visual/Sprites/Enemey/Asteroid1.png")
        self.surf = pygame.transform.scale_by(self.surf,0.6)
        self.rect = self.surf.get_rect(center=(game.screen.get_size()[0]+(self.surf.get_size()[0]/2),y_position))
        print(f"new large asteroid spawned with size:{self.surf.get_size()} and at position: {self.rect.center}")



# # # # # # PLAYER VARIANTS # # # # # #

class Human():
    def __init__(self, game) -> None:
        pygame.sprite.Sprite.__init__(self)


class Rover():
    speed = 10 # pixels per tick
    boostSpeed = 10 #pixels per tick boost
    health = 100 # hitpoints before death
    energy = 10 # MegaWatts of power
    armor = 50 # Armorpoints
    def __init__(self, game) -> None:
        pygame.sprite.Sprite.__init__(self)


class Ship():
    def __init__(self, game) -> None:
        pygame.sprite.Sprite.__init__(self)
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
        self.images = getImages("Game/assets/visual/Sprites/player/stream") # load all frames for the ship into ram so that they are ready for use and can be switched fast and easy
        for image in self.images:
            surf = self.images[image]
            surf = pygame.transform.scale_by(surf,0.25)
            surf = pygame.transform.rotate(surf,-90)
            surf_size = surf.get_size()
            self.images[image] = surf
        self.rect = pygame.Rect(300,game.screen.get_size()[1]/2,surf_size[0],surf_size[1])