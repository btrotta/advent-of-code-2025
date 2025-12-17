from utilities import parse_single_string
import numpy as np

arr = parse_single_string()
presents = []
grids = []

for a in arr:
    if a == "":
        if curr_present is not None:
            presents.append(curr_present)
        curr_present = None
    elif a[-1] == ":":
        curr_present = []
        curr_size = 0
    elif ":" not in a:
        curr_row = [1 if ch == "#" else 0 for ch in a]
        curr_present.append(curr_row)
    else:
        b = a.split(" ")
        w, h = [int(x) for x in b[0][:-1].split("x")]
        counts = np.array([int(x) for x in b[1:]])
        grids.append([[w, h], counts])

present_sizes = np.array([np.array(x).sum() for x in presents])

ans = 0
fail_count = 0
for [w, h], counts in grids:
    if w * h < (present_sizes * counts).sum():
        continue
    elif (w // 3) * (h // 3) >= sum(counts):
        ans += 1
    else:
        fail_count += 1
print(fail_count)
print(ans)
