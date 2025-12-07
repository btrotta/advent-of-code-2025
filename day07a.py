from utilities import parse_multi_string

arr = parse_multi_string(sep="")

ans = 0
for i, ch in enumerate(arr[0]):
    if ch == "S":
        beams = {i}
for a in arr[1:]:
    new_beams = set()
    for i in beams:
        if a[i] == "^":
            ans += 1
            if i - 1 >= 0:
                new_beams.add(i - 1)
            if i + 1 < len(a):
                new_beams.add(i + 1)
        else:
            new_beams.add(i)
    beams = new_beams
print(ans)

