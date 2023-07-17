class Graph:
    def __init__(self, adjact_list):
        self.adjact_list = adjact_list
 
    def get_neighbors(self, v):
        return self.adjact_list[v]
 
    # This is heuristic function which is having equal values for all nodes
    def h(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1,
            'F': 1
        }
 
        return H[n]
 
    def a_star_algorithm(self, start, stop):
        # In this open_lst is a lisy of nodes which have been visited, but who's 
        # neighbours haven't all been always inspected, It starts off with the start 
  #node
        # And closed_lst is a list of nodes which have been visited
        # and who's neighbors have been always inspected
        open_lst = set([start])
        closed_lst = set([])
 
        # present_nodeDistance has present distances from start to all other nodes
        # the default value is +infinity
        present_nodeDistance = {}
        present_nodeDistance[start] = 0
 
        # adjac_mapping contains an adjac mapping of all nodes
        adjac_mapping = {}
        adjac_mapping[start] = start
 
        while len(open_lst) > 0:
            n = None
 
            # it will find a node with the lowest value of f() -
            for v in open_lst:
                if n == None or present_nodeDistance[v] + self.h(v) < present_nodeDistance[n] + self.h(n):
                    n = v
 
            if n == None:
                print('Path doesnot exist!')
                return None
 
            # if the current node is the stop
            # then we start again from start
            if n == stop:
                reconst_path = []
 
                while adjac_mapping[n] != n:
                    reconst_path.append(n)
                    n = adjac_mapping[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            # for all the neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
              # if the current node is not presentin both open_lst and closed_lst
                # add it to open_lst and note n as it's adjac_mapping
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    adjac_mapping[m] = n
                    present_nodeDistance[m] = present_nodeDistance[n] + weight
 
                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update adjac_mapping data and present_nodeDistance data
                # and if the node was in the closed_lst, move it to open_lst
                else:
                    if present_nodeDistance[m] > present_nodeDistance[n] + weight:
                        present_nodeDistance[m] = present_nodeDistance[n] + weight
                        adjac_mapping[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            # remove n from the open_lst, and add it to closed_lst
            # because all of his neighbors were inspected
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return None
    
adjact_list = {
    'A': [('B', 1), ('C', 3), ('D', 7)],
    'B': [('A',1), ('D', 5), ('E', 2)],
    'C': [('A', 3), ('D', 12)],
    'D': [('A', 7), ('B', 5), ('C', 12), ('E', 1), ('F', 10)],
    'E': [('B', 2), ('D', 1), ('F', 6)],
    'F': [('D', 10), ('E', 6)]
}
graph1 = Graph(adjact_list)
graph1.a_star_algorithm('A', 'F')