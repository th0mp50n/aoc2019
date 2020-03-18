f = open("input6")

data = {} # dictionary: key=child, val=parent
for line in f:
    (val, key) = line.rstrip().split(")")
    data[key] = val

#
# PART 1
#

# count all the connections upwards the tree from node <next>
def follow(sum, next):
    next_nodes = [k for k, v in data.items() if v == next]
    tmp_sum = 0
    for up in next_nodes:
        tmp_sum += follow(sum+1, up)
    return sum + tmp_sum
    
print("total orbits: %s" % (follow(0, "COM")))

#
# PART 2
#

# return the path to the <target>
def find(path, next, target): 
    next_nodes = [k for k, v in data.items() if v == next]
    path_found = None
    for up in next_nodes:
        if up == target:
            return path + [up]
        else:
            path_found = find(path + [up], up, target)
            if path_found:
                break
    return path_found

# count length of the common root between node "YOU" and node "SAN"
path1 = find([], "COM", "YOU")
path2 = find([], "COM", "SAN")
cnt = 0
for i in range(len(path1)):
    if i<len(path1) and i<len(path2) and path1[i] == path2[i]:
        cnt += 1
# calculate length of route between "YOU" and "SAN"
print("distance between YOU and SAN: %d" % (len(path1) + len(path2) - 2*cnt -2))
