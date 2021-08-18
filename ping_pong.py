import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((1000,600))

pygame.display.set_caption('ping-pong')
icon = pygame.image.load('ping-pong.png')
pygame.display.set_icon(icon)

font = pygame.font.Font('freesansbold.ttf',32)
score1 = 0
score2 = 0

def score():        #displaying the scoreboard
    score_value = font.render('SCORE ' + str(score1) + ':' + str(score2),True,(150,235,94))
    screen.blit(score_value,(440,10))

#RACKET 1
racket1_img = pygame.image.load('racket.png')
racket1X = 0
racket1Y = 0
racket1_change = 0

def racket1(x,y):       #displaying the first racket
    screen.blit(racket1_img,(x,y))

#RACKET 2
racket2_img = pygame.image.load('racket2.png')
racket2X = 930
racket2Y = 300
racket2_change = 0

def racket2(x,y):       #displaying the second racket
    screen.blit(racket2_img,(x,y))

#BALL
ball_img = pygame.image.load('ball.png')
ballX = 436
ballY = random.randint(10,580)
ballX_change = 0.4
ballY_change = 0.4

def ball(x,y):      #displaying the ball
    screen.blit(ball_img,(x,y))

#The distance for 2 rackets are different because the ball will be hitting the right side of
#the first bat whereas it hits left side of the 2nd bat and the x y co-ordinates of bat image
#starts from top left corner so the distance are different

def hit1(a,b,c,d):      #checking if the ball hit racket 1
    d1 = math.sqrt(math.pow((a-b),2) + math.pow((c-d),2))
    if d1 < 52:
        return True

def hit2(a,b,c,d):      #checking if the ball hit racket 2
    d2 = math.sqrt(math.pow((a-b),2) + math.pow((c-d),2))
    if d2 < 35:
        return True

running = True

while running:
    screen.fill((200,150,100))
    score()
    racket1(racket1X,racket1Y)
    racket2(racket2X,racket2Y)
    ball(ballX,ballY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:#down arrow button for moving 1st racket down
                racket1_change = 1
            if event.key == pygame.K_UP:#up arrow button for moving 1st racket up
                racket1_change = -1
            if event.key == pygame.K_w:#w button for moving 2nd racket up
                racket2_change = -1
            if event.key == pygame.K_s:#s button for moving 2nd racket down
                racket2_change = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                racket1_change = 0
            if event.key == pygame.K_w or event.key == pygame.K_s:
                racket2_change = 0
    #racket1_change and racket2_change are the movement speed of the 2 rackets
    racket1Y += racket1_change
    racket2Y += racket2_change
    ballX += ballX_change
    ballY += ballY_change

    #checking if the ball goes out of boundary
    if ballX < 0:
        ballX = 436
        ballY = random.randint(10,580)
        ball(ballX,ballY)
        score2+=1
    if ballX > 976:
        ballX = 436
        ballY = random.randint(10,580)
        ball(ballX,ballY)
        score1+=1
    #checking if ball touches the top and bottom boundary and changing its direction
    if ballY < 0:
        ballY_change = 0.4
    if ballY > 576:
        ballY_change = -0.4

    #making sure the rackets remain inside the boundary
    if racket1Y >536:
        racket1Y = 536
    if racket1Y < 0 :
        racket1Y = 0

    if racket2Y >536:
        racket2Y = 536
    if racket2Y < 0 :
        racket2Y = 0

    #changing the direction of ball movement once it hits any of the rackets
    if hit1(racket1X,ballX,racket1Y,ballY):
        ballX_change = 0.4

    if hit2(racket2X,ballX,racket2Y,ballY):
        ballX_change = -0.4



    pygame.display.update()
