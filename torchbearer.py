"""
CS 460 – Algorithms: Final Programming Assignment
The Torchbearer

Student Name: Nathan Bomar
Student ID:   129901002

INSTRUCTIONS
------------
- Implement every function marked TODO.
- Do not change any function signature.
- Do not remove or rename required functions.
- You may add helper functions.
- Variable names in your code must match what you define in README Part 5a.
- The pruning safety comment inside _explore() is graded. Do not skip it.

Submit this file as: torchbearer.py
"""

import heapq


# =============================================================================
# PART 1
# =============================================================================

INFINITY = float('inf')

def explain_problem():
    """
    Returns
    -------
    str
        Your Part 1 README answers, written as a string.
        Must match what you wrote in README Part 1.

    TODO
    """
    return "The shortest path from S to T alone will likely not hit every relic room. " \
    "The inclusion of the relic rooms, and the fact that cheaper paths between them may not consist of only relics, " \
    "makes a shortest-path run insufficient. The path taken between all relic rooms and to the exit remains to be decided. " \
    "Because a simple shortest path is insufficient, we must take a best-so-far approach over the different valid " \
    "paths that meet the criteria above."


# =============================================================================
# PART 2
# =============================================================================

def select_sources(spawn, relics, exit_node):
    """
    Parameters
    ----------
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    list[node]
        No duplicates. Order does not matter.

    TODO
    """
    sources = relics
    if spawn not in sources:
        sources.append(spawn)
    if exit_node in sources:
        sources.remove(exit_node)
    return sources


def run_dijkstra(graph, source):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
        graph[u] = [(v, cost), ...]. All costs are nonnegative integers.
    source : node

    Returns
    -------
    dict[node, float]
        Minimum cost from source to every node in graph.
        Unreachable nodes map to float('inf').

    TODO
    """
    visited = [source]
    heap = [(pair[1], pair[0]) for pair in graph[source]] #create a list of value, key tuples to sort by from source node
    heapq.heapify(heap)
    costs = {item: INFINITY for item in list(graph)} #Load initial weights as infinite
    costs[source] = 0 #Cost to get to self is 0
    # print(f"At initialization, we have heap: {heap}, with costs: {costs}")
    while len(visited) < len(costs) and len(heap) > 0: #Loop should only end if all nodes are visited or if nothing is to be visited
        current_node = heap[0][1]
        current_cost = heap[0][0]
        # print(f"visited: {visited} \ncurrent_node: {current_node}")
        if current_node in visited:
            heap.pop(0)
            continue
        costs[current_node] = current_cost
        visited.append(current_node)
        heap.pop(0)
        new_found_edges = [(pair[1] + current_cost, pair[0]) for pair in graph[current_node]]
        heap = heap + new_found_edges
        heapq.heapify(heap)
        # print(f"\nNew Heap: {heap}\nNew Costs: {costs}")
        
    return costs


def precompute_distances(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    dict[node, dict[node, float]]
        Nested structure supporting dist_table[u][v] lookups
        for every source u your design requires.

    TODO
    """
    sources = select_sources(spawn, relics, exit_node)
    distances = {}
    for source in sources:
        distances[source] = run_dijkstra(graph, source)
    return distances


# =============================================================================
# PART 3
# =============================================================================

def dijkstra_invariant_check():
    """
    Returns
    -------
    str
        Your Part 3 README answers, written as a string.
        Must match what you wrote in README Part 3.

    TODO
    """
    return "Initialization : why the invariant holds before iteration 1:\n" \
            "S only holds the cost of 0 for itself, as the cost from S to itself is known to be 0" \
            "All other minima unknown, so their costs are infinite." \
            "Maintenance : why finalizing the min-dist node is always correct:\n" \
            "Because there are no negative edge weights, the current minimum node cannot be reached in a different way that doesn't cost more" \
            "Taking another path means starting from a higher weight, so the end result must be greater" \
            "Termination : what the invariant guarantees when the algorithm ends:\n" \
            "At termination, all node costs will be minimal, with unreachable nodes having an infinite cost.\n\n" \
            "We want to go between relic rooms and to the exit while incurring the lowest penalty" \
            "Having shortest paths between spawn, relic rooms, and exits will help us determine this best path."


# =============================================================================
# PART 4
# =============================================================================

def explain_search():
    """
    Returns
    -------
    str
        Your Part 4 README answers, written as a string.
        Must match what you wrote in README Part 4.

    TODO
    """
    return "TODO"


# =============================================================================
# PARTS 5 + 6
# =============================================================================

