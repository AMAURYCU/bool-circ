import sys
sys.path.append('../') # allows us to fetch files from the project root

from PIL import ImageDraw,Image
import math
import random 

from modules.open_digraph import *
from modules.utils import *
from math import *
from modules.bool_circ import*
width = 1000
height = 1000
class point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def n(self):
        return (round(self.x),round(self.y))
    def copy(self):
        p = point(self.x,self.y)
        return p
    def __add__(self,p2):

        self.x=self.x+p2.x
        self.y = self.y+p2.y
    def __rmul__(self,s):
    
        self.x=self.x*s
        self.y=self.y*s
    def __sub__(self,p2):
        self.x=self.x-p2.x
        self.y=self.y-p2.y
    def __repr__(self):
        return ""+str(self.x)+ " "+str(self.y)
    def translate(self,vect):
        
        self=self+vect
    
        
        
    def rotate(self,theta,c):
      
        -1*c
   
        self.translate(c)
        sx = self.x
        sy = self.y
      
        self.x = sx*cos(theta)-sy*sin(theta)
        self.y = sx * sin(theta)+sy*cos(theta)
        
        -1*c
        self.translate(c)




def drawarrows(self,p1,p2,color):
    self.line([p1.n(),p2.n()],color)
    mil = point((p1.x+p2.x)/2,(p1.y+p2.y)/2)
    a = point(mil.x-5,mil.y+5)
    b = point(mil.x-5,mil.y-5)
    a.rotate(-slope_angle(p1,p2),mil)
    b.rotate(-slope_angle(p1,p2),mil)
    self.line([mil.n(),a.n()],color)
    self.line([mil.n(),b.n()],color)
   


    

    
    
    
def drawnode(self,n,p,verbose=False):
    self.ellipse((p.x-40,p.y-40,p.x+40,p.y+40),fill='white',outline='black')
    self.text((p.x,p.y),n.label,fill='black')
    if verbose==True:
        self.text((p.x+20,p.y+20),str(n.id),fill='red')
        
def drawgraph(self,g,method='manual',node_pos=None,input_pos=None,output_pos=None):
    if method == 'manual':
        for k in node_pos:
            self.node(g.nodes[k],node_pos[k],True)
            
        if input_pos !=None:
            for k in g.inputs:
                for n in g.nodes:
                    if k==n:
                        
                        self.arrows(input_pos[k],node_pos[n],'red')
        if output_pos !=None:
            for k in g.outputs:
                for n in g.nodes:
                    if k ==n:
                        self.arrows(output_pos[k],node_pos[n],'green')
        for k3 in g.nodes:
            for l3 in g.nodes[k3].children:
                if l3 in g.nodes:
                    self.arrows(node_pos[k3],node_pos[l3],'black') 
    if method =='random':
        nod,inp,outp = random_layout(g)
        self.graph(g,'manual',nod,inp,outp)
    if method == 'circle':
        nod,inp,outp = circle_layout(g)
        self.graph(g,'manual',nod,inp,outp)
    if method == 'couche':
        nod, inp,outp= DAG_layout(g)
        self.graph(g,'manual',nod,inp,outp)
    
        
        
def distance(p1,p2):
     return math.sqrt((p2.x-p1.x)**2 +(p2.y-p1.y)**2)  
        

def random_layout(odg):
    d={}
    inp={}
    outp={}
    for k in odg.nodes:
        p=point(uniform(0,height),uniform(0,width))
        d[k]=p
        
    for k in odg.inputs:
        inp[k]=point(uniform(0,height),uniform(0,width))
    for k in odg.outputs:
        outp[k]=point(uniform(0,height),uniform(0,width))
    return(d,inp,outp)

#####continuer td 4 question 7

