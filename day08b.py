from utilities import parse_multi_int

arr = parse_multi_int(sep=",")

dist = {}
for i, x in enumerate(arr):
    for y in arr[i+1:]:
        dist[tuple(x), tuple(y)] = (x[0] - y[0]) ** 2 + (x[1] - y[1]) ** 2 + (x[2] - y[2]) ** 2


class Component:
    def __init__(self, id, size=0):
        self.id = id
        self.size = size
        self.parent = None


def get_top_component(comp):
    while comp.parent is not None:
        comp = comp.parent
    return comp


def increment_size(comp):
    # increment size of all parents and return size of top component
    comp.size += 1
    while comp.parent is not None:
        comp = comp.parent
        comp.size += 1
    return comp.size

sorted_pairs = sorted(list(dist.keys()), key=lambda x: dist[x])
node_to_comp = {}  # map node to component, can contain multiple references to same component
id_to_comp = {}
curr_component_num = 0
for x, y in sorted_pairs:
    if x in node_to_comp and y in node_to_comp:
        old_comp_x = get_top_component(node_to_comp[x])
        old_comp_y = get_top_component(node_to_comp[y])
        if old_comp_x.id != old_comp_y.id:
            top_size = old_comp_x.size + old_comp_y.size
            new_comp = Component(curr_component_num, top_size)
            id_to_comp[curr_component_num] = new_comp
            curr_component_num += 1
            old_comp_x.parent = new_comp
            old_comp_y.parent = new_comp
    elif x in node_to_comp:
        node_to_comp[y] = node_to_comp[x]
        top_size = increment_size(node_to_comp[x])
    elif y in node_to_comp:
        node_to_comp[x] = node_to_comp[y]
        top_size = increment_size(node_to_comp[y])
    else:
        new_comp = Component(curr_component_num, 2)
        id_to_comp[curr_component_num] = new_comp
        curr_component_num += 1
        node_to_comp[x] = new_comp
        node_to_comp[y] = new_comp
        top_size = 2
    if top_size == len(arr):
        break

ans = x[0] * y[0]
print(ans)
