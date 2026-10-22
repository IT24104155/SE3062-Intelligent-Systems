"""SE3062 Practical 08 - Game Theory and Adversarial Search."""
import math

class Node:
    def __init__(self, name, value=None):
        self.name, self.value, self.children = name, value, []
    def is_terminal(self):
        return not self.children

nodes_evaluated=0
def reset_counter():
    global nodes_evaluated
    nodes_evaluated=0
def increment_counter():
    global nodes_evaluated
    nodes_evaluated+=1

def minimax(node, maximizing):
    increment_counter()
    if node.is_terminal(): return node.value
    values=(minimax(child,not maximizing) for child in node.children)
    return max(values) if maximizing else min(values)

def alphabeta(node, alpha, beta, maximizing):
    increment_counter()
    if node.is_terminal(): return node.value
    if maximizing:
        best=-math.inf
        for child in node.children:
            best=max(best,alphabeta(child,alpha,beta,False))
            alpha=max(alpha,best)
            if alpha>=beta: break
        return best
    best=math.inf
    for child in node.children:
        best=min(best,alphabeta(child,alpha,beta,True))
        beta=min(beta,best)
        if alpha>=beta: break
    return best

def expectimax(node,maximizing):
    increment_counter()
    if node.is_terminal(): return node.value
    scores=[expectimax(child,not maximizing) for child in node.children]
    return max(scores) if maximizing else sum(scores)/len(scores)

def calculate_offer(t,t_max,beta,min_price,max_price,is_seller):
    time_factor=(t/t_max)**beta
    if is_seller: return min_price+(max_price-min_price)*(1-time_factor)
    return min_price+(max_price-min_price)*time_factor

def simulate_negotiation(seller_beta,buyer_beta):
    for t in range(1,21):
        seller=calculate_offer(t,20,seller_beta,600,1000,True)
        buyer=calculate_offer(t,20,buyer_beta,500,900,False)
        if buyer>=seller:
            return t,(seller+buyer)/2
    return None

def make_tree():
    root=Node('Root')
    for name, values in [('M1',[3,12,8]),('M2',[2,4,6]),('M3',[14,5,2])]:
        branch=Node(name)
        branch.children=[Node(f'{name}_L{i}',v) for i,v in enumerate(values,1)]
        root.children.append(branch)
    return root

if __name__=='__main__':
    tree=make_tree()
    reset_counter(); assert minimax(tree,True)==3 and nodes_evaluated==13
    reset_counter(); assert alphabeta(tree,-math.inf,math.inf,True)==3 and nodes_evaluated==11
    reset_counter(); assert round(expectimax(tree,True),2)==7.67
    print('Minimax: 3 (13 nodes); Alpha-Beta: 3 (11 nodes); Expectimax: 7.67')
    print('Boulware/Boulware:',simulate_negotiation(5,5))
    print('Boulware/Conceder:',simulate_negotiation(5,0.2))
