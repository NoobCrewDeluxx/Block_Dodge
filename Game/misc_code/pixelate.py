import pygame

imageSurf = pygame.image.load(f"Game/Nova.png")
imageSurf = pygame.transform.scale(imageSurf,(1920,1080))
imageSurf = pygame.transform.scale_by(imageSurf,(0.5))
imageSurf = pygame.transform.scale(imageSurf,(1920,1080))
#imageSurf = pygame.transform.scale(imageSurf,(300,300))
pygame.image.save(imageSurf,f"Nova.png")
