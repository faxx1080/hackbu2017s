from typing import List

class Prof(object):
    def __init__(self):
        self.timelist = []
        # timelist: [(0, 0, 4), (1, 13, 15)]
        # {day, timest, timeend}
        # {day: 0-6, start sun; time: float, 0 to 23.}


class Student(object) :
    def __init__(self):
        self.timelist = []
        # timelist: [{0, 0, 4, "topic"}, {1, 13, 15, "top2"}]
        # {day, timest, timeend}
        # {day: 0-6, start sun; time: float, 0 to 23., topic: string indicating topic}


def coalesce(listOfTuples):
    # topic preserved
    # [0, 1, 2] + [0, 2, 4] -> [0, 1, 4]
    newlist = []
    oldList = []
    for i in listOfTuples:
        0


def start(prof: Prof, studs: List[Student]):
    counter = {} # for diff topics
    for tup in prof.timelist:
        # all time blocks in prof
        for stu in studs:
            for stutime in stu.timelist:
                if stutime[0] != tup[0]:
                    continue
                # found a hit?
                time_st = max(stutime[1], tup[1])
                time_en = min(stutime[2], tup[2])
                if time_en - time_st < 0:
                    # fail
                    continue
                # succeeded here
                oldval = []
                try:
                    oldval = counter[stutime[3]]
                except:
                    pass
                oldval.append((stutime[0], time_st, time_en))
                counter[stutime[3]] = oldval
    return counter

if __name__ == '__main__':
    p = Prof()
    p.timelist = [(0, 9, 5+12),
                  (1, 9, 5+12),
                  (2, 8, 10),
                  (2, 12, 1+12)]

    s1 = Student()
    s1.timelist = [(0, 12, 2+12, "hw"),
                   (0, 4+12, 7+12, "class"),
                   (1, 0, 24, "exam")]
    s2 = Student()
    s2.timelist = [(0, 12, 2 + 12, "hw"),
                   (0, 3 + 12, 7 + 12, "class"),
                   (2, 8, 12, "hw")]

    res = start(p, [s1, s2])
    print(res)