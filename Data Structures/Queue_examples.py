from BasicDS import Queue

def hotPotato(namelist, num):
    simque = Queue()
    for name in namelist:
        simque.enqueue(name)
    
    while simque.size() > 1:
        for i in range(num):
            simque.enqueue(simque.dequeue())
        
        simque.dequeue()
    
    return simque.dequeue()

# print(hotPotato(["Bill","David","Susan","Jane","Kent","Brad"],5))

# Computer lab printing tasks simulation
# Printer tracks time remaining for task, busy status and amount of time needed for task
class Printer:
    """
    Queue linear data structure

    Instance variables:
        None
    """
    
    def __init__(self, ppm):
        self.pageRate = ppm
        self.currentTask = None
        self.timeremain = 0
    
    def tick(self):
        if self.currentTask != None:
            self.timeremain = self.timeremain - 1
            if self.timeremain <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask != None:
            return True
        else:
            return False
    
    # set the current task to the dequeued task
    # set time remaining based on the number of pages and the page rate
    def startNext(self, newTask):
        self.currentTask = newTask
        self.timeremain = newTask.getPages() * 60 / self.pageRate

import random

class Task:
    def __init__(self, time):
        self.timestamp = time
        self.pages = random.randrange(1,21)
    
    # records a timestamp of when the task was placed in the queue
    def getStamp(self):
        return self.timestamp
    
    def getPages(self):
        return self.pages
    
    def waitTime(self,currentTime):
        return currentTime - self.timestamp

def simulation(numSec, pagePerMin):

    labprinter = Printer(pagePerMin)
    printQueue = Queue()
    waitingtimes = []

    for currentSec in range(numSec):

        if newPrintTask():
            task = Task(currentSec)
            printQueue.enqueue(task)
        
        if (not labprinter.busy()) and (not printQueue.isEmpty()):
            nextTask = printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSec))
            labprinter.startNext(nextTask)
        
        labprinter.tick()
    
    averageWait = sum(waitingtimes)/len(waitingtimes)
    print("Avg wait {0:6.2f} secs {1:3d} tasks remaining.".format(averageWait, printQueue.size()))
    return averageWait

def newPrintTask():
    num = random.randrange(1,91)
    if num == 90:
        return True
    else:
        return False


Avg_Total_waitTime = []
for i in range(10):
    time = simulation(3600,5)
    Avg_Total_waitTime.append(time)
print(sum(Avg_Total_waitTime)/len(Avg_Total_waitTime))
