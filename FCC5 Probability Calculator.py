import copy
import random


class Hat:
    def __init__(self, **args):
        self.args = args
        dic = dict(self.args)
        self.dic = dic
        contents = []
        for i in dic:
            for j in range(dic[i]):
                contents.append(i)
        self.contents = contents

    def draw(self, pick):
        pick = int(pick)
        ran = []
        self.ran = ran
        if pick <= len(self.contents):
            for i in range(pick):
                self.ran.append(self.contents.pop(self.contents.index(random.choice(self.contents))))
        else:
            ran = self.contents
            self.contents = []
        return ran


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n_list = []
    check = []
    for ball in expected_balls:
        for i in range(expected_balls[ball]):
            check.append(ball)
    num_pass = 0
    orig = hat.contents
    for n in range(num_experiments):
        hat.contents = []
        hat.contents.extend(orig)
        # print(hat.contents)
        # print(hat.draw(num_balls_drawn))
        n_list = hat.draw(num_balls_drawn)
        n_len = len(n_list)
        # print(n_len, n_list)
        for ball in check:
            if ball in n_list:
                ind1 = n_list.index(ball)
                n_list.pop(ind1)
            if len(n_list) == n_len - len(check):
                num_pass += 1
        # print(num_pass)
    prob = num_pass / int(num_experiments)
    hat.contents = []
    hat.contents.extend(orig)
    return prob


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red": 2, "green": 1},
                         num_balls_drawn=5,
                         num_experiments=2000)


