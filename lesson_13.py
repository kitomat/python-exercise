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

obrazek, pozice = load_image("obrazek.png", (200,100))
rychlost = 10
barva_pozadi = [0,0,0]

while program_going:

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            program_going = False
        """   
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                print("nahoru")
                pozice[1] -= rychlost
            if event.key == pygame.K_a:
                print("doleva")
                pozice[0] -= rychlost
            if event.key == pygame.K_s:
                print("dolu")
                pozice[1] += rychlost
            if event.key == pygame.K_d:
                print("doprava")
                pozice[0] += rychlost            
        """
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_w]:
            pozice[1] -= rychlost
        if pressed_keys[pygame.K_s]:
            pozice[1] += rychlost
        if pressed_keys[pygame.K_a]:
            pozice[0] -= rychlost
        if pressed_keys[pygame.K_d]:
            pozice[0] += rychlost           
    okno.fill(barva_pozadi)
    okno.blit(obrazek, pozice)

    pygame.display.update()

    timer.tick(30)

pygame.quit()