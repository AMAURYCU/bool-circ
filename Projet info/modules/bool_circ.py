import sys
sys.path.append('../')
from modules.utils import *
from modules.open_digraph import *

class bool_circ(open_digraph):
  #def __init__(self,inputs,outputs,nodes):
  #  super().__init__(inputs,outputs,nodes)
    def __init__(self,*args):
        if type(args[0])==open_digraph:
            g=args[0]
            for k in g.nodes:
                if (g.nodes[k].label !='') and (g.nodes[k].label !='&') and(g.nodes[k].label !='|')and (g.nodes[k].label !='~'):
                    raise ValueError("probleme label")
                if (g.nodes[k].label =='') and ((g.nodes[k].outdegree()!=1) or (g.nodes[k].indegree()!=1)):
                    raise ValueError("erreur degre")
                if ((g.nodes[k].label=='&') or (g.nodes[k].label =='|')) and (g.nodes[k].outdegree()!=1):
                    raise ValueError("erreur degré")
                if(g.nodes[k].label =='~') and ((g.nodes[k].outdegree()!=1) or (g.nodes[k].indegree()!=1)):
                    raise ValueError("erreur degré")
            super().__init__(g.inputs,g.outputs,g.get_nodes())
        else:
            inputs = args[0]
            outputs = args[1]
            nodes = args[2]
            super().__init__(inputs,outputs,nodes)
      
    def __str__(self):
        '''
        output : str; what is displayed by str(graph)
        '''
        return ("("+str(self.inputs)+", "+str(self.nodes)
                    +", "+str(self.outputs)+")")
    
    def __repr__(self):
        '''
        output : str; the representation of a open_digraph
        '''
        return "bool_circ"+str(self)

    def to_graph(self):
        '''output: open_digraph, convert bool_circ in open_digraph'''
        g= open_digraph(self.inputs,self.outputs,self.get_nodes())
        return g
    def is_well_formed(self):
        '''output: bool, true if the bool_circ is well formed false else'''
        bc=self.copy()
        b=True
        b= b and bc.is_well_formed()
        b=b and(bc.is_cyclic()==False)
        for k in self.nodes:
            if self.nodes[k].label=='':
                b=b and(self.nodes[k].indegree()==1)
            if self.nodes[k].label == ('&' or '|' or '^'):
                b=b and(self.nodes[k].outdegree()==1)
            if self.nodes[k].label =='~':
                b=b and(self.nodes[k].outdegree()==1) and (self.nodes[k].indegree()==1)
            
        return b
        
    def parse_parentheses(self,*args):
        '''transforme self apres l'évaluation des expressions saisies'''
        liste = []
        for s in args:
      
            g = bool_circ([],[],[node(0,'',[],[])])
            
            current_node = 0
            compteur = 1
            s2 = ''
            for c in s:
                
                if c=='(':
                    g.nodes[current_node].label+=s2
                    g.nodes[current_node].parents += [compteur]
                    g.nodes[compteur]= node(compteur,'',[],[current_node])
                    current_node= compteur
                    compteur = compteur+1
                    
                    s2= ''
                elif c == ')':
                    g.nodes[current_node].label+=s2
                    current_node = g.nodes[current_node].children[0]
                    s2 = ''
                else:
                    s2 +=c
            l=[]
            for k in g.nodes:
                for k2 in g.nodes:
                    if k!=k2:
                        if (g.nodes[k].label == g.nodes[k2].label)and g.nodes[k].label!='&' and g.nodes[k].label != '~' and g.nodes[k].label !='|' :
                            
                            if (not(k,k2)in l) and (not(k2,k)in l):
                                print(l)
                                l= l+[(k,k2)]
            
            for k in l:
                print(k)
                dep = k[0]
                arr = k[1]
            
                g.fusnode(g.nodes[dep].id,g.nodes[arr].id,g.nodes[dep].label)
                
            liste+=[g]
            for k in range(1,len(liste)):
                liste[0].i_paralell(liste[k])
            l=[]
            for k in liste[0].nodes:
                for k2 in liste[0].nodes:
                    if k!=k2:
                        if (liste[0].nodes[k].label == liste[0].nodes[k2].label)and liste[0].nodes[k].label!='&' and liste[0].nodes[k].label != '~' and liste[0].nodes[k].label !='|' :
                            
                            if (not(k,k2)in l) and (not(k2,k)in l):
                              
                                l= l+[(k,k2)]
            
            for k in l:
              
                dep = k[0]
                arr = k[1]
               
                
                liste[0].fusnode(liste[0].nodes[dep].id,liste[0].nodes[arr].id,liste[0].nodes[dep].label)
        lret=[]
        for k in liste[0].nodes:
            if liste[0].nodes[k].parents ==[]:
                liste[0].inputs+= [k]
                lret += [liste[0].nodes[k].label]
                liste[0].nodes[k].label=''
            if liste[0].nodes[k].children ==[]:
                liste[0].outputs+=[k]
                
        
            
        
        
       
        self.__dict__=liste[0].__dict__
        return lret
    
