from utilities import parse_single_string
import re
import math

arr = parse_single_string(True)
num_problems = len(re.split(" +", arr[0].strip()))
problems = [[] for i in range(num_problems)]
for a in arr[:-1]:
    for i, n in enumerate(re.split(" +", a.strip())):
        problems[i].append(int(n))
ans = 0
for i, sym in enumerate(re.split(" +", arr[-1].strip())):
    if sym == "+":
        ans += sum(problems[i])
    else:
        ans += math.prod(problems[i])
print(ans)

