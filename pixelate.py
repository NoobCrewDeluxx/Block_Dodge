import pygame

maps = ["Terran","Lithos","Glacio","Solaris","Nova"]

for i in maps:
    imageSurf = pygame.image.load(f"assests/visual/MapIcons/{i}.png")
    imageSurf = pygame.transform.scale(imageSurf,(300*0.5,300*0.5))
    imageSurf = pygame.transform.scale(imageSurf,(300,300))
    pygame.image.save(imageSurf,f"{i}.png")