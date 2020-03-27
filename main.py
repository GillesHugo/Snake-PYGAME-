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

try:
    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:  #Escape or exit  is pressed
                game = False #end of the game

        window.fill(colors["black"])
        pygame.display.flip()

except:
    print("Exit error")

finally:
    pygame.quit()
    sys.exit()