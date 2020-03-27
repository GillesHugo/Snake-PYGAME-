import pygame,sys       #import modules

screen_w = 500
screen_h = 600

colors = {              #definition of basics colors
    "black":(0,0,0),
    "white":(255,255,255),
    "red":(255,0,0),
    "blue":(0,255,0),
    "green":(0,0,255),
    }

pygame.init()
window = pygame.display.set_mode((screen_h,screen_w)) #window creation
game = True


grass = pygame.image.load("grass.png")

snake = pygame.image.load("snake.png")


position_snake = snake.get_rect()
window.blit(snake, (100, 100))

try:
    while game:

        if pygame.key.get_pressed()[pygame.K_UP]:
            position_snake = position_snake.move(0,-1)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            position_snake = position_snake.move(0,1)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            position_snake = position_snake.move(-1,0)
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            position_snake = position_snake.move(1,0)



        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:  #Escape or exit  is pressed
                game = False #end of the game

        window.fill(colors["black"])
        for i in range (0,50):
            for j in range (0, 32):
                window.blit(grass, (i*16,j*16))

        window.blit(snake, position_snake)
        pygame.display.flip()

except:
    print("Exit error")

finally:
    pygame.quit()
    sys.exit()
