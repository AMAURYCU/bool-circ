import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.open_digraph import *
from modules.utils import *
from modules.open_digraph_get_set_mx import*
from modules.nodes import*



class InitTest(unittest.TestCase):

	def test_init_node(self):
		n0 = node(0, 'i', [], [1])
		self.assertEqual(n0.id, 0)
		self.assertEqual(n0.label, 'i')
		self.assertEqual(n0.parents, [])
		self.assertEqual(n0.children, [1])
		self.assertIsInstance(n0, node)

	def test_init_open_digraph(self):
		g0 = open_digraph([],[],[])
		self.assertEqual(g0.inputs,[])
		self.assertEqual(g0.outputs,[])
		self.assertEqual(g0.nodes,{})
		self.assertIsInstance(g0,open_digraph)
		g1= open_digraph([1,2],[5,6],[node(3,"a",[2],[5]),node(4,"b",[1],[6])])
		self.assertEqual(g1.inputs,[1,2])
		self.assertEqual(g1.outputs,[5,6])
		self.assertEqual(sorted(g1.nodes.keys()),[3,4])
		self.assertIsInstance(g1,open_digraph)
	

class NodeTest(unittest.TestCase):

	def setUp(self):
		self.n0 = node(0, 'a', [], [1])
		self.n1 = node(1, 'b', [0], [])

	def test_copy(self):
		n2 = self.n0.copy()
		n2.label = 'c'
		self.assertEqual(n2.id, self.n0.id)
		self.assertNotEqual(n2.label, self.n0.label)
		self.assertIsNot(n2, self.n0)
	def test_repr(self):
		s=repr(self.n0)
		self.assertEqual(s,'node(0, a, [], [1])')
	
	def test_getters(self):
		
		self.assertEqual(0,self.n0.get_id())
		self.assertEqual('a',self.n0.get_label())
		self.assertEqual([],self.n0.get_parent_ids())
		self.assertEqual([0],self.n1.get_parent_ids())
		self.assertEqual([1],self.n0.get_children_ids())
		self.assertEqual([],self.n1.get_children_ids())
		
	def test_setters(self):
		self.n0.set_id(1)
		self.assertEqual(1,self.n0.id) 
		self.n0.set_id(0)
		self.n0.set_label('c')
		self.assertEqual('c',self.n0.label)
		self.n0.set_label('a')
		self.n0.set_parent_ids([1,2])
		self.assertEqual([1,2],self.n0.parents)
		self.n0.set_parent_ids([])
		self.n0.set_children_ids([])
		self.assertEqual([],self.n0.children)
		self.n0.set_children_ids([1])
		self.n0.add_child_id(2)
		self.assertEqual([1,2],self.n0.children)
		self.n0.set_children_ids([1])
		self.n0.add_parent_id(1)
		self.assertEqual([1],self.n0.parents)
		self.n0.set_parent_ids([])
	
	def test_remove(self):
		self.n1.remove_parent_id(0)
		self.assertEqual([],self.n1.parents)
		self.n0.remove_child_id(1)
		self.assertEqual([],self.n0.children)
		self.n0.set_children_ids([1,1,1,1,1,2,3])
		self.n1.set_parent_ids([1,1,1,1,2,3])
		self.n1.remove_parent_id_all(1)
		self.n0.remove_child_id_all(1)
		self.assertEqual([2,3],self.n1.parents)
		self.assertEqual([2,3],self.n0.children)
	def test_degree(self):
		self.assertEqual(0,self.n0.indegree())
		self.assertEqual(1,self.n1.indegree())
		self.assertEqual(1,self.n0.outdegree())
		self.assertEqual(0,self.n1.outdegree())
		self.assertEqual(1,self.n1.degree())

