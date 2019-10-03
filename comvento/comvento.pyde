import random
t0 = millis()
v=65
n=50
lis_teta = [PI*random.uniform(1/2,3/2) for i in range(n)]
g=10
u=[2,-5]

def setup():
    size(1700,1000)

def draw():
    for i in lis_teta:
        bola(i)
    


class bola():
    def __init__(self,teta):
        t = (millis()-t0)/1000.0
        self.x = 850
        self.y = 1000
        self.vx=v*cos(teta)
        self.vy=-v*sin(teta)
        self.x = self.x + self.vx*t + u[0]/2*t*t
        self.y = self.y + self.vy*t + (g+u[1])/2*t*t
        circle(self.x,self.y,20)
