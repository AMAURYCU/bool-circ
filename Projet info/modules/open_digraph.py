import sys
sys.path.append('../')
from modules.utils import *

class node:

  def __init__(self, identity, label, parents, children):
    '''
    identity: int; its unique id in the graph
    label: string;
    parents: int list; a sorted list containing the ids of its parents
    children: int list; a sorted list containing the ids of its children
    '''
    self.id = identity
    self.label = label
    self.parents = parents
    self.children = children

  def __str__(self):
    '''
    output : str; the result of str(node)
    '''
    return ("("+str(self.id)+", "+self.label+", "
              +str(self.parents)+", "+str(self.children)+")")
  
  def __repr__(self):
    '''
    output : str; the representation of a node
    '''
    return "node"+str(self)

  def copy(self):
    '''
    output : node;
    returns a copy of the node
    '''
    return node(self.id, self.label, self.parents.copy(),
                                     self.children.copy())
              
              
  #debuts getters -----------------            
  def get_id(self):
    '''output: int; id of node'''
    return self.id
  def get_label(self):
    '''output: char; label of node'''
    return self.label
  def get_parent_ids(self):
    '''output: int list; id of parents'''
    return self.parents
  def get_children_ids(self):
    '''output: int list; id of children'''
    return self.children
  #fin getters ---------------------
  #debut setters -------------------
  def set_id(self,nid):
    ''' input: int; new id /change the id of node'''
    self.id = nid
  def set_label(self,nlabel):
    ''' input : char; new char /change the label of node'''
    self.label = nlabel
  def set_parent_ids(self,nparid):
    ''' input: int list; new parents ids / change the ids of parents'''
    self.parents = nparid
  def set_children_ids(self,nchilid):
    ''' input: int list; new children ids/ chage the ids of children'''
    self.children = nchilid
  def add_child_id(self,nid):
    ''' input: int; new children id / add nid to the id of children'''
    self.children= self.children+[nid]
  def add_parent_id(self,nid):
    '''input: int; new parent id/ add nid to the id of parent'''
    self.parents= self.parents+ [nid]
    
  def remove_parent_id(self,id):
    ''' input: int; id to remove/ remove the parent id'''
    self.parents = remove_one(self.parents , id)
  def remove_child_id(self,id):
    ''' input : int; id to remove/ remove the child id'''
    self.children = remove_one(self.children,id)
  def remove_parent_id_all(self,id):
    ''' input int; id to remove/ remove all the parent id'''
    self.parents = remove_all(self.parents,id)
  def remove_child_id_all(self,id):
    ''' input int; id to remove / remove all the child id'''
    self.children= remove_all(self.children,id)
  #fin setters -----------------------------------------------
  
  
  def indegree(self):
    '''output: int, the in degree of the node'''
    return len(self.parents)
  def outdegree(self):
    '''output: int, the outdegree of the node'''
    return len(self.children)
  def degree(self):
    '''output: int, the degree of the node'''
    return self.indegree()+self.outdegree()
