import pygame, pyautogui, time, random, TTS, Pop
from Clubs import * #Another file catalog so this main one doesnt feel too crowded
from DisplStuff import *

#SET UP FOR THE SCREEN
os.environ['SDL_VIDEO_WINDOW_POS'] = "0,0"
pygame.init()

pygame.display.set_caption("Career Mode")

X, Y = pyautogui.size()
scrn = pygame.display.set_mode((X, Y))
#SET UP FOR THE SCREEN

#Initialize the variables
age = 9
clock, FPS = pygame.time.Clock(), 60
done = False
team = [pygame.font.SysFont('Comic Sans M',  40).render('None', True, White), 'FILLER BECAUSE THE PARAMETER "team" is refered to as a list']

#Define functions
def DisplScrn():
    scrn.fill(Olive)
    msgbox('Age: ' + str(age), (X-100, 10), 40)
    msgbox('Club:', (X-200, 60), 40)
    scrn.blit(team[0], (X-100, 40))
    pygame.display.flip()

def JerseyMaker(team, x, y):
    #team[0] = logo
    #team[1] = main colour
    #team[2] = secondary colour

    pos = (x, y,80,200)

    pygame.draw.rect(scrn, team[1], pos) #body
    pygame.draw.rect(scrn, team[2], (pos[0]-50, pos[1]+20, 50, 50)) #left arm
    pygame.draw.rect(scrn, team[2], (pos[0]+pos[2], pos[1]+20, 50, 50)) #right arm
    pygame.draw.rect(scrn, team[2], (pos[0], pos[1]+pos[3], 30, 50)) #left leg
    pygame.draw.rect(scrn, team[2], (pos[0]+50, pos[1]+pos[3], 30, 50)) #right leg
    scrn.blit(team[0], (pos[0]+pos[3]-200, pos[1]))
    scrn.blit(Head, (pos[0], pos[1]-75))
    pygame.display.flip()

def initSituation():
    DisplScrn()
    time.sleep(2)
    centerbox("You're playing in the park...", (X/2, 100), 100)
    pygame.display.flip()
    TTS.talk("You're playing in the park")
    centerbox('and you notice a scout watching you.',(X/2, 200), 100)
    pygame.display.flip()
    TTS.talk('and you notice a scout watching you.')
    DisplScrn()
    centerbox('The scout gives you the option',(X/2, 100), 100)
    centerbox('to join one of two academies.',(X/2, 200), 100)
    pygame.display.flip()
    TTS.talk('The scout gives you the option to join one of two academies.')
    teams = random.choices(t, k=2)  #i changed it from t1 to t so all teams can scout instead of lowest rated teams
    team1 = teams[0]
    team2 = teams[1]
    POS_ON_X_CHOICE = 200
    for team in teams:
        JerseyMaker(team, POS_ON_X_CHOICE, 500)
        POS_ON_X_CHOICE = 1500
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((x < 280) and (x > 200) and (y < 700) and (y > 500)):
                    Pop.popper(900, 0.025)
                    TTS.talk('Selected!')
                    team = team1
                    done = True
                elif ((x < 1580) and (x > 1500) and (y < 700) and (y > 500)):
                    Pop.popper(900, 0.025)
                    TTS.talk('Selected!')
                    team = team2
                    done = True
        clock.tick(FPS)
    return team

def DisplHits(hits):
    msgbox('Hits: ' + str(hits), (10, 10), 40)
    pygame.display.flip()

