import pygame

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 200

okno = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

timer = pygame.time.Clock()

program_going = True

def load_image(image_path, position):
    # 1 nacist obrazek ze souboru
    image = pygame.image.load(image_path)
    # 2 nastavit pozici
    rect = image.get_rect(center=position)
    return image, rect

obrazek, pozice = load_image("lesson12/obrazek.png", (200,100))

while program_going:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            program_going = False
    
    
    okno.blit(obrazek, pozice)

    pygame.display.update()

    timer.tick(30)

pygame.quit()