from utilities import parse_single_string

arr = parse_single_string(False)
ranges = []
for a in arr:
    if a == "":
        break
    else:
        x, y = a.split("-")
        x, y = int(x), int(y)
        ranges.append([x, y])

ranges = sorted(ranges, key=lambda x: x[0])
ans = 0
curr_left, curr_right = ranges[0]
for left, right in ranges[1:]:
    if left <= curr_right and right > curr_right:
        curr_right = right
    elif left > curr_right:
       ans += curr_right - curr_left + 1
       curr_left, curr_right = left, right
ans += curr_right - curr_left + 1
print(ans)
