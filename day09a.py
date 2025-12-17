from utilities import parse_multi_int

arr = parse_multi_int(sep=",")

max_area = 0
for i, x in enumerate(arr):
    for y in arr[i+1:]:
        curr_area = (abs(x[0] - y[0]) + 1) * (abs(x[1] - y[1]) + 1)
        max_area = max(max_area, curr_area)

print(max_area)