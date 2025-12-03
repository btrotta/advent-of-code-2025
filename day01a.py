from utilities import parse_single_string

arr = parse_single_string()
curr = 50
ans = 0
for a in arr:
    dir, num = a[0], a[1:]
    num = int(num)
    if dir == "L":
        curr -= num
    else:
        curr += num
    curr = curr % 100
    if curr == 0:
        ans += 1

print(ans)
