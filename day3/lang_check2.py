# (p1, p2)
# (q1, q2)
# in coordinates

# list coordinates
# loop over permutations
#   check and store any intersection
# calculate distance for all intersections

f = open("input3")

w1 = f.readline().rstrip().split(",")
w2 = f.readline().rstrip().split(",")

print(len(w1))

# no output? ah, lazy
map(lambda x: calc_line((0,0), x), w1)

def calc_line(pos, move):
    (dir, dist) = move[0], move[1:]
    print("dir ", dir, "dist", dist)
    return 1