class open_digraph(): # for open directed graph

  def __init__(self, inputs, outputs, nodes):
    '''
    inputs: int list; the ids of the input nodes
    outputs: int list; the ids of the output nodes
    nodes: node list;
    '''
    self.inputs = inputs
    self.outputs = outputs
    self.nodes = {node.id:node for node in nodes} # self.nodes: <int,node> dict

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
    return "Open_digraph"+str(self)

  def empty():
    '''
    output : open_digraph; returns an empty graph
    '''
    return open_digraph([], [], [])
    
  def copy(self):
    '''output: open_digraph; return a copy of self'''
    l=[]
    for k in self.nodes:
      l= l+[self.nodes[k].copy()]
    odg1= open_digraph(self.inputs.copy(),self.outputs.copy(),l)
    return odg1
    
    
    
    

  #debuts getters ----------
  def get_input_ids(self):
    return self.inputs
  def get_output_ids(self):
    return self.outputs
  def get_id_node_map(self):
    return self.nodes
  def get_node_ids(self):
    return list(self.nodes.keys())
  def get_nodes(self):
    l = []
    for k in self.nodes:
      l = l+[self.nodes[k]]
    return l
    
  def get_node_by_id(self,id):
    return self.nodes[id]
  def get_nodes_by_ids(self,ids):
    l=[]
    for k in range(len(ids)):
      l=l+[self.nodes[ids[k]]]
    return l
  
  #fin getters -----------
  #debuts setters -------------
  def set_input_ids(self,nids):
    self.inputs = nids
  def set_output_ids(self,nids):
    self.outputs = nids
  def add_input_id(self,nid):
    self.inputs = self.inputs+[nid]
  def add_output_id(self,nid):
    self.outputs = self.outputs+[nid]
  #fin setters ------------------------
      
      
  def new_id(self):
    '''output: int; id un used in the graph'''
    l= self.get_node_ids()+self.get_input_ids()+self.get_output_ids()
    #on parcour les entiers jusqu a tomber sur un entier inutilisé
    
    n=0 
    while (n in l == True):
      n=n+1
    return n
    
  def add_edge(self,src,tgt):
    '''inputs int² id of source id of target '''
    #on ajoute un enfant a la source et un parent a la target
    self.nodes[src].add_child_id(tgt)
    self.nodes[tgt].add_parent_id(src)
  def add_edges(self,srcs,tgts):
    '''inputs 2 int list; ids of target and ids of sources'''
    for k in range(len(srcs)):
      self.add_edge(srcs[k],tgts[k])
    
  def add_node(self,label,parents,children):
    '''inputs char, int list, int list,informations on the added node'''
    id = self.new_id
    n0 = node(id,label,parents,children)
    for k in parents:
      self.nodes[k].add_child_id(id)
    for k in children:
      self.nodes[k].add_parent_id(id)
    self.nodes[id]=n0
    return id
  
  def add_node2(self,label,parents,children,id):
    n0 = node(id,label,parents,children)
    for k in parents:
      self.nodes[k].add_child_id(id)
    for k in children:
      self.nodes[k].add_parent_id(id)
    self.nodes[id]=n0
    
  def add_node_node(self,n):
    self.add_node(n.label,n.parents,n.children)
    
  
  def remove_edge(self,src,tgt):
    '''input: int int; id of the source and the target'''
    self.nodes[src].remove_child_id(tgt)
    self.nodes[tgt].remove_parent_id(src) 
  
  def remove_node_by_id(self,id):
    '''input int ; id of the node to remove'''
    #on supprime les aretes et on enleve le node du dictionnaire
    for k in self.nodes:
      self.remove_edge(id,k)
      self.remove_edge(k,id)
    x = self.nodes.pop(id)
    
  def remove_allnode_occ(self,id):
  
    for k in self.nodes:
      while id in self.nodes[k].parents:
        self.nodes[k].parents.remove(id)
      while id in self.nodes[k].children:
        self.nodes[k].children.remove(id)
    x= self.nodes.pop(id)
    
  def remove_allnode_occ_list(self,ids):
    for k in ids:
      self.remove_allnode_occ(k)
  def remove_edges(self,srcs,tgts):
    '''input int list,int llist; ids of the source and of the target'''
    for k in range(len(src)):
      self.remove_edge(srcs[k],tgts[k])
      
  def remove_nodes_by_ids(self,ids):
    '''ids of the nodes to remove'''
    for k in range(len(ids)):
      self.remove_node_by_id(ids[k])
    
  
  def is_well_formed(self):
    '''output : bool; true if the graph is well formed false else'''
      
    for k in self.inputs:
      c=0
      for k2 in self.nodes:
        if count_occurrences(self.nodes[k2].parents,k)!=0:
          c=c+1
      
      if c==0:
        return False
    
        
      
    for k in self.outputs:
      c=0
      for k2 in self.nodes:
        if count_occurrences(self.nodes[k2].children,k)!=0:
          c=c+1
      
      if c == 0:
        return False
      
    for k in self.nodes:
      
      if self.nodes[k].id !=k:
        return False
  
    for k in self.nodes:
        l0 = remove_list(remove_list(self.nodes[k].children,self.inputs),self.outputs)
        for k2 in l0:
            l1 = remove_list(remove_list(self.nodes[k2].parents,self.inputs),self.outputs)
            if count_occurrences(l0,k2)!= count_occurrences(l1,k):
                return False
            
            
    return True
    
    
  def max_indegree(self):
    '''output: int, max in degree of a node of the graph'''
    if len(self.get_node_ids())>=1:
      c=0
      for k in self.nodes:
        if self.nodes[k].indegree()>c:
          c=self.nodes[k].indegree()
    else:
      raise("graphe vide")
    return c
    
  def max_outdegree(self):
    '''output: int, max out degree of a node of the graph'''
    if len(self.get_node_ids())>=1:
      
      c= 0
      for k in self.nodes:
        if self.nodes[k].outdegree()>c:
          c=self.nodes[k].outdegree()
    else:
      raise ValueError("graphe vide")
    return c
    
  def min_indegree(self):
    '''output: int, min in degree of a node of the graph'''
    if len(self.get_node_ids())>=1:
      c= self.get_nodes()[0].indegree()
      for k in self.nodes:
        if self.nodes[k].indegree()<c:
          c=self.nodes[k].indegree()
    else:
      raise ValueError("graphe vide")
    return c
  def min_outdegree(self):
    '''output: int, min out degree of a node of the graph'''
    if len(self.get_node_ids())>=1:
      c=self.get_nodes()[0].outdegree()
      for k in self.nodes:
        if self.nodes[k].outdegree()<c:
          c=self.nodes[k].outdegree()
    else:
      raise ValueError("graphe vide")
    return c
  def max_degree(self):
    '''output: int, max degree of a node of the graph'''
    if len(self.get_node_ids())>=1:
      c=0
      for k in self.nodes:
        dg = self.nodes[k].degree()
        if dg>c:
          c=dg
    else:
      raise ValueError("graphe vide")
    return c
    
    
  def min_degree(self):
    '''output: int, min degree of a node of the graph'''
    if len(self.get_node_ids())>=1:
      c=self.get_nodes()[0].degree()
      for k in self.nodes:
        dg = self.nodes[k].degree()
        if dg <c:
          c=dg
    else:
      raise ValueError("graphe vide")
    return c
  
  def vire_output(self):
    '''enleve les outputs des nodes '''
    for k in self.nodes:
      for j in self.nodes[k].children:
        if j in self.outputs:
          self.nodes[k].remove_child_id(j)
  def vire_input(self):
    '''enleve les outputs des nodes '''
    for k in self.nodes:
      for j in self.nodes[k].parents:
        if j in self.inputs:
          self.nodes[k].remove_parent_id(j)
  
  def is_cyclic(self,b=True):
    '''input:bool, default true
    output: bool, true if the graph is cyclic false else'''
    
    if b:
      odg= self.copy()
      odg.vire_output()
    else:
      odg=self
    print(odg)
    if len(self.nodes)==0:
      
      return False
    else:
      c=[]
      odg.vire_output()
      for k in odg.nodes:
        if odg.nodes[k].children==[]:
          c=c+[k]
      if c !=[]:
        odg.remove_allnode_occ_list(c)
        return odg.is_cyclic(False)
      
      else:
        return True
        
  def min_id_output(self):
    '''return l'output de plus petit id'''
    if self.outputs !=[]:
      
      c= self.outputs[0]
      for k in self.outputs:
        
        if k<c:
          print(c)
          c=k
      return c
    else:
      return 0
  def max_id_inputs(self):
    '''return l'input d'id max'''
    if self.inputs !=[]:
      c= self.inputs[0]
      for k in self.inputs:
        if k>c:
          c=k
      return k
    else:
      return 0
  def min_id_inputs(self):
    '''return l'input de plus petit id'''
    if self.inputs !=[]:
      c= self.inputs[0]
      for k in self.inputs:
        if k<c:
          c=k
      return c
    else:
      return 0
  def max_id_output(self):
    '''return l'output de plus grand id'''
    if self.outputs!=[]:
      c= self.outputs[0]
      for k in self.outputs:
        if k>c:
          c=k
      return c
    else:
      return 0
    
    
    
  def min_id_node(self):
    '''retourne l'id du node de plus petit id'''
    c= self.get_node_ids()[0]
    l= self.get_node_ids()
    for k in l:
      if k<c:
        c=k
    return c
  def max_id_node(self):
    ''' retourne l'id du node le plus grand'''
    c= self.get_node_ids()[0]
    l= self.get_node_ids()
    for k in l:
      if k>c:
        c=k
    return c
  def max_id(self):
    '''retourne l'id du node le plus grand input et output confondu'''
    return max(max(self.max_id_inputs(),self.max_id_output()),self.max_id_node())
  def min_id(self):
    '''retourne l'id du node le plus petit input et output confondu'''
    return min(min(self.min_id_inputs(),self.min_id_output()),self.min_id_node())
  def shift_indices(self,n):
    '''décale tout les indices de self de n'''
  
    d=self.get_node_ids()
    for k in d :
      self.nodes[k].id=self.nodes[k].id+n
      
      d2=self.nodes[k].parents
      d3= self.nodes[k].children
      d4= remove_list(d2,self.inputs+self.outputs)
      d6= remove_list(d3,self.inputs+self.outputs)
      for l in range(len(d2)):
        
        self.nodes[k].parents[l] = self.nodes[k].parents[l]+n
      for v in range(len(d3)):
        self.nodes[k].children[v] = self.nodes[k].children[v]+n
      x= self.nodes.pop(k)
      self.nodes[k+n]=x
    for y in range(len(self.inputs)):
      self.inputs[y] += n
    for z in range(len(self.outputs)):
      self.outputs[z]+=n
      
      
  def shift_indices_sans_IO(self,n):
    ''' décale tout les id de self de n sans toucher aux inputs et outputs'''
    d=self.get_node_ids()
    for k in d :
      self.nodes[k].id=self.nodes[k].id+n
      
      d2=self.nodes[k].parents
      d3= self.nodes[k].children
      d4= remove_list(d2,self.inputs+self.outputs)
      d6= remove_list(d3,self.inputs+self.outputs)
      for l in range(len(d2)):
        if self.nodes[k].parents[l] in d4:
          self.nodes[k].parents[l] = self.nodes[k].parents[l]+n
      for v in range(len(d3)):
        if self.nodes[k].children[v] in d6:
          self.nodes[k].children[v] = self.nodes[k].children[v]+n
      x= self.nodes.pop(k)
      self.nodes[k+n]=x
    #for y in range(len(self.inputs)):
     # self.inputs[y] += n
    #for z in range(len(self.outputs)):
     # self.outputs[z]+=n
      
  def i_paralell(self,g):
    '''fusionne le graphe self avec le graphe g en paralelle'''
    '''algo: on décale touts les indices de g de (max(abs(g.max_id()-self.min_id()+1),abs(self.max_id()-g.min_id()+1))) puis on ajoute les nodes de self aux nodes de g de meme avec les inputs et les outputs'''
    self.shift_indices(max(abs(g.max_id()-self.min_id()+1),abs(self.max_id()-g.min_id()+1)))
    
    self.inputs = self.inputs+g.inputs
    self.outputs = self.outputs+g.outputs
    for k in g.nodes:
      self.nodes[k]=g.nodes[k]
      
  def parallel(self,g):
    '''idem que i_paralell sauf que renvoie la fusion de self et g sans les modifier'''
    g2= g.copy()
    f=self.copy()
    f.i_paralell(g2)
    return f
    
  def icompose(self,g):
    '''renvoie self deviens la composition séquentielle de self et g'''
    '''algo: on décale les indices de self de la quantité ligne 539 puis on relie les outputs de self aux  inputs de g  '''
    if len(self.inputs)!= len(g.inputs):
      raise ValueError("erreur")
    self.shift_indices(g.max_id()-self.min_id()+1)
    for n in g.nodes:
      self.nodes[n]=g.nodes[n]
      for k in range (len(g.outputs)):
        if  g.outputs[k] in g.nodes[n].children:
          for j in self.nodes:
            if self.inputs[k] in self.nodes[j].parents:
              self.add_edge(n,j)
    self.inputs = g.inputs
    for n in self.nodes:
      if n in g.nodes:
        print(1)
        remove_list(self.nodes[n].children,g.outputs)
      else:
        print(2)
        remove_list(self.nodes[n].parents,self.inputs)
      for n2 in self.nodes[n].parents:
        if not(n2 in self.nodes) and not(n2 in self.inputs) and not(n2 in self.outputs):
          self.nodes[n].parents.remove(n2)
      for n3 in self.nodes[n].children:
        if not(n3 in self.nodes) and not(n3 in self.inputs) and not(n3 in self.outputs):
          self.nodes[n].children.remove(n3)
    
  def compose(self,g):
    '''idem que icompose sauf que renvoie la fusion sans modifier self et g'''
    s=self.copy()
    G=g.copy()
    s.icompose(G)
    return s            
        
  def connected_components(self):
    '''renvoie les composentes connexe d'un graph'''
    l=self.get_node_ids()
    d={}
    c=0
    l2 = []
    s=self.copy()
    
    for k in l:
      d[k]= -1
    for k2 in d:
      if d[k2]== -1 and (k2 in l):
        d[k2]=c
        for k3 in remove_list(s.nodes[k2].parents,self.inputs):
          if d[k3]== -1:
            d[k3]=c
        for k4 in remove_list(s.nodes[k2].children,self.outputs):
          if d[k4]==-1:
            d[k4]=c
        remove_one(l,k2)
        c=c+1
      if d[k2]!=-1  and (k2 in l):
        for k3 in remove_list(s.nodes[k2].parents,self.inputs):
          if d[k3]== -1:
            d[k3]= d[k2]
        for k4 in remove_list(s.nodes[k2].children,self.outputs):
          if d[k4]== -1:
            d[k4]=d[k2]
        remove_one(l,k2)
    return d
      
  
        
        
  def Dijkstra(self,src, direction = None,tgt = None):
    '''implémentation de l'algo de dijkstra 
    inputs graph self, int src : l'id duquel on part,direction int -1 on parcour le graphe danns le sens inverse 1 on parcour le graph dans le bon sens , None on parcour le graph dans tout les sens, tgt int l'id cible
    outputs dist:dict les distances a chaque noeuds , prev dictles noeuds précédents'''
    g = self.copy()
    if tgt == None:
      
      g.vire_output()
      g.vire_input()
      Q = [src]
      dist = {src:0}
      prev = {}
      while Q !=[]:
        for k in Q:
          d=k
          break
        for k in Q:
          if dist[k]<dist[d]:
            d=k
        u=d
        Q.remove(u)
        if(direction ==1):
          neighbours = g.nodes[u].children
        if(direction ==-1):
          neighbours = g.nodes[u].parents
        if(direction == None):
          neighbours = g.nodes[u].children + g.nodes[u].parents
        for v in neighbours:
          if not(v in dist):
            Q=Q+[v]
          if not(v in dist) or dist[u]>dist[u]+1:
            dist[v]=dist[u]+1
            prev[v]=u
      return dist,prev
    else:
      g.vire_output()
      g.vire_input()
      Q = [src]
      dist = {src:0}
      prev = {}
      
      while (Q !=[]) and not (tgt in dist):
        for k in Q:
          d=k
          break
        for k in Q:
          if dist[k]<dist[d]:
            d=k
        u=d
        Q.remove(u)
        if(direction ==1):
          neighbours = g.nodes[u].children
        if(direction ==-1):
          neighbours = g.nodes[u].parents
        if(direction == None):
          neighbours = g.nodes[u].children + g.nodes[u].parents
        for v in neighbours:
          if not(v in dist):
            Q=Q+[v]
          if not(v in dist) or dist[u]>dist[u]+1:
            dist[v]=dist[u]+1
            prev[v]=u
      return dist,prev
  
  
  def shortest_path(self,src,tgt,direction=None):
    '''retourne la liste des id des noeuds tel que en passant par ces noeuds la distance entre src et tgt soit minimale'''
    prev = self.Dijkstra(src,direction,tgt)[1]
    l=[]
    a= tgt
    while(a != src):
      l= l+[a]
      a= prev[a]
    l=reverse(l)
    return l
  
  def distComAnsestor(self,node1,node2,direction = None):
    '''retourne la distance au l'ancetre commun entre node1 et node2'''
    ancestor1 = self.Dijkstra(node1,-1)[1]
    ancestor2 = self.Dijkstra(node2,-1)[1]
    dist = {}
  
    for k in ancestor1:
      if k in ancestor2:
        dist[k]=(len(self.shortest_path(node1,k)),len(self.shortest_path(node2,k)))
    return dist
  
      
  def triTopo(self):
    '''si le graphe est cyclique renvoie le tri topologique de self et une erreur sinon'''
    if self.is_cyclic()==False:
      g= self.copy()
      g.vire_input()
      g.vire_output()
      l=[]
      c=0
      inl= g.inputs
      g.remove_allnode_occ_list(inl)
      l=l+[inl]
      while g.nodes !={}:
        print(g)
        inl =[]
        for k in g.nodes:
          
          if g.nodes[k].parents ==[]:
      
            inl = inl+[k]
        g.remove_allnode_occ_list(inl)
        l=l+[inl]
      return l
    else:
      raise ValueError("GrapheCyclique")
    
  
  def profondeurNode(self,nodeId):
    '''renvoie la profondeur du noeud d'id nodeId'''
    l = self.triTopo()
    for k in range(len(l)):
      for j in l[k]:
        if j == nodeId:
          return k
    raise ValueError("noeud pas dans graphe")
  
  def profondeurGraphe(self):
    '''renvoie la profondeur du graph'''
    l= self.triTopo()
    return len(l)
  

  
  def chemainPlusLong(self, depart,arrivee):
    g= self.copy()
    g.vire_input()
    g.vire_output()
    tt = g.triTopo()
    dist = {}
    prev = {}
    c= 0
    iatteint = False
    for k in range(len(tt)):
      for i in tt[k]:
        if i == depart:
          dist[depart]=0
          prev[depart]= depart
          c= k
    for k in range(c+1, len(tt)):
      for i in tt[k]:
        par={}
        for j in g.nodes[i].parents:
          if j in dist:
            par[j]=dist[j]
        if par != {}:
          z= maxg(par)
          dist[i]=dist[z]+1
          prev[i]=z
        if(i==arrivee):
          iatteint = True
          break
      if iatteint:
        break
    return dist,prev
  
  def vraiChemainPlusLong(self,depart,arrivee):
    ''' renvoie le chemain le plus long ainsi que la distance a parcourir entre depart et arrivee'''
    way = self.chemainPlusLong(depart,arrivee)[1]
    dist = self.chemainPlusLong(depart,arrivee)
    l=[]
    d=arrivee
    while d !=depart:
      l= l+ [d]
      d=way[d]
    l=l+[depart]
    l= reverse(l)
    return l,len(l)-1
      
    
            
  def fusnode (self,n1,n2,label):
    '''fusionne les noeudes n1 et n2 et donne le label label a la fusion'''
    n = node(self.nodes[n1].id,label,enleveDoublon(self.nodes[n1].parents+self.nodes[n2].parents),(self.nodes[n1].children+self.nodes[n2].children))  
    
    nn2 = node(self.nodes[n2].id,label,self.nodes[n2].parents,self.nodes[n2].children)     
    self.remove_node_by_id(n2)
    for k in self.nodes:

      if k in nn2.parents:
       
        n.parents+= [k]
        self.nodes[k].children +=[n.id]
        self.nodes[k].children=enleveDoublon(self.nodes[k].children)
        
      if k in nn2.children:
 
        n.children+=[k]
        self.nodes[k].parents =self.nodes[k].parents+[n.id]
        self.nodes[k].parents = enleveDoublon(self.nodes[k].parents)
    n.parents = enleveDoublon(n.parents)
    n.children=enleveDoublon(n.children)
    self.nodes[n1]= n
      
      
          
          
          
          
