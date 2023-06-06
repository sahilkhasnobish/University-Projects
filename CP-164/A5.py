"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""

from pqueue import pQueue
from copy import deepcopy
class Process:
    def __init__(self,PID,time,arrival):
        assert len(str(PID))>0 or time<0 or PID<0, "‘Invalid PID’, ‘Invalid time’ and ‘Invalid arrival’"
        self.PID = PID
        self.time = time
        self.arrival = arrival
    
    def __str__(self):
        return ('[{}]({},{})'.format(self.arrival, self.PID, self.time))
    
    def key(self):
        return self.PID
    
    def __eq__(self,other):
        return self.arrival == other.arrival and self.time == other.time and self.PID == other.PID
    
    def __ne__(self,other):
        return not self == other
    
    def __gt__(self,other):
        if self.arrival > other.arrival:
            return True
        elif self.arrival < other.arrival:
            return False
        elif self.time > other.time:
            return True
        elif self.time < other.time:
            return False
        elif self.PID > other.PID:
            return True 
        return False 
    
    def __ge__(self,other):
        return self > other or self  == other
    
    def __lt__(self,other):
        if self.arrival < other.arrival:
            return True
        elif self.arrival > other.arrival:
            return False
        elif self.time < other.time:
            return True
        elif self.time > other.time:
            return False
        elif self.PID < other.PID:
            return True 
        return False
    
    def __le__(self,other): 
        return self < other or self == other

def read_processes(filename):
    inFile = open(filename, 'r')
    processes = []
    for i in inFile:
        strip_line = i.strip()
        process_info1 = strip_line.split(']')
        process_info2 = strip_line.split(',')
        arrival = int(process_info1[0][1:])
        time = int(process_info2[1][:-1])
        get_pid = (process_info2[0].split('('))
        PID = int(get_pid[1])
        item = Process(PID,time,arrival)
        processes.append(deepcopy(item))
   
    return processes

def schedule(filename,scheduler_type):
    if scheduler_type == 'FIFO':
        processes = read_processes(filename)
        schedule_FIFO(processes)
    elif scheduler_type == 'SJF':
        processes = read_processes(filename)
        schedule_SJF(processes)
    else:
        print('Error, scheduler type not FIFO or SJF')
    return

def schedule_FIFO(processes):
    queue = pQueue(10000000000000, 'L')
    for i in processes:
        queue.insert(deepcopy(i))
    timer = 0
    print('[Timer:{}]: Starting FIFO Scheduler'.format(timer))
    timer +=1
    while not queue.is_empty():
        item = queue.peek()
        if timer<item.arrival:
            print('[Timer:{}]: idle'.format(timer))
            timer+=1
        else:
            print('Fetching Process: {}'.format(item))
            for i in range(item.time):
                print('[Timer:{}]: {}'.format(timer, item.PID))
                timer+=1
            queue.remove()
    print('[Timer:{}]: Closing FIFO Scheduler'.format(timer))            
    return

def schedule_SJF(processes):
    process_list = []
    queue = pQueue(10000000000000, 'L')
    for i in processes:
        queue.insert(deepcopy(i))
    timer = 0
    print('[Timer:{}]: Starting SJF Scheduler'.format(timer))
    timer +=1
    while not queue.is_empty():
        min_val = queue.peek().time
        sorted_process = queue.peek()
        if timer<queue.peek().arrival:
            print('[Timer:{}]: idle'.format(timer))
            timer+=1
        else:
            while not queue.is_empty() and timer >= queue.peek().arrival:
                item = queue.remove()
                process_list.append(deepcopy(item))
                if item.time < min_val:
                    min_val = item.time
                    sorted_process = item

            print('Fetching Process: {}'.format(sorted_process))
            process_list.remove(sorted_process)
            for i in range(sorted_process.time):
                print('[Timer:{}]: {}'.format(timer, sorted_process.PID))
                timer+=1
            for x in process_list:
                queue.insert(x)

            process_list = []

    print('[Timer:{}]: Closing SJF Scheduler'.format(timer))            
    return
