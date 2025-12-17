from utilities import parse_multi_string
import numpy as np
from functools import reduce

arr = parse_multi_string(False, sep=" ")
machines = []
for i, a in enumerate(arr):
    curr_machine = {"buttons": [], "joltage": []}
    for s in a:
        if s[0] == "(":
            vals = [int(x) for x in s[1:-1].split(",")]
            curr_machine["buttons"].append(tuple(vals))
        elif s[0] == "{":
            for ch in s[1:-1].split(","):
                curr_machine["joltage"].append(int(ch))
    machines.append(curr_machine)


# each button may need to be pressed multiple times
# order of button pressing doesn't matter
ans = 0
for m in machines:
    target_state = np.array(m["joltage"])
    buttons = m["buttons"]
    arr_buttons = []
    for b in buttons:
        curr_arr = [0 for i in range(len(target_state))]
        for i in b:
            curr_arr[i] = 1
        arr_buttons.append(np.array(curr_arr))
    min_button_sum = min([len(b) for b in buttons])
    max_button_sum = max([len(b) for b in buttons])
    np.seterr(all="raise")


    def get_shortest(target_state, curr_count=0, exclude_buttons=()):
        if len(exclude_buttons) == len(buttons):
            return np.inf

        # check target state is feasible
        changed = True
        max_counts = np.array([max(target_state) for i in range(len(buttons))])
        max_counts[list(exclude_buttons)] = 0
        min_counts = np.array([0 for i in range(len(buttons))])
        while changed:
            changed = False
            for i, x in enumerate(target_state):
                for j, b in enumerate(buttons):
                    if i in b and j not in exclude_buttons:
                        if x < max_counts[j]:
                            max_counts[j] = x
                            changed = True
            max_total = sum([max_counts[i] * arr_buttons[i] for i in range(len(buttons))])
            for i, x in enumerate(target_state):
                curr_buttons = [j for j, b in enumerate(buttons) if i in b and j not in exclude_buttons]
                for j in curr_buttons:
                    n = sum([max_counts[k] for k in curr_buttons if k != j if k not in exclude_buttons])
                    if n < x:
                        if x - n > min_counts[j]:
                            min_counts[j] = x - n
                            changed = True
            min_total = sum([min_counts[i] * arr_buttons[i] for i in range(len(buttons))])
            if np.any(min_total > target_state) or np.any(min_counts > max_counts) or np.any(max_total < target_state):
                return np.inf

        for i, x in enumerate(target_state):
            if x == 0:
                continue
            common = reduce(np.intersect1d, [b for b in buttons if i in b])
            common_states = [y for j, y in enumerate(target_state) if j in common]
            if min(common_states) < x:
                return np.inf

        # find target counter with smallest number of possible button combinations
        num_choices = (max_counts - min_counts).astype(float)
        num_choices[list(exclude_buttons)] = np.inf
        best_button = np.argmin(num_choices)
        coeff = np.hstack(
                    [a[:, np.newaxis] for j, a in enumerate(arr_buttons) if
                     j not in exclude_buttons and j != best_button])
        rank = np.linalg.matrix_rank(coeff)
        new_exclude_buttons = tuple(sorted(exclude_buttons + (best_button,)))
        best_count = np.inf
        for button_count in range(min_counts[best_button], max_counts[best_button] + 1):
            new_target = target_state - arr_buttons[best_button] * button_count
            if np.any(new_target < 0):
                continue
            elif np.any(new_target > 0):
                if rank >= len(buttons) - len(exclude_buttons) - 1:
                    ans = np.linalg.lstsq(coeff, new_target)
                    int_x = np.abs(
                        np.round(np.maximum(0, np.minimum(ans[0], np.max(new_target))),
                                 0).astype(int))
                    if np.all(np.matmul(coeff, int_x).astype(int) == new_target):
                        best_count = min(best_count, curr_count + button_count + sum(int_x))
                else:
                     best_count = min(best_count, get_shortest(new_target, curr_count + button_count, new_exclude_buttons))
            else:
                best_count = min(best_count, curr_count + button_count)
        return best_count

    curr_ans = get_shortest(target_state)
    ans += curr_ans

print(ans)
