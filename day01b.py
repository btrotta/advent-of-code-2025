from utilities import parse_single_string

arr = parse_single_string()
curr = 50
ans = 0
prev = curr
for a in arr:
    dir, num = a[0], a[1:]
    num = int(num)
    if dir == "L":
        curr -= num
        ans += num // 100
        curr = curr % 100
        if curr > prev and prev != 0:
            ans += 1
        elif curr == 0:
            ans += 1
    else:
        curr += num
        ans += num // 100
        curr = curr % 100
        if curr < prev:
            ans += 1
    prev = curr

print(ans)
