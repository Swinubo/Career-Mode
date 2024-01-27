import pygame, os, pathlib

pygame.init()

scrn = pygame.display.set_mode((0, 0))

current_dir = os.getcwd()
image_path = pathlib.Path(current_dir, 'PlayerLogos')
image_path_g = pathlib.Path(current_dir, 'Career Mode Images')

LOGO_IMAGE_SIZE = (80, 80)
BALL_IMAGE_SIZE = (50, 50)

#Colour log
Black=(0,0,0)
White=(255,255,255)
Red=(255,0,0)
Lime=(0,255,0)
Blue=(0,0,255)
Yellow=(255,255,0)
Cyan=(0,255,255)
Magenta=(255,0,255)
Silver=(192,192,192)
Gray=(128,128,128)
Maroon=(128,0,0)
Olive=(128,128,0)
Green=(0,128,0)
Purple=(128,0,128)
Teal=(0,128,128)
Navy=(0,0,128)
Orange=(255,165,0)

#CLUB IMAGES CATALOG

Chelsea = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Chelsea.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Blue, Blue]
Spurs = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Tottenham.png"))).convert_alpha(), LOGO_IMAGE_SIZE), White, Blue]
ManUtd = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Manchester United.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Red, Orange]
ManCity = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Manchester City.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Cyan, Cyan]
LFC = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Liverpool.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Red, Red]
Arsenal = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Arsenal.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Red, White]
Newcastle = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Premier League', "Newcastle United.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Black, White]

PSG = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Ligue 1', "Paris Saint-Germain.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Blue,Red]
Marseille = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Ligue 1', "Olympique de Marseille.png"))).convert_alpha(), LOGO_IMAGE_SIZE),White, Cyan]
Lyon = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Ligue 1', "Olympique Lyonnais.png"))).convert_alpha(), LOGO_IMAGE_SIZE), White, Red]

Porto = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Liga Portugal', "FC Porto.png"))).convert_alpha(), LOGO_IMAGE_SIZE), White, Navy]
Sporting = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Liga Portugal', "Sporting Cp.png"))).convert_alpha(), LOGO_IMAGE_SIZE), White, Green]
Benfica = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Liga Portugal', "Benfica.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Magenta, Magenta]

RealMadrid = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'La Liga', "Real Madrid.png"))).convert_alpha(), LOGO_IMAGE_SIZE),White,White]
AthleticoMadrid = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'La Liga', "Athletico.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Red, Blue]
Barca = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'La Liga', "Barcelona.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Magenta, Blue]
Sevilla = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'La Liga', "Sevilla.png"))).convert_alpha(), LOGO_IMAGE_SIZE), White, Maroon]
Sociedad = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'La Liga', "Real Sociedad.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Blue,White]

Inter = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Serie A', "Inter Milan.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Blue, Black]
Milan = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Serie A', "AC Milan.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Magenta, Black]
Juve = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Serie A', "Juventus.png"))).convert_alpha(), LOGO_IMAGE_SIZE),White,Black]
Roma = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Serie A', "Roma.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Magenta, Yellow]
Napoli = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Serie A', "Napoli.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Cyan, Blue]

Munich = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Bundesliga', "Bayern.png"))).convert_alpha(), LOGO_IMAGE_SIZE), White, Magenta]
Dortmund = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Bundesliga', "BVB.png"))).convert_alpha(), LOGO_IMAGE_SIZE), Yellow, Black]
Wolfsburg = [pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path, 'Bundesliga', "Wolfsburg.png"))).convert_alpha(), LOGO_IMAGE_SIZE),Green, White]

#Club rank
t1 = [Porto, Sporting, Lyon, Wolfsburg, Sevilla]
t2 = [Sociedad, Marseille, Roma, Benfica]
t3 = [Spurs, AthleticoMadrid, Napoli, Dortmund, Newcastle]
t4 = [Chelsea, ManCity, ManUtd, Arsenal, PSG, RealMadrid, Barca, Munich, LFC, Inter, Milan, Juve]

t = [Porto, Sporting, Lyon, Wolfsburg, Sevilla, Sociedad, Marseille, Roma, Benfica, Spurs, AthleticoMadrid, Napoli, Dortmund, Newcastle,  Chelsea, ManCity, ManUtd, Arsenal, PSG, RealMadrid, Barca, Munich, LFC, Inter, Milan, Juve]

#Other images
Ball = pygame.transform.scale(pygame.image.load(str(pathlib.Path(image_path_g, "Ball.png"))).convert_alpha(), BALL_IMAGE_SIZE)


'''
while True:
    JerseyMaker(Barca, (100,100,80,200), scrn)
    pygame.display.flip()
'''
# This comment block at the top is just something that i turned on and off to see if the JerseyMaker() function worked

#Update: i moved jersey maker to the main file


#b = a bracket
#t = a team
#c = a club
#s = a score