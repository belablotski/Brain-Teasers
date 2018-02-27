move_num = 1

def move_one(disc, src, dest):
    global move_num
    print "{}: Move disc {} from pole {} to {}".format(move_num, disc, src, dest)
    move_num += 1

def move_many(disc, src, dest):
    tmp = list(set([1, 2, 3]) - set([src, dest]))[0]
    if disc > 1:
        move_many(disc-1, src, tmp)
    move_one(disc, src, dest)
    if disc > 1:
        move_many(disc-1, tmp, dest)

if __name__ == "__main__":
    move_many(5, 1, 3)