def Minigame1():
    TTS.talk('Balls will appear on the screen. Hit as many as you can!')
    hits = 0
    limit = 90  #1.5 seconds limit to hit and on each interation of the for loop it gets shorter by .05 seconds (about ish)
    for num in range(20): #Change the range based on how many balls you want
        xM1 = random.randint(0, X) #xM1 = X for minigame 1
        yM1 = random.randint(0, Y)
        DisplScrn()
        DisplHits(hits)
        scrn.blit(Ball, (xM1, yM1))
        pygame.display.flip()
        time = 0
        hit_on_this_try = False
        while time != limit:
            time += 1
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if ((x < xM1 + 50) and (x > xM1) and (y < yM1 + 50) and (y > yM1)):
                        Pop.popper(900, 0.025)
                        if hit_on_this_try == False:
                            hits += 1
                            hit_on_this_try = True
            clock.tick(FPS)
        limit -= 3
    TTS.talk(str(hits))
    if hits > 10: #if hits are greater than 10 then stay at club or else kicked
        TTS.talk('Based on your results, the manager has allowed you to stay at the club for as long as you wish for!')
    else: 
        TTS.talk('Based on your results, the manager has decided to kick you out of the club. Restart the game to try again.')
        pygame.quit()
        quit()

def UCL():
    CurrentStage = '16'
    if age == 16:
        TTS.talk("Since you are now 16, your manager has decided to start you in this seasons' Uefa Champions League!")

    b1 = random.sample(t, 1)
    b1.append(team)
    b2 = random.sample(t, 2)
    b3 = random.sample(t, 2)
    b4 =random.sample(t, 2)
    b5 = random.sample(t, 2)
    b6 =random.sample(t, 2)
    b7 =random.sample(t, 2)
    b8 = random.sample(t, 2)

    bracket = [b1,b2,b3,b4,b5,b6,b7,b8]
    x = 0

    for b in bracket:
        c1 = b[0]
        c2 = b[1]
        scrn.blit(c1[0], (x, 0))
        scrn.blit(c2[0], (x+90, 0))
        pygame.display.flip()
        time.sleep(0.25)
        x += 180

    #up to here it's all good

    out_of_ucl = False
    while not out_of_ucl:
        UCL_buttons(X, Y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if ((x < X) and (x > X-300) and (y < Y/2-60) and (y > Y/2-100)):
                    TTS.talk('Play')
                elif ((x < X) and (x > X-300) and (y < Y/2+40) and (y > Y/2)):
                    TTS.talk('Simulate one leg')
                    match_sim(1, bracket)
                elif ((x < X) and (x > X-300) and (y < Y/2+140) and (y > Y/2+100)):
                    TTS.talk('Simulate both legs')
                    
                    if CurrentStage == '16':
                        out_of_ucl, CurrentStage, bracket = match_sim(2, bracket, CurrentStage)
                    elif CurrentStage == '8':
                        out_of_ucl, CurrentStage, bracket = Quarters(2, bracket, CurrentStage)
                    elif CurrentStage == '4':
                        out_of_ucl, CurrentStage, bracket = Semis(2, bracket, CurrentStage)
                    elif CurrentStage == '2':
                        out_of_ucl, CurrentStage, bracket = final(bracket)

                elif ((x < X) and (x > X-300) and (y < Y/2+240) and (y > Y/2+200)):
                    TTS.talk('Simulate all')
        clock.tick(FPS)

def match_sim(legs, bracket, CurrentStage):
    y = 200
    s1 = 0
    s2 = 0
    for num in range(legs):
        c1 = random.randint(0,4)
        c2 = random.randint(0,4) #PLAYER'S TEAM
        s1 += c1 #s1 is used to record the two legs while c1 is only used to record one leg
        s2 += c2
        fixture = str(c1) + ' - ' + str(c2)

        b = bracket[0]    #bracket = all the teams (b1, b2, b3, b4, etc)
                                #b = one singular bracket (Ex: b2)

        if c2 > c1:
            TTS.talk('You won!')
        elif c2 == c1:
            TTS.talk("It's a draw!")
        else:
            TTS.talk('You lost!')
            
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(fixture, True, White), (0, y))
        pygame.display.flip()
        y += 100
    
    if legs == 2:
        aggregate = 'A: ' + str(s1) + ' - ' + str(s2)
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(aggregate, True, White), (0, 400))
        if s2 > s1:
            TTS.talk('You won on aggragate!')
            bracket[0] = b[1]
            print("b[1]: " + str(b[1]))
            print("bracket[0] (b4 sim all matches): " + str(bracket[0]))
        elif s2 == s1:
            TTS.talk("It's a draw! Penalties!")
        else:
            TTS.talk('You lost on aggragate!')
            return True, '16', ''

    bracket = sim_all_other_matches(legs, bracket, CurrentStage)
    time.sleep(2)

    b1 = bracket[0]
    t1, t2 = b1[0], b1[1]

    b2 = bracket[1]
    t3, t4 = b2[0], b2[1]

    b3 = bracket[2]
    t5, t6 = b3[0], b3[1]

    b4 = bracket[3]
    t7, t8 = b4[0], b4[1]

    bracket.remove(bracket[4])
    bracket.remove(bracket[4])
    bracket.remove(bracket[4])
    bracket.remove(bracket[4])

    x = 0
    y = 0
    teams = [t1, t2, t3, t4, t5, t6, t7, t8]
    print("All the teams: " + str(teams))

    DisplScrn()
    UCL_buttons(X, Y)

    for t in teams:
        print("Team:" + str(t))
        scrn.blit(t[0], (x,y))
        pygame.display.flip()
        x += 90
        time.sleep(0.25)

    return False, '8', bracket

