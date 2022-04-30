import sys
sys.path.append('../')
from modules.utils import *

from modules.nodes import *
class open_digraph_get_set_mx:
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