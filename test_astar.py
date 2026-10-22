from agent import SearchAgent

def test_heuristics():
    agent = SearchAgent()
    assert agent.manhattan_distance((0,0),(3,4)) == 7
    assert agent.euclidean_distance((0,0),(3,4)) == 5.0

def test_search():
    agent = SearchAgent()
    path = agent.astar_search((0,0),(3,0),{(1,0)},(5,5))
    assert path is not None and len(path) == 5
    assert (1,0) not in path and path[-1] == (3,0)
    assert agent.astar_search((0,0),(0,0),set(),(3,3)) == []
    assert agent.astar_search((0,0),(2,2),{(0,1),(1,0)},(3,3)) is None

if __name__ == '__main__':
    test_heuristics()
    test_search()
    print('All Week 04 A* tests passed.')