def sim_all_other_matches(legs, bracket, CurrentStage):
    x = 200
    NUM = 0
    for NUM in range(len(bracket)-1):
        y = 200
        s1 = 0
        s2 = 0
        b = bracket[NUM+1]
        for num in range(legs):
            c1 = random.randint(0,4)
            c2 = random.randint(0,4)
            s1 += c1
            s2 += c2
            fixture = str(c1) + ' - ' + str(c2)
            aggregate = 'A: ' + str(s1) + ' - ' + str(s2)

            if s2 > s1:
                bracket[NUM+1] = b[1]
            else:
                bracket[NUM+1] = b[0]

            scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(fixture, True, White), (x, y))
            time.sleep(0.25)
            y += 100
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(aggregate, True, White), (x, 400))
        pygame.display.flip()
        x += 200
        if (NUM == 6) and (CurrentStage == '16'):
            CONSTANTBRACKET = bracket
            bracket[0] = [CONSTANTBRACKET[1],CONSTANTBRACKET[0]]
            bracket[1] = [CONSTANTBRACKET[2],CONSTANTBRACKET[3]]
            bracket[2] = [CONSTANTBRACKET[4],CONSTANTBRACKET[5]]
            bracket[3] = [CONSTANTBRACKET[6],CONSTANTBRACKET[7]]
            return bracket
        elif (NUM == 2) and (CurrentStage == '8'):   #DECIDE LATER THE NUMS THO
            CONSTANTBRACKET = bracket
            bracket[0] = [CONSTANTBRACKET[1],CONSTANTBRACKET[0]]
            bracket[1] = [CONSTANTBRACKET[2],CONSTANTBRACKET[3]]
            return bracket
        elif (NUM == 0) and (CurrentStage == '4'): #DECIDE LATER THE NUMS THO
            CONSTANTBRACKET = bracket
            bracket[0] = [CONSTANTBRACKET[1],CONSTANTBRACKET[0]]
            return bracket

