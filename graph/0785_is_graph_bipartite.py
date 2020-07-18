from collections import deque
from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # bfs search
        if not graph:
            return False

        n = len(graph)
        # store which subset it belongs: 0 -> unassigned; 1, 2 -> subsets
        dict_node = [0 for _ in range(n)]

        # nodes need to visit
        queue = deque()

        for i in range(n):
            # if not visited
            if dict_node[i] == 0:
                queue.append(i)
                while queue:
                    node = queue.pop()
                    # exclude single node
                    if not graph[node]:
                        dict_node[node] = 3
                        continue

                    # check the connections' subset
                    for item in graph[node]:
                        if dict_node[item] == 0:
                            queue.append(item)
                            dict_node[item] = (2 if dict_node[node] == 1 else 1)
                        elif dict_node[item] == dict_node[node]:
                            return False
                        else:
                            continue

        return True
