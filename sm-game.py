import sys
import pygame
import time
pygame.init()

Version = 2.0

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0

font = pygame.font.Font(pygame.font.get_default_font(), 30)


class DisplayMgr:
  def __init__(self):
    self.appSurf = pygame.display.set_mode((1200, 768))
    self.appRect = self.appSurf.get_rect()
    self.gameSurf = pygame.Surface((self.appRect.width, self.appRect.height-200))
    self.consoleSurf = pygame.Surface((self.appRect.width, 200))
     
  def clearAll(self):
    self.gameSurf.fill(black)
    self.consoleSurf.fill(white)
    verText = pygame.font.Font.render(font, "Version " + str(Version), True, black)
    dMgr.consoleSurf.blit(verText, dest=(self.consoleSurf.get_rect().width - verText.get_rect().width, self.consoleSurf.get_rect().height - verText.get_rect().height))
  
  def blitAll(self):
    self.appSurf.blit(self.gameSurf, dest=(0, 0))
    self.appSurf.blit(self.consoleSurf, dest=(0, self.appRect.height-200))
  


class Player:
  def __init__(self, img):
    self.skinSurfOriginal = pygame.image.load(img)
    
    self.skinSurf = pygame.transform.smoothscale(self.skinSurfOriginal,  (100, 100))
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
myPlayer.skinSurfRect.move_ip(600, dMgr.gameSurf.get_rect().height - myPlayer.skinSurfRect.height)
obstable = Player("traffic-cone.png")
obstable.skinSurfRect.move_ip(600, 0)
obstable2 = Player("tree.png")
obstable2.skinSurfRect.move_ip(800, 0)

obstaclePassed = 0  
obsMoveY = 5

while 1:

  if (myPlayer.skinSurfRect.collidelist((obstable.skinSurfRect, obstable2.skinSurfRect)) != -1):
  #if myPlayer.skinSurfRect.collidelist((obstable.skinSurfRect)):
    gameOver(frame, dMgr)
    
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
  if (myPlayer.skinSurfRect.x < 0):
    myPlayer.skinSurfRect.x = 0
  if (myPlayer.skinSurfRect.x > (dMgr.gameSurf.get_rect().width - myPlayer.skinSurfRect.width)):
    myPlayer.skinSurfRect.x = (dMgr.gameSurf.get_rect().width - myPlayer.skinSurfRect.width)
  
  obstable.skinSurfRect.move_ip(0, obsMoveY)
  if (  obstable.skinSurfRect.y > dMgr.gameSurf.get_rect().height):
    obstable.skinSurfRect.y = 0  
    obsMoveY = obsMoveY + 3
    obstable.skinSurfRect.x = myPlayer.skinSurfRect.x

  obstable2.skinSurfRect.move_ip(0, obsMoveY)
  if (  obstable2.skinSurfRect.y > dMgr.gameSurf.get_rect().height):
    obstable2.skinSurfRect.y = 0  
    #obsMoveY = obsMoveY + 3
    obstable2.skinSurfRect.x = obstable.skinSurfRect.x -100
  
  # Game Surface Blits
  dMgr.gameSurf.blit(myPlayer.skinSurf, dest=myPlayer.skinSurfRect)
  dMgr.gameSurf.blit(obstable.skinSurf, dest=obstable.skinSurfRect)
  dMgr.gameSurf.blit(obstable2.skinSurf, dest=obstable2.skinSurfRect)

  # Console Blits
  myText = pygame.font.Font.render(font, "Frame #" + str(frame), True, red)
  dMgr.consoleSurf.blit(myText, dest=(10, 10))

  
  dMgr.blitAll()
  pygame.display.flip()
  frame = frame + 1