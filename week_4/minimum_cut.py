from typing import List, Tuple
from collections import defaultdict
import random
import copy


def build_graph(rows) -> dict:
    graph = defaultdict(lambda: {'fused': [], 'connected': {}})

    for row in rows:
        nodes = [int(_) for _ in row.split()]
        this_node, connected = nodes[0], nodes[1:]

        for n in connected:
            graph[this_node]['connected'][n] = True
            graph[n]['connected'][this_node] = True
  
    return graph


def pick_random_edge(graph: dict) -> Tuple[int, int]:
    from_node = random.choice(list(graph.keys()))
    to_node = random.choice(list(graph[from_node]['connected'].keys()))
    return from_node, to_node


def fuse_edge(graph: dict, edge: Tuple[int, int]) -> dict:
    """
        Remove edge, then construct new edges connecting to the combined
        node with all nodes that the deleted/contracted node is connected to.
        Also clean up, or remove, any edges connecting to the 
        deleted/contracted node.
    """
    del graph[edge[0]]['connected'][edge[1]]
    del graph[edge[1]]['connected'][edge[0]]
    
    clean_up_edges = []
    combined_node = edge[0]
    delete_node = edge[1]

    for connected_to in graph[delete_node]['connected']:
        if combined_node != connected_to:
            graph[combined_node]['connected'][connected_to] = True
            graph[connected_to]['connected'][combined_node] = True
            clean_up_edges.append((connected_to, delete_node))

    graph[combined_node]['fused'].append(delete_node)
    graph[combined_node]['fused'].extend(graph[delete_node]['fused'])
    del graph[delete_node]

    for stale_edge in clean_up_edges:
        del graph[stale_edge[0]]['connected'][stale_edge[1]]
    
    return graph


def random_contract(graph: dict) -> Tuple[List[int], List[int]]:
    while len(graph.items()) > 2:
        edge: Tuple[int, int] = pick_random_edge(graph)
        graph = fuse_edge(graph, edge)

    partitions = []

    for node in graph:
        partitions.append(sorted([node] + graph[node]['fused']))

    return tuple(partitions)


def count_cuts(partitions: Tuple[List[int], List[int]], graph: dict):
    total = 0
    a, b = partitions

    for i in a:
        for j in b:
            if graph[i]['connected'].get(j):
                total += 1

    return total


with open('data/graph.txt', 'r') as f:
    rows = f.read().splitlines()

graph = build_graph(rows)
best_min_cut_count = None

for x in range(0, 40000):
    partitions = random_contract(copy.deepcopy(graph))
    cut_count = count_cuts(partitions, graph)

    if best_min_cut_count is None or cut_count < best_min_cut_count:
        best_min_cut_count = cut_count
        print('Nice! Just found an even better cut: %s' % best_min_cut_count)

print('Best: %s' % best_min_cut_count)
