from node import Node

p_size =3
iterations =0

goal = [1,2,3,
        4,5,6,
        7,8,0]

f_example_case = [6,8,5,
                  2,7,0,
                  1,4,3]

s_example_case = [0,1,3,
                  4,2,5,
                  7,8,6]

worst_case = [8,7,6,
              5,4,3,
              2,1,0]

visited = set()
to_visit = list()
current_node = Node
goal_node = Node(goal, None)

def is_current_the_goal(node):
    return node.state == goal_node.state

def swap(t_node, a, b):
    t_node.state[a], t_node.state[b] = t_node.state[b], t_node.state[a]

def create_node(state, parent):
    return Node(state, parent)

def show_path(node):
    if(node.parent != 0):
        show_path(node.parent)
    node.reveal()

#expand the states that suppose to be visited
def move(node):
    #left
    t_node = create_node(node.state[:], node)
    z_index = t_node.z_index()
    if(z_index not in [0,3,6]):
        swap(t_node, z_index, z_index-1)
        if(tuple(t_node.state) not in visited):
            to_visit.append(t_node)
        else:
            visited.add(tuple(t_node.state))

    #up
    t_node = create_node(node.state[:], node)
    if(z_index not in [0,1,2]):
        swap(t_node, z_index, z_index-3)
        if(tuple(t_node.state) not in visited):
            to_visit.append(t_node)
        else:
            visited.add(tuple(t_node.state))

    #right
    t_node = create_node(node.state[:], node)
    if(z_index not in [2,5,8]):
        swap(t_node, z_index, z_index+1)
        if(tuple(t_node.state) not in visited):
            to_visit.append(t_node)
        else:
            visited.add(tuple(t_node.state))

    #down
    t_node = create_node(node.state[:], node)
    if(z_index not in [6,7,8]):
        swap(t_node, z_index, z_index+3)
        if(tuple(t_node.state) not in visited):
            to_visit.append(t_node)
        else:
            visited.add(tuple(t_node.state))


def bfs(initial_state):
    global iterations, p_size, goal_node
    initial_node = Node(initial_state, 0)

    #initialize the list of nodes to visit
    to_visit.insert(0, initial_node)

    while to_visit:
        current_node = to_visit.pop(0)
        if(is_current_the_goal(current_node)):
            show_path(current_node)
            print(iterations)
            return
        elif tuple(current_node.state) not in visited:
            move(current_node)
            visited.add(tuple(current_node.state))
            iterations += 1

bfs(worst_case)
