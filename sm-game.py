import sys
import pygame
import time
pygame.init()

black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0


class DisplayMgr:
  def __init__(self):
    self.appSurf = pygame.display.set_mode((1024, 768))
    self.appRect = self.appSurf.get_rect()
    self.gameSurf = pygame.Surface((self.appRect.width, self.appRect.height-200))
    self.consoleSurf = pygame.Surface((self.appRect.width, 200))
     
  def clearAll(self):
    self.gameSurf.fill(black)
    self.consoleSurf.fill(white)
  
  def blitAll(self):
    self.appSurf.blit(self.gameSurf, dest=(0, 0))
    self.appSurf.blit(self.consoleSurf, dest=(0, self.appRect.height-200))
  


class Player:
  def __init__(self, img):
    self.skinSurfOriginal = pygame.image.load(img)
    
    #self.skinSurf = pygame.transform.rotozoom(self.skinSurfOriginal,  0.0, 0.25)
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
myPlayer.skinSurfRect.move_ip(512, dMgr.gameSurf.get_rect().height - myPlayer.skinSurfRect.height)
obstable = Player("traffic-cone.png")
obstable.skinSurfRect.move_ip(512, 0)

#scale(surface, size, dest_surface=None)
#pygame.transform.scale(car, (128,128), car2)


font = pygame.font.Font(pygame.font.get_default_font(), 36)
#render(text, antialias, color, background=None) -> Surface
myText = pygame.font.Font.render(font, "x.x", True, (255, 255, 255))

color0 = 200, 200, 200
color1 = 255, 255, 255


  
obsMoveY = 5

while 1:

  if myPlayer.skinSurfRect.colliderect(obstable.skinSurfRect):
    gameOver(frame, dMgr)
    
  moveX = 0
  for event in pygame.event.get():
    if event.type == pygame.QUIT: 
      #sys.exit()
      gameOver(0, dMgr)
    if event.type == pygame.KEYDOWN:
      if event.key == pygame.K_RIGHT:
        moveX = 100
      elif event.key == pygame.K_LEFT:
        moveX = -100
  
  pygame.time.Clock().tick(60.0)
  
  dMgr.clearAll()

  #color1 = color0
  #if (frame % 2):
  #  color0 = white
  #else:
  #  color0 = black
  #screen.fill(color0)

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
  
  # Blit player
  dMgr.gameSurf.blit(myPlayer.skinSurf, dest=myPlayer.skinSurfRect)
  dMgr.gameSurf.blit(obstable.skinSurf, dest=obstable.skinSurfRect)

  myText = pygame.font.Font.render(font, "Frame #" + str(frame), True, red)
  dMgr.consoleSurf.blit(myText, dest=(10, 10))

  
  #Surface((width, height), flags=0, depth=0, masks=None)
  #surf = pygame.Surface((100, 100))
  dMgr.blitAll()
  pygame.display.flip()
  frame = frame + 1