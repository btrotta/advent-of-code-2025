from utilities import parse_multi_int
import math
from utilities import connected_components
from collections import defaultdict

arr = parse_multi_int(sep=",")

dist = {}
for i, x in enumerate(arr):
    for y in arr[i+1:]:
        dist[tuple(x), tuple(y)] = (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2

sorted_pairs = sorted(list(dist.keys()), key=lambda x: dist[x])
num_conn = 1000
edge_dict = defaultdict(lambda: [])
for x, y in sorted_pairs[:num_conn]:
    edge_dict[x].append(y)
    edge_dict[y].append(x)

components = connected_components(edge_dict)
component_lengths = [len(x) for x in components]
ans = math.prod(sorted(component_lengths)[-3:])
print(ans)
