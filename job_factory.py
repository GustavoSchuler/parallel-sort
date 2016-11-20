import Pyro4
from job import Job


@Pyro4.expose
class JobFactory:

    jobs_todo = []
    jobs_done = []

    def __init__(self):
        self.jobs_todo = [Job().list for i in range(10)]

    def getJob(self):
        return self.jobs_todo.pop()

    def jobDone(self, job):
        self.jobs_done.append(job)

