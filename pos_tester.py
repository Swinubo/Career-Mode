import pygame, pyautogui

pygame.init()

X, Y = pyautogui.size()
scrn = pygame.display.set_mode((X, Y))

Black = (0,100,0)

done = False

while not done:

    #Arrow
    pygame.draw.rect(scrn, Black, (1600, 50, 100, 50))
    pygame.draw.polygon(scrn, Black, ((1700, 0), (1700, 150), (1750, 75)))


    pygame.display.update()

#This is just some random file that I created so that I can test the postion of different stuff.