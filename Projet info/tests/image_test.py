from random import *
import sys
sys.path.append('../') # allows us to fetch files from the project root
from modules.images import *
from PIL import ImageDraw,Image
import math

import unittest
from modules.open_digraph import *
from modules.utils import *

class InitTest(unittest.TestCase):
   
    def setUp(self):
        self.p=point(1,-2)
        self.p2=point(3,-4)
        self.p3 = point(1,0)
        
        
    
    def test_copy(self):
        
        p1=self.p.copy()
        self.assertEqual(1,p1.x)
        self.assertEqual(-2,p1.y)
        self.p.x=3
        self.assertEqual(p1.x,1)
        self.p.x=1
        
    def test_add(self):
        self.p+self.p2
        self.assertEqual(self.p.x,4)
        self.assertEqual(self.p.y,-6)
        
    def test_rmul(self):
        self.p.__rmul__(2)
        self.assertEqual(2,self.p.x)
        self.assertEqual(-4,self.p.y)
    '''def test_rotate(self):
        self.p.rotate(pi/2,point(0,0))
        self.assertEqual(self.x,0)'''
    def test_translate(self):
        self.assertEqual()
    


if __name__ == '__main__': # the following code is called only when
  unittest.main()          # precisely this file is run