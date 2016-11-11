import Pyro4
from random import sample

@Pyro4.expose
class Jobs(object):

    jobs = []
    jobsDone = []
    jobNumber = 10

    def __init__(self):
        self.createJobs()

    def getJob(self):
        return self.jobs.pop(0) if self.jobs else None

    def setJob(self, job):
        self.jobsDone.append(job)
        print(job[:100])

    def createJobs(self):
        self.jobs = [sample(range(0, 10000), 10000) for _ in range(self.jobNumber)]