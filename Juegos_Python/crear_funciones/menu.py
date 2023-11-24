import pygame

pygame.init()

def main():

    screen = pygame.display.set_mode((800, 600))
    # logo = pygame.image.load("logo32x32.png")
    # pygame.display.set_icon(logo)
    # pygame.display.set_caption("minimal program")

    player = pygame.Rect((300, 250, 50, 50))

    run = True
    while run:
        
        screen.fill((0, 0, 0))
        
        pygame.draw.rect(screen, (255, 0, 0), player)
        
        key = pygame.key.get_pressed()
        if key[pygame.K_a] == True:
            player.move_ip(-1, 0)
        if key[pygame.K_d] == True:
            player.move_ip(1, 0)
        if key[pygame.K_w] == True:
            player.move_ip(0, -1)
        if key[pygame.K_s] == True:
            player.move_ip(0, 1)
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                
        pygame.display.update()        

if __name__ == "__main__":
    main()
