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
        for k in range(1, n // 2 + 1):
            m = n // k
            if n % k == 0 and all([b_str[i * k:(i + 1) * k] == b_str[:k] for i in range(1, m)]):
                ans.add(b)
print(sum(ans))
