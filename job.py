import random


class Job(object):

    def __init__(self):
        self.list = random.sample(range(1,10001), 10000)