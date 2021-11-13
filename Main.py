# -*- coding: utf-8 -*-
"""
Created on Sun May  9 11:41:07 2021

@author: User
"""

# -*- coding: utf-8 -*-
"""
Created on Sat May  1 11:59:48 2021

@author: User
"""

# -*- coding: utf-8 -*-


  
import priority_queue
import node
import state


# create new node 
def make_node(state,parent,h,g):
    return node.Node(state,parent,h,g)

# calculate H
#using overloading operator sub in state object
def calc_h(state):
    return state-goal_state

# check if the state in board's bounderies
# check for water
def valid_state(i,j):
    if i in range(0,size) and j in range(0,size):
        if matrix_input[i][j] == 'W':
            return False
        return True
    else:
        return False
    
# returns all the neighbors of the current state. 
def SUCC(state1):
    states = []
    
    if valid_state(state1.i+1,state1.j):
        states.append(state.State((state1.i)+1,state1.j))
    if valid_state(state1.i-1,state1.j):
        states.append(state.State((state1.i)-1,state1.j))
    if valid_state(state1.i,state1.j+1):
        states.append(state.State(state1.i,(state1.j)+1))
    if valid_state(state1.i,state1.j-1):
        states.append(state.State(state1.i,(state1.j)-1))
    return states

    
def create_file(node):
    file = open("output.txt","w")
    path = ""
    if  type(node) is str:
        file.write(node)
        file.close
        return
    
    final_cost = node.f
    while (node.parent):
        path = path+node.how_did_i_get_here()
        node = node.parent
        if not node.parent:
            path = path[::-1] + "\tCost of the solution: " +str(final_cost)
            print(path)
            file.write(path)
            file.close
        path +="-"    
 

    
        
    
def calc_g1(state):
    if matrix_input[state.i][state.j] == 'D':
        return 4
    elif matrix_input[state.i][state.j] == 'R':
        return 1
    elif matrix_input[state.i][state.j] == 'W':
        return 1000000
    elif matrix_input[state.i][state.j] == 'A' or matrix_input[state.i][state.j] == 'B':
        return 0

   
# greedy best first algoritham
def greedyBestFirst():
    open_DS = priority_queue.PriorityQueue()
    close_DS = priority_queue.PriorityQueue()
    open_DS.insert(make_node(init_state,None,calc_h(init_state),0))
    while not open_DS.isEmpty():
       next_node = open_DS.delete()
       close_DS.insert(next_node)
       if next_node.state == goal_state:
           create_file(next_node)
           return
       next_states = []
       next_states = SUCC(next_node.state)
       for s in next_states:
           if not (close_DS.find_state(s)) and not(open_DS.find_state(s)):
                   new = make_node(s,next_node,calc_h(s),1+next_node.g)
                   open_DS.insert(new)
                   

def Astar():
    open_DS = priority_queue.PriorityQueue()
    close_DS = priority_queue.PriorityQueue()
    open_DS.insert(make_node(init_state,None,calc_h(init_state),0))
    while not open_DS.isEmpty():
       next_node = open_DS.delete()
       close_DS.insert(next_node)
       if next_node.state == goal_state:
           create_file(next_node)
           return
       next_states = []
       next_states = SUCC(next_node.state)
       for s in next_states:
           if not (close_DS.find_state(s)) and not(open_DS.find_state(s)):
                   new = make_node(s,next_node,calc_h(s),calc_g1(s)+next_node.g)
                   open_DS.insert(new)
    create_file("no path")



#Main
##opening the file, read the algorithm and board size
file = open("input.txt", "r")
algo = file.readline().rstrip("\n\r")
size = int(file.readline().rstrip("\n\r"));

##reading the matrix board game from the file
matrix_input = []
row =[]

while 1:
    char = file.read(1)
    if not char:
        matrix_input.append(row)
        break
    elif char == '\n':
        matrix_input.append(row)
        row=[]
    else:
      row.append(char)  

      
#finding and start position and goal position
for i in range(size):
    for j in range(size):
        if matrix_input[i][j] == 'A':
            init_state = state.State(i,j)
        elif matrix_input[i][j] == 'B':
            goal_state = state.State(i,j)




file.close()
if algo == 'A*':
    Astar()
elif algo =="greedyBestFirst":
    greedyBestFirst()
else:
    print("Worng algoritham name")

    



   