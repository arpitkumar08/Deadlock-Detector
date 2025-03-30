import networkx as nx

class DeadlockDetector:
    def __init__(self):
        self.graph = nx.DiGraph()

    def add_dependency(self, process1, process2):
        """Adds a dependency between two processes."""
        self.graph.add_edge(process1, process2)

    def detect_deadlock(self):
        """Detects deadlocks using cycle detection."""
        try:
            cycle = nx.find_cycle(self.graph, orientation="original")
            return cycle
        except nx.NetworkXNoCycle:
            return None
