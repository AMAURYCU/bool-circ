import sys
sys.path.append('../')
from modules.utils import *

class node_mx:

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
  