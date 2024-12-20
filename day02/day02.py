def hasSafeTrend(levels):
    length = len(levels)
    for cur_index in range(length):
        nxt_index = min(cur_index + 1, length - 1)
        if cur_index < nxt_index:
            diff = abs(levels[cur_index] - levels[nxt_index])
            if not (1 <= diff <= 3):
                return False
    return True


def increasing_or_decreasing(levels):
    asc_levels = sorted(levels)
    desc_levels = sorted(levels, reverse=True)
    return levels == asc_levels or levels == desc_levels


def isSafe(levels, is_dampener_on):
    safe = increasing_or_decreasing(levels) and hasSafeTrend(levels)
    if not safe and is_dampener_on:
        for i in range(len(levels)):
            if not safe:
                smaller_levels = levels.copy()
                smaller_levels.pop(i)
                if (increasing_or_decreasing(smaller_levels) and hasSafeTrend(smaller_levels)):
                    safe = True
    return safe


with open("input.txt", "r") as file:
    lines = file.readlines()
    num_safe_reports = 0
    for line in lines:
        levels = list(map(int, line.strip().split(" ")))
        if isSafe(levels, True):
            num_safe_reports += 1
    print(num_safe_reports)
