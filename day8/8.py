f = open("input8")
line = f.readline().rstrip()

(w, h) = (25, 6)
frame_size = w*h
num_frames = len(line)/frame_size

#
# PART 1
#

# find frame with fewest "0"
frame_fewest_zero_num = frame_size
frame_fewest_zero_id = None
for frame in range(num_frames):
    (s, e) = (frame*frame_size, (frame+1)*frame_size)
    num_zeroes = line[s:e].count("0")
    if num_zeroes < frame_fewest_zero_num:
        frame_fewest_zero_num = num_zeroes
        frame_fewest_zero_id = frame

(s, e) = (frame_fewest_zero_id*frame_size, (frame_fewest_zero_id+1)*frame_size)
print("value for frame with fewest zeroes: %d" % (line[s:e].count("1")*line[s:e].count("2")))

#
# PART 2
#

# select the first non-transparent pixel and add to result_image
result_image = ""
for pixel in range(frame_size):
    pix_range = line[pixel::frame_size]
    i = 0
    for i in range(num_frames):
        if pix_range[i] != "2":
            break
    result_image += pix_range[i]

result_image = result_image.replace("1", " ") # for visibility
# print result_image
for i in range(h):
    print("%s" % result_image[i*w:(i+1)*w])