def randBoolCirc(n,nbinp = None, nboutp=None):
    '''renvoie un circuit booléen '''
   
    g= randomg(n,n,form = 'DAG')
    gprime = g.copy()
    for k in gprime.nodes:
        if g.nodes[k].parents ==[]:
            g.inputs+=[k]
        if g.nodes[k].children==[]:
            g.outputs+=[k]
        
        if g.nodes[k].indegree()==g.nodes[k].outdegree() and g.nodes[k].outdegree()==1:
            opun =['~']
            g.nodes[k].label = opun[0]
        if g.nodes[k].indegree()==1 and g.nodes[k].outdegree()>1:
            g.nodes[k].label = ''
            
        elif g.nodes[k].indegree()>1 and g.nodes[k].outdegree()==1:
            opbin = ['&','|']
            a =random()
            if a >0.5:
                g.nodes[k].label = opbin[0]
            else:
                g.nodes[k].label = opbin[1]
        
        elif g.nodes[k].indegree()>1 and g.nodes[k].outdegree()>1:
            n1 = node(g.max_id()+1,'',[],[])
            n2 = node(g.max_id()+2,'',[],[])
       
            g.nodes[n1.id]=n1
            g.nodes[n2.id]=n2
            
            for d in g.nodes:
                
                if k!=d:
                   
                    for e in range(len(g.nodes[d].parents)):
                        if g.nodes[d].parents[e]==k:
                            g.nodes[d].parents[e]=n2.id
                            g.nodes[n2.id].children+=[g.nodes[d].id]
                            
                    for f in range(len(g.nodes[d].children)):
                        if g.nodes[d].children[f]==k:
                            g.nodes[d].children[f]=n1.id
                            g.nodes[n1.id].parents+=[g.nodes[d].id]
            g.nodes[n1.id].children = [n2.id]
            g.nodes[n2.id].parents = [n1.id]
            
            g.remove_allnode_occ(k)
            print(g)
    
    if nbinp == None and nboutp ==None:
        
        return g
    elif nbinp!= None or nboutp == None:
        
        while nbinp > len(g.inputs):
            a = randint(g.min_id(),g.max_id())
            while not(a in g.nodes):
                a = randint(g.min_id(),g.max_id())
            g.inputs+= [a]
    
        while nbinp < len(g.inputs):
            N = choice(g.inputs)
            N2 = choice(g.inputs)
            while N2== N:
                N2 = choice(g.inputs)
            n = node(g.max_id()+1,'',[],[N,N2])
            g.inputs.remove(N)
            g.inputs.remove(N2)
            
            g.nodes[N].parents+=[n.id]
            g.nodes[N2].parents+= [n.id]
            
        
        while nboutp > len(g.outputs):
            a = randint(g.min_id(),g.max_id())
            while not(a in g.nodes):
                a = randint(g.min_id(),g.max_id())
            g.outputs+= [a]
    
        
        while nboutp < len(g.outputs):
            N = choice(g.outputs)
            N2 = choice(g.outputs)
            while N2== N and g.outputs>=2:
                N2 = choice(g.outputs)
            n = node(g.max_id()+1,'',[N,N2],[])
            g.outputs.remove(N)
            g.outputs.remove(N2)
            
            g.nodes[N].children+=[n.id]
            g.nodes[N2].children+= [n.id]
        for k in g.nodes:
            if g.nodes[k].indegree() ==g.nodes[k].outdegree() and g.nodes[k].indegree()==1:
                g.nodes[k].label = '~'
            if g.nodes[k].indegree()==1 and g.nodes[k].outdegree()>1:
                g.nodes[k].label = ''
                
            if g.nodes[k].indegree()>1 and g.nodes[k].outdegree()==1:
                opbin = ['&','|']
                a =random()
                if a >0.5:
                    g.nodes[k].label = opbin[0]
                else:
                    g.nodes[k].label = opbin[1]
    return g
        
    
    
            
        








