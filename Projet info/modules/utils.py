
from random import *
import sys
sys.path.append('../') # allows us to fetch files from the project root

def remove_all(l, x):
    ''' input int list, int  output: int list'''
    l1= []
    for k in range(len (l)):
        if l[k] != x:
            l1= l1+[l[k]]
    return l1
    


def remove_one(l,x):
    '''input int list, int: x= int to be removed from l output: int list'''
    l1=[]
    c=0
    for k in range(len(l)):
        if l[k]!=x or c!=0:
            l1 = l1+[l[k]]
        if l[k]==x:
            c=c+1
    return l1
    
def count_occurrences(l,x):
    '''input int list, int output: int'''
    c = 0
    for k in range(len(l)):
        if l[k]==x:
            c=c+1
    return c

def remove_list(l,l2):
    '''input int list int list;  output: list'''
    l0=l
    for k in l2:
        l0= remove_all(l0,k)
    return l0
    
def random_int_list(n,bound):
    l=[]
    for k in range(n):
        l= l+[randint(0,bound)]
    return l
def max_liste(l):
    c = l[0]
    for k in l:
        if k>c:
            c=k
    return c
def random_int_matrix(n,bound,null_diag = True):
    l=[]
    if null_diag == True:
        for i in range(n):
            l = l+[[]]
            for j in range(n):
                if i == j:
                    l[i] = l[i] +[0]
                else: 
                    l[i] = l[i] +[randint(0,bound)]
    
    if null_diag== False:
        for k in range(n):
            l = l +[random_int_list(n,bound)]
    
    return l
def random_symetric_int_matrix(n,bound,null_diag=True):
    l = random_int_matrix(n,bound,null_diag)
    if null_diag == True:
        l = random_int_matrix(n,bound,null_diag)
        for i in range(n):
            for j in range(i,n):
                l[j][i]= l[i][j]
    else:
        l = random_int_matrix(n,bound,False)
        for i in range(n):
            for j in range(i,n):
                l[j][i]= l[i][j]
    return l
    
def random_triangular_int_matrix(n,bound,null_diag=True):
    l = []
    for i in range(n):
        l = l+[[]]
        for j in range(n):
            if null_diag == True:
                if i>=j:
                    l[i] = l[i]+[0]
                else:
                    l[i]= l[i]+[randint(0,bound)]
            else:
                if i>j:
                    l[i] = l[i]+[0]
                else:
                    l[i]= l[i]+[randint(0,bound)]
    return l
    

def max_matrix(m):#utilisee pour test
    c=m[0][0]
    for i in range(len(m)):
        for j in range(len(m)):
            if m[i][j]>c:
                c = m[i][j]
    return c


def random_oriented_int_matrix(n,bound,null_diag=True):
    if null_diag == True:
        l = random_int_matrix(n,bound,null_diag)
        for i in range(n):
            for j in range(n):
                c = randint(1,2)
                if l[i][j]!=0 and l[j][i]!=0:
                    if c == 1:
                        l[i][j]=0
                    else: 
                        l[j][i]=0
    if null_diag==False:
        l = random_int_matrix(n,bound,False)
        for i in range(n):
            for j in range(n):
                c = randint(1,2)
                if l[i][j]!=0 and i!=j and l[j][i]!=0:
                    if c == 1:
                        l[i][j]=0
                    else:
                        l[j][i]=0
        
    
    return l
    
def ming(d):
    a=0
    for k in d:
        a=k
        break
    for k in d:
        if d[k]<d[a]:
            a=k
    return a


def invPerm(l):
    l2= [0]*len(l)
    for k in range(len(l2)):
        for j in range(len(l)):
            if(l[j]==k):
                l2[k]=j
    return l2

def reverse(l):
    l2 = []
    for k in l:
        l2 = [k]+l2
        
   
    return l2
    
def maxg(d):
    a=0
    for k in d:
        a=k
        break
    for k in d:
        if d[k]>d[a]:
            a=k
    return a


def enleveDoublon(l):
    if(len(l)==0):
        return l
    l=tri_liste(l)

    nvL = [l[0]]

    for k in range(1,len(l)):
        if l[k]!=l[k-1]:
            nvL+=[l[k]]
               
        d=l[k]
    return nvL
    

def tri_liste(l):
    if l == []:
        return l
    else:
        c = l[0]
        l1 = []
        l2 = []
    for k in l[1:]:
        if k<c:
            l1=l1+[k]
        else:
            l2 = l2 + [k]
    return tri_liste(l1)+[c]+tri_liste(l2)
    
    
      