def circle_layout(odg):
    
    d={}
    inp={}
    out = {}
    l= odg.get_node_ids()
    c= len(l)
    cinp = len(odg.inputs)
    cout= len(odg.outputs)
    if c !=0:
        theta = 2*math.pi/c
        for k in range(len(l)):
            p= point(height/2+200,width/2)
            for compteur in range(k):
                p.rotate(theta,point(height/2, width/2))
            lcrochetk = l[k]
            d[lcrochetk]=p
    if cinp !=0:
        thetainp =-math.pi/cinp  
        for k in range(cinp):
            p= point(height/2,width/2+300)
            for compteur in range(k):
                p.rotate(thetainp,point(height/2,width/2))
            inp[odg.inputs[k]]=p
    if cout !=0:
        
        thetaout = math.sqrt(2)*math.pi/cout
        for k in range(cout):
            p = point(height/2 ,width/2-300)
            for compteur in range(k):
                p.rotate(thetaout,point(height/2,width/2))
            out[odg.outputs[k]]=p
        
            
    return d,inp,out
    
def slope_angle(p1,p2):
    if p2.x!=p1.x:
        return atan((p2.y-p1.y)/(p2.x-p1.x))
    else:
        return math.pi/2
    
    
def DAG_layout(odg):
    l = odg.triTopo()
    c = len(l)
    posy = []
    posx = []
    aza =  200
    azb = 100
    d={}
    inp = {}
    outp={}
    for k in range(c):
        posy += [aza]
        aza += height/c
    for i in range(len(l)):
        pose =[]
        for j in range(len(l[i])):
            pose+= [azb]
            azb += width/len(l[i])
        azb = 100
        posx += [pose]
    print(posx)
    print(posy)
    print(l)
    for k in range(c):
        for i in range(len(l[k])):
          
           print(i) 
           d[l[k][i]]=point(posx[k][i],posy[k])
    cinp = 0
    cout =0
    for k in odg.inputs:
        inp[k]= point(cinp,0)
        cinp += width /len(odg.inputs)
    for k in odg.outputs:
        outp[k]= point(cout,height)
        cout += width/len(odg.outputs)
    return d,inp,outp
        






odg4= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3,0], [6]),node(0, 'b', [1], [7,5,4])])
        
        
ImageDraw.ImageDraw.graph=drawgraph    
ImageDraw.ImageDraw.node=drawnode
ImageDraw.ImageDraw.arrows = drawarrows
odg5=open_digraph([0,1,2],[],[node(0,'',[],[3]),node(1,'',[],[5,8,4]),node(2,'',[],[4]),node(3,'',[0],[7,5,6]),node(4,'',[1,2],[6]),node(5,'',[3,1],[7]),node(6,'',[3,4],[8,9]),node(7,'',[3,5],[]),node(8,'',[1,6],[]),node(9,'',[6],[])])
p1= point(100,100)
p2 = point(300,300)
odg1= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3,0], [6]),node(0, 'b', [1], [7,5,4])])
n0 = node(0, 'a', [], [1])
d={4:p1,0:p2}
d2={1:point(0,0),2:point(20,0),3:point(30,0)}
d3={5:point(0,800),6:point(20,800),7:point(30,800)}
image = Image.new("RGB",(width,height),'white')
draw = ImageDraw.Draw(image)

bc= open_digraph([2,4,5],[0],[node(0, '|', [1, 6], []),node(1, '&', [2, 3], [0]),node(2,'' , [], [1]),node(3, '&', [4, 5], [1]),node(4,'' , [], [3, 6]),node(5,'' , [], [3, 8]),node(6, '&', [4, 8], [0]),node(8, '~', [5],[6])])
#draw.line([p1.n(),p2.n()],'black')
#draw.rectangle([(130,150),(170,190)],outline = 'black')
#draw.text((150,170), "& | ~", fill='black')
#draw.ellipse((100, 100, 150, 200), fill='white', outline='black')
#draw.node(n0,p1,True)
randbc = randBoolCirc(5,3,3)
draw.graph(randbc,'couche')
draw.text((0,0),"lmqjsdflmsjqfd",'black')
image.save("test.jpg")












