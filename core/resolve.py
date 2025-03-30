import networkx as nx

def resolve_deadlock(graph):
    try:
        # Detect cycles (deadlock)
        cycles = list(nx.simple_cycles(graph))
        if not cycles:
            return "No deadlock detected."

        print(f"Deadlock Detected: {cycles}")

        # Choose a process to terminate
        for cycle in cycles:
            process_to_terminate = cycle[0]
            print(f"Terminating Process: {process_to_terminate}")
            
            # Remove the process from the graph
            graph.remove_node(process_to_terminate)

            print(f"Process {process_to_terminate} terminated to break deadlock.")
            break

        # Recheck for deadlock
        cycles_after = list(nx.simple_cycles(graph))
        if cycles_after:
            return "Deadlock still exists. Reattempting..."
        else:
            return "Deadlock resolved successfully."
    except Exception as e:
        return f"Error: {e}"
