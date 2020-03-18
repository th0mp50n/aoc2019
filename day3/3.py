import sys

f = open("input3")

w1 = f.readline().rstrip().split(",")
w2 = f.readline().rstrip().split(",")

def newpos(pos, move):
    (dir, dist, neg) = move[0], int(move[1:]), 1
    if(dir in "DL"):
        neg = -1
    if(dir in 'UD'):
        new_pos = (pos[0], pos[1]+(dist*neg))
    else:
        new_pos = (pos[0]+(dist*neg), pos[1])
    return new_pos

def intersection(l1, l2):
    (ax, ay, bx, by, cx, cy, dx, dy) = (l1[0][0], l1[0][1], l1[1][0], l1[1][1],
                                        l2[0][0], l2[0][1], l2[1][0], l2[1][1])
    
    #print("points: ", ax, ay, bx, by, cx, cy, dx, dy)

    if ax == bx and cx == dx: # vertical lines
        if ax != cx: # parallel
            return None
        else: # same vertical line
            if ay > by: # orientate line 1
                #print("orienting line 1")
                ax, ay, bx, by = bx, by, ax, ay
            if cy > dy: # orientate line 2
                #print("orienting line 1")
                cx, cy, dx, dy = dx, dy, cx, cy
            if ay > cy: # sort lines
                #print("sorting lines")
                ax, ay, bx, by, cx, cy, dx, dy = cx, cy, dx, dy, ax, ay, bx, by
            if ay <= cy <= by: # check overlap
                if ay <= 0 <= by:
                    if cy <= 0 <= dy: # both lines pass through x axis
                        return (ax, 0)
                    # else here was erroneous
                if cy > 0: # positive y axis
                    return (ax, cy)
                else: # negative y axis
                    if dy < by:
                        return (ax, dy) # line 2 encapsulated
                    else:
                        return (ax, by) # line 2 extending
            else: # no overlap
                return None
    elif ay == by and cy == dy: # horizontal lines: transpose and call intersection()
        result = intersection([[ay, ax], [by, bx]], [[cy, cx], [dy, dx]])
        if result:
            return (result[1], result[0]) # back-transpose result
        else:
            return None
    else: # perpendicular lines
        # make a-b the vertical line and c-d the horizontal line AND vert/horiz line direction up/right respectively
        if cx == dx:
            ax, ay, bx, by, cx, cy, dx, dy = dx, dy, cx, cy, ax, ay, bx, by
        if ay > by:
            ax, ay, bx, by = bx, by, ax, ay
        if cx > dx:
            cx, cy, dx, dy = dx, dy, cx, cy
        # compute intersection if exists
        if cx <= ax <= dx and ay <= cy <= by:
            return (ax, cy)
        else:
            return None
    # error if reach here

def dist(p1, p2):
    (ax, ay, bx, by) = p1[0], p1[1], p2[0], p2[1]

    if ax == bx: # vertical line
        return abs(ay - by)
    if ay == by: # horizontal line
        return abs(ax - bx)
    raise Exception('Two points not on same line')

cable1 = []
start = (0,0)
for m in w1:
    new = newpos(start, m)
    cable1.append((start, new))
    print("start", start, "move", m, "new", new)
    start = new

cable2 = []
start = (0,0)
for m in w2:
    new = newpos(start, m)
    cable2.append((start, new))
    print("start", start, "move", m, "new", new)
    start = new

shortest = None
stored_intersections = []
for l1 in cable1:
    print(l1)
    for l2 in cable2:
        #print("l1: {}, l2: {}".format(str(l1), str(l2)))
        i = intersection(l1, l2)
        #print("intersecting at: " + str(i))
        if i:
            distance = abs(i[0]) + abs(i[1])
            if distance == 0: # incorrect if cables intersect at origin after initial start
                continue
            if shortest == None or distance < shortest:
                shortest = distance
            stored_intersections.append(i) # store intersections

print("manhattan distance: %d" % (shortest))

# now to compute shortest signal delay
def dist_to_intersect(i):
    distl1 = 0
    distl2 = 0
    for l1 in cable1:
        distl1 = distl1 + dist(l1[0], l1[1])
        if intersection(l1, [i, i]):
            for l2 in cable2:
                distl2 = distl2 + dist(l2[0], l2[1])
                if intersection(l2, [i, i]):
                    s1 = dist(l1[1], i)
                    s2 = dist(l2[1], i)
                    return distl1 + distl2 - s1 - s2

print(stored_intersections)

print(sorted(list(map(dist_to_intersect, stored_intersections))))

# print( intersection([[0,6],[0,15]], [[0,10], [0,1]]) ) # positive overlapping vertical out of order lines
# print( intersection([[0,6],[0,15]], [[0,20], [0,16]]) ) # positive non-overlapping vertical out of order lines
# print( intersection([[0,-10],[0,-5]], [[0,-7], [0,-2]]) ) # negative overlapping vertical ordered lines
# print( intersection([[0,-20],[0,10]], [[0,-10], [0,10]]) ) # overlapping lines both intersectioning x axis
# print( intersection([[0,-10],[0,-5]], [[0,-7], [0,-6]]) ) # negative overlapping encapsulated ordered

# print( intersection([[0,-10],[0,-5]], [[-10,-7], [10,-7]]) ) # perpendicular with intersection
# print( intersection([[0,-10],[0,-5]], [[-10,-7], [-2,-7]]) ) # perpendicular without intersection

# print( intersection([[6,0],[15,0]], [[10,0], [1,0]]) ) # positive overlapping horizontal out of order lines
# print( intersection([[-10,0],[-5,0]], [[-7,-10], [-7,10]]) ) # perpendicular with intersection
# print( intersection([[-15,0],[6,0]], [[4,0], [1,0]]) ) # CAUGHT wrong else condition after "if ay <= 0 <= by:": if line 2 doesn't pass x axis then proceed

# print( intersection([[0,6],[0,15]], [[0,8], [0,8]]) ) # line and point intersection
# print( intersection([[0,8], [0,8]], [[0,6],[0,15]]) ) # point and line intersection
# print( intersection([[0,6],[0,15]], [[0,5], [0,5]]) ) # line and point not intersecting

# print( dist([0,6], [0,15]) )
# print( dist([6,0], [15,0]) )
# try:
#     print( dist([0,6], [6,15]) )
# except Exception as ex:
#     print("Caught exception ", ex)
