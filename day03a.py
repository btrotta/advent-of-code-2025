from utilities import parse_multi_int

arr = parse_multi_int(sep="")
ans = 0
for a in arr:
    curr_max = -1
    prev_max = a[-1]
    for n in reversed(a[:-1]):
        if n >= curr_max:
            prev_max = max(curr_max, prev_max)
            curr_max = n
    ans += curr_max * 10 + prev_max
print(ans)
