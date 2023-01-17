import datetime
import memory_profiler

def log (mess):
    with open("log.txt", "a") as logfile:
        logfile.write(str(datetime.datetime.now()) + "\t" + str(memory_profiler.memory_usage()) + "\t" + mess +"\n")