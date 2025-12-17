from utilities import parse_multi_string
from collections import Counter

arr = parse_multi_string(False, sep=" ")
edges = {}
for a in arr:
    n1 = a[0].replace(":", "")
    edges[n1] = []
    for n2 in a[1:]:
        edges[n1].append(n2)


def get_paths(start, end):
    curr_nodes = {start}
    paths_to_node = Counter({start: 1})
    curr_paths_to_node = Counter({start: 1})
    while len(curr_nodes) > 0:
        new_nodes = set()
        new_paths_to_node = Counter()
        for n1 in curr_nodes:
            count = curr_paths_to_node[n1]
            for n2 in edges.get(n1, []):
                new_paths_to_node.update({n2: count})
                new_nodes.add(n2)
        curr_nodes = new_nodes
        curr_paths_to_node = new_paths_to_node
        paths_to_node.update(new_paths_to_node)
    return paths_to_node[end]


ans = (get_paths("svr", "dac") * get_paths("dac", "fft") * get_paths("fft", "out")) \
      + (get_paths("svr", "fft") * get_paths("fft", "dac") * get_paths("dac", "out"))
print(ans)