import pygame

pygame.init()

display_surface = pygame.display.set_mode((600,400))
pygame.display.set_caption("My First Pygame Window")

white = (255,255,255)
blue = (0, 85, 164)
red = (239, 65, 53)
running = True

while running == True : 

    display_surface.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False 
    pygame.draw.rect(display_surface, blue, (0,0,200,400))
    pygame.draw.rect(display_surface, white, (200,0,200,400))
    pygame.draw.rect(display_surface, red, (400,0,200,400))       
    pygame.display.update()
pygame.quit()

