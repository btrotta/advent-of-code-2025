from utilities import parse_multi_int

arr = parse_multi_int(sep="")
ans = 0
for a in arr:
    curr_max = a[-12:]  # curr_max[i] is the current max value for the i_th battery
    for n in reversed(a[:-12]):
        new_val = n
        for i in range(12):
            if new_val >= curr_max[i]:
                new_val2 = curr_max[i]
                curr_max[i] = new_val
                new_val = new_val2
            else:
                break
    for i in range(12):
        ans += curr_max[i] * 10 ** (11 - i)
print(ans)