def Quarters(legs, bracket, CurrentStage):
    y = 200
    s1 = 0
    s2 = 0
    for num in range(legs):
        c1 = random.randint(0,4)
        c2 = random.randint(0,4) #PLAYER'S TEAM
        s1 += c1 #s1 is used to record the two legs while c1 is only used to record one leg
        s2 += c2
        fixture = str(c1) + ' - ' + str(c2)

        b = bracket[0]    #bracket = all the teams (b1, b2, b3, b4, etc)
                                #b = one singular bracket (Ex: b2)

        if c2 > c1:
            TTS.talk('You won!')
        elif c2 == c1:
            TTS.talk("It's a draw!")
        else:
            TTS.talk('You lost!')
            
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(fixture, True, White), (0, y))
        pygame.display.flip()
        y += 100
    
    if legs == 2:
        aggregate = 'A: ' + str(s1) + ' - ' + str(s2)
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(aggregate, True, White), (0, 400))
        if s2 > s1:
            TTS.talk('You won on aggragate!')
            bracket[0] = b[1]
        elif s2 == s1:
            TTS.talk("It's a draw! Penalties!")
        else:
            TTS.talk('You lost on aggragate!')
            return True, '16', bracket
    bracket = sim_all_other_matches(legs, bracket, CurrentStage)
    time.sleep(2)

    b1 = bracket[0]
    t1, t2 = b1[0], b1[1]

    b2 = bracket[1]
    t3, t4 = b2[0], b2[1]

    bracket.remove(bracket[2])
    bracket.remove(bracket[2])

    x = 0
    y = 0
    teams = [t1, t2, t3, t4]
    print("All the teams: " + str(teams))

    DisplScrn()
    UCL_buttons(X, Y)

    for t in teams:
        print("Team:" + str(t))
        scrn.blit(t[0], (x,y))
        pygame.display.flip()
        x += 90
        time.sleep(0.25)

    return False, '4', bracket

def Semis(legs, bracket, CurrentStage):
    y = 200
    s1 = 0
    s2 = 0
    for num in range(legs):
        c1 = random.randint(0,4)
        c2 = random.randint(0,4) #PLAYER'S TEAM
        s1 += c1 #s1 is used to record the two legs while c1 is only used to record one leg
        s2 += c2
        fixture = str(c1) + ' - ' + str(c2)

        b = bracket[0]    #bracket = all the teams (b1, b2, b3, b4, etc)
                                #b = one singular bracket (Ex: b2)

        if c2 > c1:
            TTS.talk('You won!')
        elif c2 == c1:
            TTS.talk("It's a draw!")
        else:
            TTS.talk('You lost!')
            
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(fixture, True, White), (0, y))
        pygame.display.flip()
        y += 100
    
    if legs == 2:
        aggregate = 'A: ' + str(s1) + ' - ' + str(s2)
        scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(aggregate, True, White), (0, 400))
        if s2 > s1:
            TTS.talk('You won on aggragate!')
            bracket[0] = b[1]
        elif s2 == s1:
            TTS.talk("It's a draw! Penalties!")
        else:
            TTS.talk('You lost on aggragate!')
            return True, '16', bracket
    bracket = sim_all_other_matches(legs, bracket, CurrentStage)
    time.sleep(2)

    b1 = bracket[0]
    t1, t2 = b1[0], b1[1]

    bracket.remove(bracket[1])

    x = 0
    y = 0
    teams = [t1, t2]
    print("All the teams: " + str(teams))

    DisplScrn()
    UCL_buttons(X, Y)

    for t in teams:
        print("Team:" + str(t))
        scrn.blit(t[0], (x,y))
        pygame.display.flip()
        x += 90
        time.sleep(0.25)

    return False, '2', bracket

def final(bracket):
    y = 200
    s1 = 0
    s2 = 0
    c1 = random.randint(0,4)
    c2 = random.randint(0,4) #PLAYER'S TEAM
    fixture = str(c1) + ' - ' + str(c2)

    b = bracket[0]    #bracket = all the teams (b1, b2, b3, b4, etc)
                                #b = one singular bracket (Ex: b2)

    if c2 > c1:
        TTS.talk('You won the Uefa Champions League!')
    elif c2 == c1:
        TTS.talk("It's a draw!")
    else:
        TTS.talk('You lost on aggragate!')
            
    scrn.blit(pygame.font.SysFont('Comic Sans M',  40).render(fixture, True, White), (0, y))
    pygame.display.flip()
    y += 100
    return True, '16', bracket

team = initSituation()
age += 1
#Minigame1() UNCOMMENT THIS AFTER DONE WITH TESTS

for num in range(6): #ages up to 16, 10 (current age) + 6 (added age through this for loop) = 16
    age += 1
    DisplScrn()
    arrow()
    time.sleep(0.75)

for num in range (24):
    DisplScrn()
    UCL()
    age += 1