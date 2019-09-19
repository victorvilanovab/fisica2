import random
t0 = millis()
v=70
teta1 = PI*random.uniform(1/2,3/2)
teta2 = PI*random.uniform(1/2,3/2)
teta3 = PI*random.uniform(1/2,3/2)
teta4 = PI*random.uniform(1/2,3/2)
teta5 = PI*random.uniform(1/2,3/2)
teta6 = PI*random.uniform(1/2,3/2)
teta7 = PI*random.uniform(1/2,3/2)
teta8 = PI*random.uniform(1/2,3/2)
teta9 = PI*random.uniform(1/2,3/2)
teta10 = PI*random.uniform(1/2,3/2)
teta11 = PI*random.uniform(1/2,3/2)
teta12 = PI*random.uniform(1/2,3/2)
teta13 = PI*random.uniform(1/2,3/2)
teta14 = PI*random.uniform(1/2,3/2)
teta15 = PI*random.uniform(1/2,3/2)
teta16 = PI*random.uniform(1/2,3/2)
teta17 = PI*random.uniform(1/2,3/2)
teta18 = PI*random.uniform(1/2,3/2)
teta19 = PI*random.uniform(1/2,3/2)
teta20 = PI*random.uniform(1/2,3/2)
def setup():
    size(1000,500)

def draw():
    bola(teta1)
    bola(teta2)
    bola(teta3)
    bola(teta4)
    bola(teta5)
    bola(teta6)
    bola(teta7)
    bola(teta8)
    bola(teta9)
    bola(teta10)
    bola(teta11)
    bola(teta12)
    bola(teta13)
    bola(teta14)
    bola(teta15)
    bola(teta16)
    bola(teta17)
    bola(teta18)
    bola(teta19)
    bola(teta20)
    


class bola():
    def __init__(self,teta):
        t = (millis()-t0)/1000.0
        self.x = 500
        self.y = 500
        self.vx=v*cos(teta)
        self.vy=-v*sin(teta)
        self.x=self.x + self.vx*t
        self.y=self.y+self.vy*t+5*t*t
        circle(self.x,self.y,20)
        
