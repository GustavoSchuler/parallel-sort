import Pyro4
from time import time


class Worker(object):

    def __init__(self):
        t = time()

        factory = Pyro4.Proxy("PYRONAME:factory")
        job = factory.getJob()

        while job is not None:
            job_time = time()
            self.bubblesort(job)
            print("Job finished in " + str(time() - job_time) + " seconds.")
            factory.jobDone(job)
            job = factory.getJob()

        print("\nNo more jobs to do.\nTotal worked time: " + str(time() - t))

    def bubblesort(self, list):
        for i in range(len(list)):
            for k in range(len(list) - 1, i, -1):
                if (list[k] < list[k - 1]):
                    tmp = list[k]
                    list[k] = list[k - 1]
                    list[k - 1] = tmp


def main():
    Worker()

if __name__ == '__main__':
    main()