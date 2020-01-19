import pygame
import random
import sys

pygame.init()

width = 800
height =  600

color = (150,150,150)

playersize = 50

playerpos = [width/2,height-2*playersize]

enemysize = 50

enemypos = [random.randint(0, width-enemysize),0]

enemylist = [enemypos]

red = (255,0,0)

speed = 10

white =(255,255,255)

score = 0

clock = pygame.time.Clock()

myfont = pygame.font.SysFont("calibri", 40)

def setlevel(score, speed):
    if score <10:
        speed=4
    elif score <20:
        speed = 10
    elif score < 30:
        speed = 15
    elif score < 70:
        speed = 30
    return speed

def dropenemy(enemylist):
    delay = random.random()
    if len(enemylist) < 20 and delay < 0.1:
        xpos = random.randint(0,width-enemysize)
        ypos = 0
        enemylist.append([xpos, ypos])

def drawenemy(enemylist):
    for enemypos in enemylist:
            pygame.draw.rect(screen, red, (enemypos[0], enemypos[1], enemysize, enemysize))

def update_enemypos(enemylist, score): 
    for index, enemypos in enumerate(enemylist):
        if enemypos[1] >=0 and enemypos[1] < height:
            enemypos[1]+=speed

        else:
            enemylist.pop(index)
            score += 1
    return score

def collisoncheck(enemylist, playerpos):
    for enemypos in enemylist:
        if detectcollision(playerpos,enemypos):
            return True
    return False
        
def detectcollision(playerpos,enemypos):
    p_x = playerpos[0]
    p_y = playerpos[1]
    e_x = enemypos[0]
    e_y = enemypos[1]

    if(e_x >= p_x and e_x < (p_x + playersize)) or (p_x >= e_x and p_x < (e_x + enemysize)):
        if(e_y >= p_y and e_y < (p_y + playersize)) or (p_y >= e_y ) and p_y < (e_y+enemysize):
            return True
        return False

screen = pygame.display.set_mode((width,height)) #width and height of screen in python

gameover = False

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type ==pygame.KEYDOWN:

            x = playerpos[0]
            y = playerpos[1]

            if event.key == pygame.K_LEFT:
                x -= playersize

            elif event.key == pygame.K_RIGHT:
                x+= playersize

            playerpos=[x,y]

    screen.fill((0,0,0))

    # if detectcollision(playerpos,enemypos):
    #     gameover = True
    #     break

    dropenemy(enemylist)

    score = update_enemypos(enemylist, score)

    speed = setlevel(score,speed)
    text = "Your Score:" + str(score)
    label = myfont.render(text, 1, white)
    screen.blit(label,(width-200, height-40))

    if collisoncheck(enemylist, playerpos):
        gameover = True
        print(score)
        print(speed)
        break

    drawenemy(enemylist)

    pygame.draw.rect(screen, color , (playerpos[0],playerpos[1],playersize,playersize)) #(where it is to be displayed, color of rectangle, (dimensions of rectangle x cord, y cord, width, height ))


    clock.tick(30)
 
    pygame.display.update()