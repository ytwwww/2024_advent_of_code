import re

# Part One
with open("input.txt", "r") as f:
    input = f.read().rstrip()
    matches = re.findall("mul\(\d+,\d+\)", input)
    sum = 0
    for match in matches:
        numbers = re.findall("\d+", match)
        result = 1
        for num in numbers:
            result *= int(num)
        sum += result
    print(sum)


# Part Two
with open("input.txt", "r") as f:
    input = f.read().rstrip()
    matches = re.findall("mul\(\d+,\d+\)|don't\(\)|do\(\)", input)
    sum = 0
    do = True
    for match in matches:
        if match == "do()":
            do = True
        elif match == "don\'t()":
            do = False
        elif do:
            numbers = re.findall("\d+", match)
            result = 1
            for num in numbers:
                result *= int(num)
            sum += result
    print(sum)