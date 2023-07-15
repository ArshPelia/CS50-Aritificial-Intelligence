""" 
Nodes contain information that makes them very useful for the purposes of search algorithms. 

They contain a state, which can be checked using the goal test to see if it is the final state.

If it is, the node’s path cost can be compared to other nodes’ path costs, which allows 
    choosing the optimal solution. 

Once the node is chosen, by virtue of storing the parent node and the action that led 
    from the parent to the current node, it is possible to trace back every step of the way 
    from the initial state to this node, and this sequence of actions is the solution.
 """

class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action


class StackFrontier():
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    # Define the function that removes a node from the frontier and returns it.
    def remove(self):
    	  # Terminate the search if the frontier is empty, because 
          # this means that there is no solution.
        if self.empty():
            raise Exception("empty frontier")
        else:
        	  # Save the last item in the list (which is the newest node added)
            node = self.frontier[-1]
            # Save all the items on the list besides the last node (i.e. removing the last node)
            self.frontier = self.frontier[:-1]
            return node


class QueueFrontier(StackFrontier):
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0
    
    # Define the function that removes a node from the frontier and returns it.
    def remove(self):
    	  # Terminate the search if the frontier is empty, because this means that there is no solution.
        if self.empty():
            raise Exception("empty frontier")
        else:
            # Save the oldest item on the list (which was the first one to be added)
            node = self.frontier[0]
            # Save all the items on the list besides the first one (i.e. removing the first node)
            # self.frontier = self.frontier[1:]
            node = self.frontier.pop(0)  #remove the first item (queue behavior)
            return node
        