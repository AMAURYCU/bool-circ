import sys
sys.path.append('../') # allows us to fetch files from the project root

import unittest
from modules.bool_circ import *
from modules.utils import *






class Bool_circ_test(unittest.TestCase):
    def test_init_bool_circ(self):
        odg2 = open_digraph([1],[6],[node(4, '&', [], [6]),node(0, '', [1], [6])])
        b=bool_circ(odg2)
        self.assertEqual(b.is_well_formed(),True)
        self.assertIsInstance(b,bool_circ)

    def setUp(self):
        self.odg1=open_digraph([],[],[])
        self.odg2 = open_digraph([1],[6],[node(4, '&', [], [6]),node(0, '', [1], [6])])
        #self.odg3 = open_digraph([1],[6],[node(4, '&', [0], [6,0]),node(0, '', [1,4], [6,4])])
        self.bc1= bool_circ(self.odg1)
        self.bc2= bool_circ(self.odg2)
        #self.bc3= bool_circ(self.odg3)
    def test_to_graph(self):
        self.assertIsInstance(self.bc1.to_graph(),open_digraph)
    def test__formed(self):
        self.assertEqual(self.bc1.is_well_formed(),True)
        self.assertEqual(self.bc2.is_well_formed(),True)
        #self.assertEqual(False,self.bc3.is_well_formed())
        #avec la nouvelle version de init on ne peu parler que de bool_circ bien formés
    def test_parse_parentheses(self):
        odg2 = open_digraph([1],[6],[node(4, '&', [], [6]),node(0, '', [1], [6])])
        b=bool_circ(odg2)
        b.parse_parentheses("((x0)&((x1)&(x2)))|((x1)&(~(x2)))")
        self.assertEqual(b.nodes[0].label,'|')
    
    
if __name__ == '__main__': # the following code is called only when
  unittest.main()          # precisely this file is run