def graph_from_adjacency_matrix(l):
  '''renvoie un graphe a partir d'une matrice dadjacence présentée sour la forme d'une liste de liste'''
  odg = open_digraph([],[],[])
  for k in range(len(l)):
      odg.add_node2('a',[],[],k)
  for i in range(len(l)):
      for j in range(len(l)):
          p=l[i][j]
          for k in range(p):
              odg.add_edge(i,j)

  return odg

def randomg(n, bound,inputs=0,outputs = 0, form = "free"):
  '''crée un graph aléatoire 
  free= sans contrainte
  dag = dirigé acyclique
  oriented = orienté
  ...'''
  if form == "free":
    m = random_int_matrix(n,bound,False)
  elif form=="DAG":
    m= random_triangular_int_matrix(n,bound,True)
  elif form =="oriented":
    m= random_oriented_int_matrix(n,bound,False)
  elif form == "undirected":
    m= random_symetric_int_matrix(n,bound,False)
  elif form == "loop-free undirected":
    m= m= random_symetric_int_matrix(n,bound)
  elif form == "loop-free oriented":
    m= random_oriented_int_matrix(n,bound) 
  elif form == "loop-free DAG":
    m= random_triangular_int_matrix(n,bound)
  elif form =="loop-free":
    m= random_int_matrix(n,bound)
  else:
    raise ValueError("mauvais arg")
  odg = graph_from_adjacency_matrix(m)
  for i in range(inputs):
    n= choice(odg.get_node_ids())
    odg.inputs= odg.inputs+[n]
    odg.remove_node_by_id(n)
  for j in range(outputs):
    n= choice(odg.get_node_ids())
    odg.outputs= odg.outputs+[n]
    odg.remove_node_by_id(n)
  return odg
  
 
















