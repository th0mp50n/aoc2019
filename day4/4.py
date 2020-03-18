counter = [int(i) for i in "193651"]

# [1,5,4,2,2,2] -> [1,5,4,4,4,4]
def next_incremental(counter):
    pivot = counter[0]
    for i in range(1, len(counter)):
        if counter[i] < pivot:
            counter[i:] = [pivot] * (len(counter)-i)
            return counter
        else:
            pivot = counter[i]

match_total = 0
i = 0
while True:
    next_incremental(counter)
    # stop condition
    if int("".join(str(x) for x in counter)) >= 649729:
        break
    # first part of assignment
    # [1,5,4,5,5,7]: success because double 5
    #
    # i = i+1 
    # if i > 20:
    #     break
    # check there is at least one double
    # mem = counter[0]
    # for j in range(1, len(counter)):
    #     if counter[j] == mem:
    #         print(counter)
    #         match_total += 1
    #         break
    #     mem = counter[j]
    #
    # second part of assignment: [1,5,4,5,5,5] fail because triple 5 and no other double
    for j in counter:
        if counter.count(j) == 2:
            print(counter)
            match_total += 1
            break
    # add one
    for j in reversed(range(0, len(counter))):
        if counter[j] < 9:
            counter[j] = counter[j] + 1
            break
        else:
            counter[j] = 0


print(match_total)