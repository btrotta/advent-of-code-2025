from utilities import parse_multi_string

arr = parse_multi_string(sep=" ")
machines = []
for i, a in enumerate(arr):
    curr_machine = {"state": [], "buttons": []}
    for s in a:
        if s[0] == "[":
            for ch in s[1:-1]:
                if ch == ".":
                    curr_machine["state"].append(0)
                else:
                    curr_machine["state"].append(1)
        elif s[0] == "(":
            vals = [int(x) for x in s[1:-1].split(",")]
            curr_machine["buttons"].append(tuple(vals))
    machines.append(curr_machine)

# WLOG, each button needs to be pressed at most once
# order of button pressing doesn't matter
ans = 0
for m in machines:
    target_state = m["state"]
    buttons = m["buttons"]
    state_dict = {tuple(): [0 for i in range(len(target_state))]}  # map set of button presses to state
    target_reached = False
    while not target_reached:
        new_state_dict = {}
        for button_set, prev_state in state_dict.items():
            for b in buttons:
                if b not in button_set:
                    new_button_set = tuple(sorted(button_set + (b, )))
                    new_state = prev_state.copy()
                    for ind in b:
                        new_state[ind] = 1 - new_state[ind]
                    new_state_dict[new_button_set] = new_state
                    if target_state == new_state:
                        ans += len(new_button_set)
                        target_reached = True
                        break
            if target_reached:
                break
        state_dict = new_state_dict

print(ans)

