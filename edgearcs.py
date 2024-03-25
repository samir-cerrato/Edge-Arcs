def process_digraph(sequence_number):
    n = int(input().strip()) 
    if n == 0:
        return None, None  
    
    encountered_arcs = set()
    arcs = 0  
    edges = 0 

    for from_vertex in range(n):
        adj_list = list(map(int, input().strip().split()))  
        arcs += len(adj_list) 
        edges += sum(1 for to_vertex in adj_list if (from_vertex, to_vertex) in encountered_arcs)  # Count valid edges (bi-directed connections)
        encountered_arcs |= {(to_vertex, from_vertex) for to_vertex in adj_list}
    return arcs, edges


def main():
    counter = 1  

    while True:
        arcs, edges = process_digraph(counter)
        if arcs is None:
            break
        print(f"Digraph {counter}: {arcs - 2 * edges} {edges}")
        counter += 1 

if __name__ == "__main__":
    main()

