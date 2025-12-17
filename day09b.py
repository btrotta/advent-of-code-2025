from utilities import parse_multi_int

arr = parse_multi_int(sep=",")

max_area = 0
for i, a in enumerate(arr):
    for j, b in enumerate(arr[i+1:]):
        curr_area = (abs(a[0] - b[0]) + 1) * (abs(a[1] - b[1]) + 1)
        if curr_area <= max_area:
            continue
        v_min, v_max = min(a[0], b[0]), max(a[0], b[0])
        h_min, h_max = min(a[1], b[1]), max(a[1], b[1])
        check_ok = True
        for k in range(len(arr)):
            e1 = arr[k]
            e2 = arr[(k + 1) % len(arr)]
            # e1 and e2 are the same in either the x or y coord;
            # ensure the other coord is sorted
            e1, e2 = sorted([e1, e2])
            # check edges of loop do not intersect inner boundary of rectangle, and
            # no edge is inside the inner border of the rectangle
            if e1[0] == e2[0]:
                if (v_min < e1[0] < v_max) and ((e1[1] < h_min < e2[1]) or (e1[1] < h_max < e2[1]) or (h_min <= e1[1] <= e2[1] <= h_max)):
                    check_ok = False
                    break
            else:
                if (h_min < e1[1] < h_max) and ((e1[0] < v_min < e2[0]) or (e1[0] < v_max < e2[0]) or (v_min <= e1[0] <= e2[0] <= v_max)):
                    check_ok = False
                    break
        if not check_ok:
            continue
        # check rectangle is inside (not outside) the loop
        if v_max - v_min > 1 and h_max - h_min > 1:
            inner_point = [v_min + 1, h_min + 1]
            num_border_crossings = 0
            for k in range(len(arr)):
                e1 = arr[k]
                e2 = arr[(k + 1) % len(arr)]
                e1, e2 = sorted([e1, e2])
                if e1[0] == e2[0]:
                    if e1[0] <= inner_point[0] and e1[1] < inner_point[1] < e2[1]:
                        num_border_crossings += 1
            if num_border_crossings % 2 == 0:
                check_ok = False
        if check_ok:
            max_area = curr_area

print(max_area)
