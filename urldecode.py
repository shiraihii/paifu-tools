import sys
# Take a replay URL, spit out the URL for the mjlog
# Input needs to be a full log spec - 2012072820gm-0009-0000-x33591c066f4f

t = [22136, 52719, 55146, 42104, 59591, 46934, 9248, 28891, 49597, 52974, 62844, 4015, 18311, 50730, 43056, 17939, 64838, 38145, 27008, 39128, 35652, 63407, 65535, 23473, 35164, 55230, 27536, 4386, 64920, 29075, 42617, 17294, 18868, 2081]
src = sys.argv[1].split('-')

a = int(src[3][1:5], 16)
b = int(src[3][5:9], 16)
c = int(src[3][9:13], 16)
d = 0
if src[0] >= "2010041111gm":
	d = int("3" + src[0][4:10]) % (((17 * 2) - int(src[0][9])) - 1)

src[3] = "%x%x" % (a^b^t[d], b^t[d]^c^t[d+1])
print "-".join(src)

