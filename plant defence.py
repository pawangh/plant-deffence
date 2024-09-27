import pgzrun
import random
import time

WIDTH=800
HEIGHT=600
TITLE="plant defence"
start=time.time()
total=0

player=Actor("bee")
player.pos=(50,300)
pollen=0

flower=Actor("3")
flower.pos=(500,400)
def draw():
  screen.blit("1",(0,0))
  screen.draw.text("pollen="+str(pollen),(350,20),color="black",fontsize=40)
  player.draw()
  flower.draw()
def update():
  global pollen
  if keyboard.right:
    player.x=player.x+5
  if keyboard.left:
    player.x=player.x-5
  if keyboard.up:
    player.y=player.y-5
  if keyboard.down:
    player.y=player.y+5
  if player.colliderect(flower):
    pollen=pollen+5
    flower.pos=(random.randint(100,700),random.randint(100,500))
pgzrun.go()