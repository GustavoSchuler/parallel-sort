import Pyro4


class Worker(object):

    def __init__(self):
        factory = Pyro4.Proxy("PYRONAME:factory")

        job = factory.getJob()
        print(job)


def main():
    Worker()

if __name__ == '__main__':
    main()