#!/usr/bin/python3
import sys
import platform
import keyboard
import time

def printVersion():
  print("Platform       : " + platform.system())
  print("Python version : " + platform.python_version())


def parseArgs():
  
  #print (sys.argv)
  opts = [opt for opt in sys.argv[1:] if opt.startswith("-")]
  
  unitTest = False
  if '-t' in opts: unitTest = True
  return unitTest

class GameCtrl:
  def __init__(self):
    self.isRunning = False
    
  def run(self):
    self.isRunning = True
    
    self.level()
    self.isRunning = False

  def stop(self):
    print ("Stopping game")
    self.isRunning = False
    
  def level(self):
    print ("Level 1:")
    print ("Press the key when you see a letter")
    
    time.sleep(0.5)
    print ("a")
    startTime =  time.perf_counter()
    event = keyboard.read_event()
    stopTime =  time.perf_counter()
    deltaTime = stopTime - startTime
    if event.event_type == keyboard.KEY_DOWN and event.name == 'a':
      print('a was pressed')    
    print (f"Your time: {deltaTime:0.3f} s")

def on_esc():
  print('esc was pressed')
  exit()

def my_keyboard_hook(keyboard_event):
  print("Name:", keyboard_event.name)
  print("Scan code:", keyboard_event.scan_code)
  print("Time:", keyboard_event.time)


def unitTest():
  print ("UNIT TEST")
  return False


#______________________________________________________________________________
def main():
  printVersion()
  test = parseArgs()

  if (test == True):
    if (unitTest() == False):
      print ("UNIT TEST FAIL!")

  game = GameCtrl()
  keyboard.add_hotkey('esc', game.stop)
  game.run()
  while (game.isRunning):
    time.sleep(0.1)

  #keyboard.hook(my_keyboard_hook)
  # Block forever, so that the program won't automatically finish,
  # preventing you from typing and seeing the printed output
  #keyboard.read_key()

  
    
main()
