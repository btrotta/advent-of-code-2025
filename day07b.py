from utilities import parse_multi_string

arr = parse_multi_string(sep="")

ans = 0
for i, ch in enumerate(arr[0]):
    if ch == "S":
        beams = {i: 1}  # count number of paths leading to this point
for a in arr[1:]:
    new_beams = {}
    for i in beams:
        if a[i] == "^":
            if i - 1 >= 0:
                new_beams[i - 1] = new_beams.get(i - 1, 0) + beams[i]
            if i + 1 < len(a):
                new_beams[i + 1] = new_beams.get(i + 1, 0) + beams[i]
        else:
            new_beams[i] = new_beams.get(i, 0) + beams[i]
    beams = new_beams

print(sum(beams.values()))

