class HanoiTowers(object):
    """Solve Hanoi towers puzzle with checker"""

    def __init__(self, num_of_disks):
        self.__move_num = 1
        self.__num_of_disks = num_of_disks
        self.__poles = [range(1, self.__num_of_disks+1), [], []]

    def __move_one(self, disc, src, dest):
        print "{}: Move disc {} from pole {} to {}".format(self.__move_num, disc, src, dest)
        assert self.__poles[src-1][0] == disc
        self.__poles[src-1] = self.__poles[src-1][1:]
        assert len(self.__poles[dest-1]) == 0 or self.__poles[dest-1][0] > disc
        self.__poles[dest-1].insert(0, disc)
        self.__move_num += 1
        print "Poles after: {}\n".format(self.__poles)

    def __move(self, disc, src, dest):
        tmp = list(set([1, 2, 3]) - set([src, dest]))[0]
        if disc > 1:
            self.__move(disc-1, src, tmp)
        self.__move_one(disc, src, dest)
        if disc > 1:
            self.__move(disc-1, tmp, dest)

    def start(self):
        print "Poles: {}\n".format(self.__poles)
        self.__move(self.__num_of_disks, 1, 3)

if __name__ == "__main__":
    ht = HanoiTowers(3)
    ht.start()