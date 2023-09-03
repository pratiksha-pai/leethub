"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        
        if not node:
            return None
        
        # mp from the current nodes to the new_nodes so you can link neighbors later
        mp = {}
        visited = []
        link_visited = []
        # explore to create new nodes, populate a map to link from the old to new nodes
        def explore(node):
            if not node:
                return 
            
            if node not in mp:
                new_node = Node(node.val)
                mp[node] = new_node
                visited.append(node)
                
            for neigh in node.neighbors:
                if neigh not in visited:
                    explore(neigh)
        
        # link the new nodes to the neighbors 
        def link(node):
            if not node:
                return 
            link_visited.append(node)
            for neigh in node.neighbors:
                if mp[neigh] not in mp[node].neighbors:
                    mp[node].neighbors.append(mp[neigh])
            for neigh in node.neighbors:
                if neigh not in link_visited:
                    link(neigh)

        explore(node)
        link(node)
        return mp[node]
