with open("input.txt", "r") as file:
    lines = file.readlines()
    left_collection = []
    right_collection = []
    for line in lines:
        left, right = line.strip().split("   ")
        left_collection.append(int(left))
        right_collection.append(int(right))
    left_collection.sort()
    right_collection.sort()

    diff_sum = 0
    for i in range(len(left_collection)):
        diff_sum += abs(left_collection[i] - right_collection[i])
    print(diff_sum)

    similarity_score = 0
    for right_num in right_collection:
        if right_num in left_collection:
            similarity_score += right_num
    print(similarity_score)
