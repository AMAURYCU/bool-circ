import sys
sys.path.append('../')
import unittest

from modules.utils import *


class utilTests (unittest.TestCase):
    def setUp(self):
        self.l0=[1,2,3,4,5,5,4,3,5]
    
    def test_remove_all(self):
        self.assertEqual([1,2,3,4,4,3],remove_all(self.l0,5))
        self.assertEqual([1,2,3,4,5,5,4,3,5],remove_all(self.l0,7))
    
    def test_remove_one(self):
        self.assertEqual([1,2,3,4,5,4,3,5],remove_one(self.l0,5))
    def test_count_occurrences(self):
        self.assertEqual(3, count_occurrences(self.l0,5))
    def test_random_int_list(self):
        l1= random_int_list(4,9)
        self.assertEqual(len(l1),4)
        self.assertEqual(max(l1)<=9,True)
    def test_random_int_matrix(self):
        m = random_int_matrix(4,10)
        self.assertEqual(4,len(m))
        self.assertEquals(4,len(m[0]),len(m[1]))
        self.assertEquals(4,len(m[2]),len(m[3]))
        self.assertEqual(max_matrix(m)<=10,True)
        for k in range(4):
            for i in range(4):
                if k == i:
                    self.assertEqual(0,m[k][i])
    def test_random_symetric_int_matrix(self):
        m = random_symetric_int_matrix(4,10)
        self.assertEqual(4,len(m))
        self.assertEquals(4,len(m[0]),len(m[1]))
        self.assertEquals(4,len(m[2]),len(m[3]))
        self.assertEqual(max_matrix(m)<=10,True)
        for k in range(4):
            for i in range(4):
                self.assertEqual(m[k][i],m[i][k])
                if k == i:
                    self.assertEqual(0,m[k][i])
    def test_random_triangular_int_matrix(self):
        m = random_triangular_int_matrix(4,10)
        self.assertEqual(4,len(m))
        self.assertEquals(4,len(m[0]),len(m[1]))
        self.assertEquals(4,len(m[2]),len(m[3]))
        self.assertEqual(max_matrix(m)<=10,True)
        for k in range(4):
            for i in range(4):
                if k>=i:
                  self.assertEqual(m[k][i],0)
    
    def test_random_oriented_int_matrix(self):
        m = random_oriented_int_matrix(4,10)
        self.assertEqual(4,len(m))
        self.assertEquals(4,len(m[0]),len(m[1]))
        self.assertEquals(4,len(m[2]),len(m[3]))
        self.assertEqual(max_matrix(m)<=10,True)
        for k in range(4):
            for i in range(4):
                if k == i:
                    self.assertEqual(0,m[k][i])
                else:
                    if m[k][i]!=0:
                        self.assertEqual(m[i][k]==0,True)
    
        
        
        
        
        
        
        
        
        
        
    

if __name__ == '__main__': # the following code is called only when
  unittest.main()          # precisely this file is run