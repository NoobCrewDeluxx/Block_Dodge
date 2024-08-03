import pygame

maps = ["Terran","Lithos","Glacio","Solaris","Nova"]

for i in maps:
    imageSurf = pygame.image.load(f"assets/visual/MapIcons/NonPixelated/{i}.png")
    imageSurf = pygame.transform.scale(imageSurf,(300*0.25,300*0.25))
    imageSurf = pygame.transform.scale(imageSurf,(300,300))
    pygame.image.save(imageSurf,f"{i}.png")