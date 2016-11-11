import sys
import Pyro4
from jobs import Jobs

def main(argv):
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    jobs = Jobs()
    uri = daemon.register(jobs)
    ns.register("jobs", uri)

    daemon.requestLoop()

if __name__ == "__main__":
    main(sys.argv)