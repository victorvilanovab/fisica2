import random
t0 = millis()
v=80
n=50
lis_teta = [PI*random.uniform(1/2,3/2) for i in range(n)]
g=20
u=[-4,0]

def setup():
    size(1300,700)

def draw():
    for i in lis_teta:
        bola(i)
    


class bola():
    def __init__(self,teta):
        t = (millis()-t0)/1000.0
        self.x = 650
        self.y = 700
        self.vx=v*cos(teta)
        self.vy=-v*sin(teta)
        self.x = self.x + self.vx*t + u[0]/2*t*t
        self.y = self.y + self.vy*t + 5*t*t
        circle(self.x,self.y,20)
        
