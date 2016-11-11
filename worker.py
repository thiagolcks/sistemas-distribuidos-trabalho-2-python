import Pyro4
import time
import sys

class Worker:

    def __init__(self):
        start_time = time.time()

        jobs = Pyro4.Proxy("PYRONAME:jobs")
        job = jobs.getJob()
        while job is not None:
            self.sort(job)
            jobs.setJob(job)
            job = jobs.getJob()

        print("--- %s seconds ---" % (time.time() - start_time))

    def sort(self, alist):
        for passnum in range(len(alist)-1, 0, -1):
            for i in range(passnum):
                if alist[i]>alist[i+1]:
                    temp = alist[i]
                    alist[i] = alist[i+1]
                    alist[i+1] = temp

if __name__ == "__main__":
    worker = Worker()