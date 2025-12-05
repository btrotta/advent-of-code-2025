from utilities import parse_01, DIRECTIONS_DIAG

arr = parse_01(one_char="@")

rolls = set([complex(i, j) for i in range(len(arr[0])) for j in range(len(arr)) if arr[i][j] == 1])

ans = 0
for r in rolls:
    num_adj = 0
    for d in DIRECTIONS_DIAG:
        if r + d in rolls:
            num_adj += 1
            if num_adj >= 4:
                break
    else:
        ans += 1
print(ans)
