# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=[]):
        self.val = val
        self.neighbors = neighbors


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        visited = {}

        def dfs(curr_node):
            if not curr_node:
                return

            # For deep clone purpose, only clone the value but neighbors
            cloned = Node(curr_node.val, [])

            # return visited neighbors if already visited
            if curr_node in visited:
                return visited[curr_node]

            # store in hashtable
            visited[curr_node] = cloned

            # iterate through current node and update the hashtable
            for item in curr_node.neighbors:
                cloned.neighbors.append(dfs(item))

            return cloned

        return dfs(node)
