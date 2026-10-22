"""IT3012 Practical 04: A* informed search. Standalone SearchAgent."""
import math
import heapq
from itertools import count

class SearchAgent:
    def manhattan_distance(self, pos, goal):
        return abs(pos[0]-goal[0])+abs(pos[1]-goal[1])

    def euclidean_distance(self, pos, goal):
        return math.sqrt((pos[0]-goal[0])**2+(pos[1]-goal[1])**2)

    def astar_search(self, start_pos, goal_pos, walls, grid_size, heuristic_type='manhattan'):
        """Return cell positions from after start to goal; None if unreachable."""
        if heuristic_type not in ('manhattan', 'euclidean'):
            raise ValueError('Unknown heuristic type')
        h = self.manhattan_distance if heuristic_type=='manhattan' else self.euclidean_distance
        w, height = grid_size
        walls = set(walls)
        def valid(p):
            return 0 <= p[0] < w and 0 <= p[1] < height and p not in walls
        if not valid(start_pos) or not valid(goal_pos):
            return None
        frontier, seq = [], count()
        heapq.heappush(frontier, (h(start_pos,goal_pos),0,next(seq),start_pos))
        best_g = {start_pos: 0}
        parent = {}
        closed = set()
        while frontier:
            _, g, _, node = heapq.heappop(frontier)
            if g != best_g.get(node) or node in closed:
                continue
            if node == goal_pos:
                result = []
                while node != start_pos:
                    result.append(node)
                    node = parent[node]
                return result[::-1]
            closed.add(node)
            x,y = node
            for nxt in ((x,y-1),(x,y+1),(x-1,y),(x+1,y)):
                if not valid(nxt) or nxt in closed:
                    continue
                new_g = g+1
                if new_g < best_g.get(nxt,float('inf')):
                    best_g[nxt] = new_g
                    parent[nxt] = node
                    heapq.heappush(frontier,(new_g+h(nxt,goal_pos),new_g,next(seq),nxt))
        return None

    def plan_for_nearest_food(self, position, remaining_food, walls, grid_size):
        """Helper; adapt to the original visual game's percept/action format."""
        if not remaining_food:
            return []
        target = min(remaining_food,key=lambda item:self.manhattan_distance(position,item))
        return self.astar_search(position,target,walls,grid_size)
