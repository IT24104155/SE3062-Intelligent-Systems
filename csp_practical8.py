"""SE3062 Practical 8: CSP algorithms for map coloring and N-Queens."""
from collections import deque
import copy

class CSP:
    def __init__(self, variables, domains, neighbors, constraints):
        self.variables=list(variables)
        self.domains={v:list(domains[v]) for v in variables}
        self.neighbors=neighbors
        self.constraints=constraints
        self.assignments_count=0
        self.backtracks_count=0
    def is_complete(self, assignment):
        return len(assignment)==len(self.variables)
    def is_consistent(self, var, value, assignment):
        return all(self.constraints(var,value,n,assignment[n]) for n in self.neighbors[var] if n in assignment)

def backtrack_naive(csp, assignment=None):
    if assignment is None: assignment={}
    if csp.is_complete(assignment): return assignment.copy()
    var=next(v for v in csp.variables if v not in assignment)
    for value in csp.domains[var]:
        if csp.is_consistent(var,value,assignment):
            assignment[var]=value; csp.assignments_count+=1
            result=backtrack_naive(csp,assignment)
            if result is not None: return result
            del assignment[var]; csp.backtracks_count+=1
    return None

def select_variable_mrv_degree(csp, assignment):
    remaining=[v for v in csp.variables if v not in assignment]
    return min(remaining,key=lambda v: (
        sum(csp.is_consistent(v,value,assignment) for value in csp.domains[v]),
        -sum(n not in assignment for n in csp.neighbors[v])
    ))

def order_domain_values_lcv(csp, var, assignment):
    valid=[value for value in csp.domains[var] if csp.is_consistent(var,value,assignment)]
    def ruled_out(value):
        return sum(
            not csp.constraints(var,value,n,other)
            for n in csp.neighbors[var] if n not in assignment
            for other in csp.domains[n]
            if csp.is_consistent(n,other,assignment)
        )
    return sorted(valid,key=ruled_out)

def backtrack_heuristics(csp, assignment=None):
    if assignment is None: assignment={}
    if csp.is_complete(assignment): return assignment.copy()
    var=select_variable_mrv_degree(csp,assignment)
    for value in order_domain_values_lcv(csp,var,assignment):
        assignment[var]=value; csp.assignments_count+=1
        result=backtrack_heuristics(csp,assignment)
        if result is not None: return result
        del assignment[var]; csp.backtracks_count+=1
    return None

def forward_check(csp, var, value, assignment, domains):
    pruned={v:list(vals) for v,vals in domains.items()}
    pruned[var]=[value]
    for n in csp.neighbors[var]:
        if n not in assignment:
            pruned[n]=[other for other in pruned[n] if csp.constraints(n,other,var,value)]
            if not pruned[n]: return pruned,False
    return pruned,True

def ac3(csp,queue=None,domains=None):
    domains={v:list(vals) for v,vals in (csp.domains if domains is None else domains).items()}
    if queue is None: queue=[(v,n) for v in csp.variables for n in csp.neighbors[v]]
    queue=deque(queue)
    while queue:
        xi,xj=queue.popleft()
        revised=False
        for x in domains[xi][:]:
            if not any(csp.constraints(xi,x,xj,y) for y in domains[xj]):
                domains[xi].remove(x); revised=True
        if revised:
            if not domains[xi]: return domains,False
            for xk in csp.neighbors[xi]:
                if xk!=xj: queue.append((xk,xi))
    return domains,True

def backtrack_mac(csp,assignment=None,domains=None):
    if assignment is None: assignment={}
    if domains is None: domains={v:list(vals) for v,vals in csp.domains.items()}
    if csp.is_complete(assignment): return assignment.copy()
    var=min((v for v in csp.variables if v not in assignment),key=lambda v:len(domains[v]))
    for value in domains[var]:
        if csp.is_consistent(var,value,assignment):
            next_assignment={**assignment,var:value}; csp.assignments_count+=1
            narrowed={v:list(vals) for v,vals in domains.items()}
            narrowed[var]=[value]
            queue=[(n,var) for n in csp.neighbors[var] if n not in next_assignment]
            narrowed,ok=ac3(csp,queue,narrowed)
            if ok:
                result=backtrack_mac(csp,next_assignment,narrowed)
                if result is not None:return result
            csp.backtracks_count+=1
    return None

def n_queens(n=8):
    variables=[f"Q{i}" for i in range(n)]
    domains={v:list(range(n)) for v in variables}
    neighbors={v:[u for u in variables if u!=v] for v in variables}
    def constraint(var1,val1,var2,val2):
        return val1!=val2 and abs(val1-val2)!=abs(int(var1[1:])-int(var2[1:]))
    return CSP(variables,domains,neighbors,constraint)

if __name__=="__main__":
    for name,solver in (
        ("Naive Backtracking",backtrack_naive),
        ("MRV + Degree + LCV",backtrack_heuristics),
        ("MAC",backtrack_mac)
    ):
        problem=n_queens(8)
        solution=solver(problem)
        assert solution and len(solution)==8
        print(name,problem.assignments_count,problem.backtracks_count)
