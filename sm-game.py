import sys
import pygame
import time
from collections import namedtuple

pygame.init()

Version = 2.0

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

font = pygame.font.Font(pygame.font.get_default_font(), 30)

Resolution = namedtuple("Resolution", "width height")
appRes = Resolution(width=1200, height=768)
consoleRes = Resolution(width=appRes.width, height=200)
gameRes = Resolution(width=appRes.width, height=appRes.height - consoleRes.height)


class DisplayMgr:
    def __init__(self):
        self.appSurf = pygame.display.set_mode(appRes)
        self.appRect = self.appSurf.get_rect()
        self.gameSurf = pygame.Surface(gameRes)
        self.consoleSurf = pygame.Surface(consoleRes)

    def clearAll(self):
        self.gameSurf.fill(black)
        self.consoleSurf.fill(white)
        verText = pygame.font.Font.render(font, "Version " + str(Version), True, black)
        dMgr.consoleSurf.blit(
            verText,
            dest=(
                self.consoleSurf.get_rect().width - verText.get_rect().width,
                self.consoleSurf.get_rect().height - verText.get_rect().height,
            ),
        )

    def blitAll(self):
        self.appSurf.blit(self.gameSurf, dest=(0, 0))
        self.appSurf.blit(self.consoleSurf, dest=(0, self.appRect.height - 200))


class Player:
    def __init__(self, img):
        self.skinSurfOriginal = pygame.image.load(img)

        self.skinSurf = pygame.transform.smoothscale(self.skinSurfOriginal, (100, 100))
        self.skinSurfRect = self.skinSurf.get_rect()


def gameOver(frame, dMgr):
    dMgr.consoleSurf.fill(white)
    myText = pygame.font.Font.render(font, "GAME OVER! Score: " + str(frame), True, red)
    dMgr.consoleSurf.blit(myText, dest=(10, 10))
    dMgr.blitAll()
    pygame.display.flip()
    time.sleep(2)
    sys.exit()


dMgr = DisplayMgr()
frame = 0


myPlayer = Player("car.png")
myPlayer.skinSurfRect.move_ip(
    600, dMgr.gameSurf.get_rect().height - myPlayer.skinSurfRect.height
)
obstacles = [Player("traffic-cone.png")]

obstaclePassed = 0
obsMoveY = 5

while 1:

    # if (myPlayer.skinSurfRect.collidelist(obstacles) != -1):
    # if myPlayer.skinSurfRect.collidelist((obstacle.skinSurfRect)):
    # gameOver(frame, dMgr)

    moveX = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver(0, dMgr)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                moveX = 100
            elif event.key == pygame.K_LEFT:
                moveX = -100

    pygame.time.Clock().tick(60.0)

    dMgr.clearAll()

    myPlayer.skinSurfRect.move_ip(moveX, 0)
    if myPlayer.skinSurfRect.x < 0:
        myPlayer.skinSurfRect.x = 0
    if myPlayer.skinSurfRect.x > (
        dMgr.gameSurf.get_rect().width - myPlayer.skinSurfRect.width
    ):
        myPlayer.skinSurfRect.x = (
            dMgr.gameSurf.get_rect().width - myPlayer.skinSurfRect.width
        )

    #  obstacle.skinSurfRect.move_ip(0, obsMoveY)
    #  if (  obstacle.skinSurfRect.y > dMgr.gameSurf.get_rect().height):
    #    obstacle.skinSurfRect.y = 0
    #    obsMoveY = obsMoveY + 3
    #    obstacle.skinSurfRect.x = myPlayer.skinSurfRect.x

    #  obstacle2.skinSurfRect.move_ip(0, obsMoveY)
    #  if (  obstacle2.skinSurfRect.y > dMgr.gameSurf.get_rect().height):
    #    obstacle2.skinSurfRect.y = 0
    # obsMoveY = obsMoveY + 3
    #    obstacle2.skinSurfRect.x = obstacle.skinSurfRect.x -100

    # Game Surface Blits
    dMgr.gameSurf.blit(myPlayer.skinSurf, dest=myPlayer.skinSurfRect)

    for obs in obstacles:
        dMgr.gameSurf.blit(obs.skinSurf, dest=obs.skinSurfRect)

    # Console Blits
    myText = pygame.font.Font.render(font, "Frame #" + str(frame), True, red)
    dMgr.consoleSurf.blit(myText, dest=(10, 10))

    dMgr.blitAll()
    pygame.display.flip()
    frame = frame + 1
