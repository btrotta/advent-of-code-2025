from utilities import parse_multi_string

arr = parse_multi_string(sep=",")
arr = arr[0]
ans = set()
for a in arr:
    lower, upper = a.split("-")
    lower, upper = int(lower), int(upper)
    for b in range(lower, upper + 1):
        b_str = str(b)
        n = len(b_str)
        if n % 2 == 0 and b_str[:n//2] == b_str[n//2:]:
            ans.add(b)
print(sum(ans))
