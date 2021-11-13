# -*- coding: utf-8 -*-
"""
Created on Sat May  1 18:23:55 2021

@author: User
"""

class State(object):
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
        
    def __eq__(self,other):
        if (str(self.i) == str(other.i) and str(self.j) == str(other.j)):
            return True
        return False
    
    def __str__(self):
        return "I index:" +str(self.i)+" " +"J index:"+str(self.j)
    
    def __sub__(self,other):
        return (abs(self.i - other.i) + abs(self.j - other.j))
    
