import Pyro4
from job_factory import JobFactory


class Server:

    def __init__(self):
        daemon = Pyro4.Daemon()
        ns = Pyro4.locateNS()

        factory = JobFactory()

        uri = daemon.register(factory)
        ns.register("factory", uri)

        print("Server is ready.")
        daemon.requestLoop()


def main():
    Server()

if __name__ == '__main__':
    main()