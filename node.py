# -*- coding: utf-8 -*-
"""
Created on Sat May  1 15:30:25 2021

@author: User
"""


class Node(object):
        
        g = 0
                  
        def __init__(self,state,parent,h,g):
            self.state = state
            self.parent = parent
            self.h = int(h)
            self.g = int(g)
            self.f = int(g)+int(h)
        
      
        def __lt__(self,other):
            if (self.f < other.f):
                return True
            return False
      
        def __str__(self):
            return "State:"+str(self.state)+" Parent1:   "" H:" + str(self.h)
        
        def __eq__(self,other):
            if self.state.i == other.state.i and self.state.j == other.state.j:
                return True
            return False
        
        def how_did_i_get_here(self):
            if not self.parent:
                return
            if (self.state.i == self.parent.state.i):
                if int(self.state.j) > int(self.parent.state.j):
                    return 'R'
                else:
                    return 'L'
            else:
                if int(self.state.i) > int(self.parent.state.i):
                    return 'D'
                else:
                    return 'U'
