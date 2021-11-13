# -*- coding: utf-8 -*-
"""
Created on Thu Apr 29 16:22:15 2021

@author: User
"""


##class PriorityQueue
class PriorityQueue(object):
    def __init__(self):
        self.queue = []
  
    def __str__(self):
        return ' '.join([str(i) for i in self.queue])
  
    # for checking if the queue is empty
    def isEmpty(self):
        return len(self.queue) == 0
  
    # for inserting an element to the queue
    def insert(self, data):
        self.queue.append(data)
        
#using overloading < in node class
    # for popping an element based on priority
    def delete(self):
        try:
            min = 0
            for i in range(len(self.queue)):
                if self.queue[i] < self.queue[min]:
                    min = i
            item = self.queue[min]
            del self.queue[min]
            return item
        except IndexError:
            print()
            exit()

#using overloading == in node class
    def isIn(self,node1):
            for i in range(len(self.queue)):
                if self.queue[i] == node1:
                    return True
            return False
     
#using overloading == in state class        
    def find_state(self,state):
        for i in range(len(self.queue)):
            if self.queue[i].state == state:
                return True
        return False