from utilities import parse_multi_string
import math

arr = parse_multi_string(sep="")
# pad with spaces so all rows are same length
max_len = max(len(a) for a in arr)
for i in range(len(arr)):
    arr[i] = arr[i] + [" " for i in range(max_len - len(arr[i]))]
ans = 0
curr_ans = 0
for col, ch in enumerate(arr[-1]):
    if ch == "+":
        op = sum
        ans += curr_ans
        curr_ans = 0
    elif ch == "*":
        op = math.prod
        ans += curr_ans
        curr_ans = 1
    n = 0
    for row in range(len(arr) - 1):
        ch = arr[row][col]
        if ch != " ":
            n = n * 10 + int(ch)
    if n > 0:
        curr_ans = op([curr_ans, n])
ans += curr_ans

print(ans)

