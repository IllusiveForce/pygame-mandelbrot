#Imports
import  pygame  as  pg
import  random
import math
pg.init()

#Constants
maxIter=20
windowWidth=600
windowHeight=600
halfWindowWidth=windowWidth/2
halfWindowHeight=windowHeight/2

gameDisplay=pg.display.set_mode((windowWidth,windowHeight+70))
font=pg.font.Font(None,30)

#Colors
palette=[(255,255,255)]

for i in range(100):
  for j in range(10):
     color=(j*20,100,0)
     #color=(random.randint(0,255),random.randint(0,255),random.randint(0,255))
     palette.append(color)

#Function
def  fractal(i):
   global  maxIter
   z=0
   n=0
   zoom=1
   while  abs(z)<=2  and  n<maxIter:
       z=z**2+i/zoom  #     /2 is for zoomed fractal
       n+=1
   return  n
   
#Render fractal
for  a  in  range(windowWidth*2):
   for  event  in  pg.event.get():
       if  event.type==pg.QUIT:
           pg.quit()
   for  b  in  range(windowHeight*2):
       plotPixel=complex((a-windowWidth)/halfWindowWidth,(b-windowHeight)/halfWindowHeight)
       if fractal(plotPixel)==maxIter:
           gameDisplay.set_at((int(a/2),int(b/2)),(0,0,0))
           pg.display.update()
       else:
           gameDisplay.set_at((int(a/2),int(b/2)),palette[fractal(plotPixel)])
           pg.display.update()
mouserectpos=(0,0)

#Loop
while True:
  pg.draw.rect(gameDisplay,(255,255,255),pg.Rect(0,windowWidth,windowWidth,windowWidth))
  for  event  in  pg.event.get():
       if  event.type==pg.QUIT:
           pg.quit()
  if event.type==pg.MOUSEMOTION:
    mouserectpos=event.pos
  gameDisplay.blit(font.render('Mouse: '+str(mouserectpos),False,(0,0,0)),(10,10))
  gameDisplay.blit(font.render('Fractal: '+str(fractal(complex((mouserectpos[0]*2-windowWidth)/halfWindowWidth,(mouserectpos[1]*2-windowHeight)/halfWindowHeight))),False,(0,0,0)),(10,50))
  pg.display.update()
