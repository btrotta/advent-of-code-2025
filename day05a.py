from utilities import parse_single_string

arr = parse_single_string()
ranges = []
first_part = True
ans = 0
for a in arr:
    if a == "":
        first_part = False
    elif first_part:
        x, y = a.split("-")
        x, y = int(x), int(y)
        ranges.append([x, y])
    else:
       z = int(a)
       for x, y in ranges:
           if x <= z <= y:
               ans += 1
               break

print(ans)