def find_optimal_route(dist_table, spawn, relics, exit_node):
    """
    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
        Output of precompute_distances.
    spawn : node
    relics : list[node]
        Every node in this list must be visited at least once.
    exit_node : node
        The route must end here.

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


def _explore(dist_table, current_loc, relics_remaining, relics_visited_order,
             cost_so_far, exit_node, best):
    """
    Recursive helper for find_optimal_route.

    Parameters
    ----------
    dist_table : dict[node, dict[node, float]]
    current_loc : node
    relics_remaining : collection
        Your chosen data structure from README Part 5b.
    relics_visited_order : list[node]
    cost_so_far : float
    exit_node : node
    best : list
        Mutable container for the best solution found so far.

    Returns
    -------
    None
        Updates best in place.

    TODO
    Implement: base case, pruning, recursive case, backtracking.

    REQUIRED: Add a 1-2 sentence comment near your pruning condition
    explaining why it is safe (cannot skip the optimal solution).
    This comment is graded.
    """
    pass


# =============================================================================
# PIPELINE
# =============================================================================

def solve(graph, spawn, relics, exit_node):
    """
    Parameters
    ----------
    graph : dict[node, list[tuple[node, int]]]
    spawn : node
    relics : list[node]
    exit_node : node

    Returns
    -------
    tuple[float, list[node]]
        (minimum_fuel_cost, ordered_relic_list)
        Returns (float('inf'), []) if no valid route exists.

    TODO
    """
    pass


# =============================================================================
# PROVIDED TESTS (do not modify)
# Graders will run additional tests beyond these.
# =============================================================================

def _run_tests():
    print("Running provided tests...")

    # Test 1: Spec illustration. Optimal cost = 4.
    graph_1 = {
        'S': [('B', 1), ('C', 2), ('D', 2)],
        'B': [('D', 1), ('T', 1)],
        'C': [('B', 1), ('T', 1)],
        'D': [('B', 1), ('C', 1)],
        'T': []
    }
    print(f"selected sources are: {select_sources('S', ['B', 'C', 'D'], 'T')}")
    print(f"final costs: {run_dijkstra(graph_1, 'S')}, type: {type}")
    print(f"The distances from every sources are: {precompute_distances(graph_1, 'S', ['B', 'C', 'D'], 'T')}")
    # cost, order = solve(graph_1, 'S', ['B', 'C', 'D'], 'T')
    # assert cost == 4, f"Test 1 FAILED: expected 4, got {cost}"
    # print(f"  Test 1 passed  cost={cost}  order={order}")

    # # Test 2: Single relic. Optimal cost = 5.
    # graph_2 = {
    #     'S': [('R', 3)],
    #     'R': [('T', 2)],
    #     'T': []
    # }
    # cost, order = solve(graph_2, 'S', ['R'], 'T')
    # assert cost == 5, f"Test 2 FAILED: expected 5, got {cost}"
    # print(f"  Test 2 passed  cost={cost}  order={order}")

    # # Test 3: No valid path to exit. Must return (inf, []).
    # graph_3 = {
    #     'S': [('R', 1)],
    #     'R': [],
    #     'T': []
    # }
    # cost, order = solve(graph_3, 'S', ['R'], 'T')
    # assert cost == float('inf'), f"Test 3 FAILED: expected inf, got {cost}"
    # print(f"  Test 3 passed  cost={cost}")

    # # Test 4: Relics reachable only through intermediate rooms.
    # # Optimal cost = 6.
    # graph_4 = {
    #     'S': [('X', 1)],
    #     'X': [('R1', 2), ('R2', 5)],
    #     'R1': [('Y', 1)],
    #     'Y': [('R2', 1)],
    #     'R2': [('T', 1)],
    #     'T': []
    # }
    # cost, order = solve(graph_4, 'S', ['R1', 'R2'], 'T')
    # assert cost == 6, f"Test 4 FAILED: expected 6, got {cost}"
    # print(f"  Test 4 passed  cost={cost}  order={order}")

    # # Test 5: Explanation functions must return non-placeholder strings.
    # for fn in [explain_problem, dijkstra_invariant_check, explain_search]:
    #     result = fn()
    #     assert isinstance(result, str) and result != "TODO" and len(result) > 20, \
    #         f"Test 5 FAILED: {fn.__name__} returned placeholder or empty string"
    # print("  Test 5 passed  explanation functions are non-empty")

    # print("\nAll provided tests passed.")


if __name__ == "__main__":
    _run_tests()