class DigraphTest(unittest.TestCase):

	def setUp(self):
			self.odg1= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3], [6]),node(0, 'b', [1], [7,5])])
			self.odg2= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3,0], [6]),node(0, 'b', [1], [7,5,4])])
			self.odg3= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [3,0], [6]),node(0, 'b', [1], [7,5,4])])
			self.odg4= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3,0,0], [6]),node(0, 'b', [1], [7,5,4])])
			self.odg5= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3,0,0], [6]),node(0, 'b', [1], [7,5,4,4])])
			self.odg6= open_digraph([1,2,3],[5,6,7],[node(4, 'a', [2,3,0,0], [6,0]),node(0, 'b', [1,4], [7,5,4,4])])
	def test_copy(self):
		pass

		
		
		
	def test_repr(self):
		pass
	def test_empty(self):
		pass
	
	def test_getters(self):
		
		self.assertEqual([1,2,3],self.odg1.get_input_ids())
		self.assertEqual([5,6,7],self.odg1.get_output_ids())
		self.assertEqual(self.odg1.nodes,self.odg1.get_id_node_map())
		self.assertEqual([self.odg1.nodes[4],self.odg1.nodes[0]],self.odg1.get_nodes())
		self.assertEqual(list(self.odg1.nodes.keys()),self.odg1.get_node_ids())
		self.assertEqual(self.odg1.nodes[4], self.odg1.get_node_by_id(4))
		self.assertEqual([self.odg1.nodes[4],self.odg1.nodes[0]],self.odg1.get_nodes_by_ids([4,0]))
	
	def test_setters(self):
		self.odg1.set_input_ids([3,4])
		self.assertEqual([3,4],self.odg1.inputs)
		self.odg1.set_input_ids([1,2,3])
		self.odg1.set_output_ids([1,2])
		self.assertEqual([1,2],self.odg1.outputs)
		self.odg1.add_output_id(3)
		self.assertEqual([1,2,3],self.odg1.outputs)
		self.odg1.set_output_ids([5,6,7])
		self.odg1.add_input_id(5)
		self.assertEqual([1,2,3,5],self.odg1.inputs)
		self.odg1.set_input_ids([1,2,3])
	
	def test_new_id (self):
		self.assertEqual(self.odg1.new_id(),0)
	
	
	def test_add_edge(self):
		self.odg1.add_edge(4,0)
		n1= self.odg1.get_node_by_id(4)
		self.assertEqual(n1.get_children_ids(),[6,0])
		n2 = self.odg1.get_node_by_id(0)
		self.assertEqual(n2.get_parent_ids(),[1,4])
	
	def test_add_node(self):
		n0 =self.odg1.add_node('a', [4], [0])
		self.assertEqual(self.odg1.get_node_ids(),[4,0,n0])
		self.assertEqual(self.odg1.nodes[4].get_children_ids(),[6,n0])
		self.assertEqual(self.odg1.nodes[0].get_parent_ids(),[1,n0])
		
	def test_remove_edge(self):
		self.odg2.remove_edge(0,4)
		self.assertEqual(self.odg2.nodes[4].parents,[2,3])
		self.assertEqual(self.odg2.nodes[0].children,[7,5])
		
	def test_remove_node_by_id(self):
		self.odg2.remove_node_by_id(4)
		self.assertEqual(list(self.odg2.nodes.keys()),[0])
		self.assertEqual(self.odg2.nodes[0].children,[7,5])
	def test_is_well_formed(self):
		self.assertEqual(True,self.odg2.is_well_formed())
		self.assertEqual(False,self.odg3.is_well_formed())
		self.assertEqual(False,self.odg4.is_well_formed())
		self.assertEqual(True,self.odg5.is_well_formed())
		
	
	def test_degree(self):
		c=self.odg1.max_indegree()
		self.assertEqual(c,2)
		c=self.odg1.max_outdegree()
		self.assertEqual(c,2)
		self.assertEqual(1,self.odg1.min_indegree())
		self.assertEqual(1,self.odg1.min_outdegree())
		self.assertEqual(self.odg4.max_degree(),5)
		self.assertEqual(self.odg4.min_degree(),4)
		
	def test_vire_outputs(self):
		self.odg1.vire_output()
		self.assertEqual([],self.odg1.nodes[4].children)
	def test_is_cyclic(self):
		self.assertEqual(True,self.odg6.is_cyclic())
		self.assertEqual(False,self.odg3.is_cyclic())
	def test_id(self):
		self.assertEqual(self.odg1.min_id(),0)
		self.assertEqual(self.odg1.max_id(),7)
	def test_shift_indices(self):
		self.odg3.shift_indices(10)
		self.assertEqual(self.odg3.nodes[14].parents[1],10)
		self.assertEqual(self.odg3.get_node_ids(),[14,10])
	def test_maxmin(self):
		O = open_digraph([1,2,3],[5,6,7],[node(4, 'a', [3,0], [6]),node(0, 'b', [1], [7,5,4])])
		self.assertEqual(O.min_id_output(),5)
		self.assertEqual(O.max_id_inputs(),3)
		self.assertEqual(O.min_id_inputs(),1)
		self.assertEqual(O.max_id_output(),7)
	def test_maxmin_node(self):
		self.assertEqual(self.odg3.min_id_node(),0)
		self.assertEqual(self.odg4.max_id_node(),4)
		self.assertEqual(self.odg4.max_id(),7)
		self.assertEqual(self.odg4.min_id(),0)
	def test_shift_indices(self):
		self.odg3.shift_indices(3)
		self.assertEqual(self.odg3.nodes[7].label,'a')
		self.assertEqual(self.odg3.nodes[7].parents[0],6)
		
		
		

	
	
	
	
	
	
	
	
	

if __name__ == '__main__': # the following code is called only when
  unittest.main()          # precisely this file is run