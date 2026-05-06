import heapq
from collections import deque
 

def program3():
    print("\n" + "=" * 60)
    print("PROGRAM 3 — AO* Algorithm on AND-OR Graph")
    print("=" * 60)
 
    h = {'A': None, 'B': 5, 'C': 3, 'D': 4, 'E': 7, 'F': 9}
    terminals = {'C', 'D', 'E', 'F'}
 
    connectors = {
        'A': [
            ('OR',  ['B'],    1),
            ('AND', ['C','D'], 1),
        ],
        'B': [
            ('AND', ['E','F'], 1),
        ]
    }
 
    def connector_cost(node, children, edge_cost):
        return sum(edge_cost + h[c] for c in children)
 
    def ao_star(node, indent=0):
        pad = "  " * indent
        if node in terminals:
            h[node] = 0
            print(f"{pad}Terminal node {node}: h=0")
            return [node]
 
        options = connectors.get(node, [])
        print(f"\n{pad}Expanding node: {node}")
 
        costs = []
        for ctype, children, ecost in options:
            c = connector_cost(node, children, ecost)
            print(f"{pad}  {ctype} via {children} = {c}")
            costs.append((c, ctype, children, ecost))
 
        costs.sort(key=lambda x: x[0])
        best_cost, best_type, best_children, best_ecost = costs[0]
 
        print(f"{pad}  --> Picking {best_type} via {best_children} (cost={best_cost})")
 
        solution = [node]
        child_solutions = []
        for child in best_children:
            sub = ao_star(child, indent + 1)
            child_solutions.extend(sub)
 
        actual_cost = sum(best_ecost + h[c] for c in best_children)
        h[node] = actual_cost
        print(f"{pad}Revised h({node}) = {actual_cost}")
 
        if len(best_children) > 1:
            solution.append(tuple(best_children))
        else:
            solution.extend(best_children)
 
        solution.extend(child_solutions)
        return solution
 
    result = ao_star('A')
    print(f"\nSolution sub-graph: A -> ({', '.join(connectors['A'][0][1] if h['B'] < h['C']+h['D'] else connectors['A'][1][1])})")
    print(f"Final h(A) = {h['A']}")
 
 
if __name__ == "__main__":
    program3()