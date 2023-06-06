"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""
from data import Student
from my_queue import Queue
from copy import deepcopy

def compare_students(student1,student2):
    """
    -------------------------------------------------------
    Description:
        Compare two student objects
        Compare keys, then last name, then first name
        Return 1 if student1 > student2
        Return 2 if student1 < student2
        Return 0 if student1 == student2
        Return -1 if there is an error, which is if either input is not a student object
            In that case also print an error message
    Use: result = compare_students(student1,student2)
    -------------------------------------------------------
    Parameters:
        student1 - a student object (Student)
        student2 - a student object (Student)    
    Returns:
        result - 0/1/2/-1 (int)            
    -------------------------------------------------------
    """

    if not (isinstance(student1, Student) or not (isinstance(student2, Student))):
        print('Error(compare_students): invalid input parameter type')
        result = -1
    else:
        if student1.sid > student2.sid:
            result  = 1
        elif student2.sid > student1.sid:
            result = 2
        else:
            if student1.last > student2.last:
                result = 1
            elif student2.last > student1.last:
                result = 2
            else:
                if student1.first > student2.first:
                    result = 1
                elif student2.first > student1.first:
                    result = 2
                else:
                    result = 0
    return result
def remove_group(queue,num):
    """
    -------------------------------------------------------
    Description:
        Remove num items from a queue, and return it as a list
        if invalid queue or invalid num, print error message and return empty list
    Use: removed_items = remove_group(queue,num)
    -------------------------------------------------------
    Parameters:
        queue - a queue object containing arbitrary items (Queue)
        num - number of items to be removed from queue (int)
    Returns:
        removed_items - list containing copies of removed items (list)           
    -------------------------------------------------------
    """
    removed_items = []
    if not (isinstance(queue, Queue)):
        print('Error(remove_group): invalid input parameter type')
        removed_items = []
    elif not (isinstance(num, int)):
        print('Error(remove_group): invalid input parameter type')
        removed_items = []
    elif (num<0):
        removed_items = []
        print('Error(remove_group): invalid value for num')
    else:
        if num == 0:
            removed_items = []
        else:
            if not (queue.is_empty()):
                if num > len(queue):
                    for _ in range(len(queue)):
                        item = queue.remove()
                        removed_items.append(deepcopy(item))  
                else:
                    for _ in range(num):
                        item = queue.remove()
                        removed_items.append(deepcopy(item))
    return removed_items
def remove_batch(queue,year):
    """
    -------------------------------------------------------
    Description:
        Remove students enrolled in given year from a given queue
        Function process queue items sequentially:
        if year does not match, item is moved to rear of queue
        students removed are stored in a queue
    Use: batch_queue = remove_batch(queue,year)
    -------------------------------------------------------
    Parameters:
        queue - a queue object containing student objects (Queue)
        year - enrollment year (int)
    Returns:
        batch_queue - a queue containing students of same batch          
    -------------------------------------------------------
    """
    count = 0
    queue_list = []
    while not queue.is_empty():
        item = queue.remove()
        queue_list.append(deepcopy(item))
        count+=1
    
    for i in queue_list:
        queue.insert(deepcopy(i))
    
    batch_queue = Queue(100000000)
    if not (isinstance(queue, Queue)) or not (isinstance(year, int)):
        print('Error(remove_batch): invalid input parameter type')
        batch_queue = Queue()
    
    else:
        for n in queue_list:       
            if str(n.sid)[:4] == str(year):
                batch_queue.insert(deepcopy(n))
                queue.remove()
            else:
                queue.remove()
                queue.insert(deepcopy(n))  
    return batch_queue   

def priority_merge(queue1,queue2):
    """
    -------------------------------------------------------
    Description:
        Merge two queues into one main queue
        The front of the two queues is compared, the larger one is inserted first
        The process repeats until no more objects remain in both queues
        Further details of the merging is provided in the PDF file
    Use: q3 = proirity_merge(q1,q2)
    -------------------------------------------------------
    Parameters:
        queue1 - a queue containing student objects (Queue)
        queue2 - a queue containing student objects (Queue)
    Returns:
        queue3 - a queue containing student objects (Queue)            
    -------------------------------------------------------
    """
    queue3 = Queue(100000000)
    while not (queue1.is_empty()) or not (queue2.is_empty()):
        
        if queue1.is_empty():
            while not queue2.is_empty():
                student = queue2.peek()
                queue3.insert(student)
                queue2.remove()
        elif queue2.is_empty():
            while not queue1.is_empty():
                student = queue1.peek()
                queue3.insert(student)
                queue1.remove()
        else:  
            student1 = deepcopy(queue1.peek())
            student2 = deepcopy(queue2.peek())
            result = compare_students(student1,student2)
            if result == 1:
                queue3.insert(student1)
                queue1.remove()
            elif result == 2:
                queue3.insert(student2)
                queue2.remove()
            else:
                queue3.insert(student1)
                queue1.remove()          
                queue2.remove()
         
    return queue3

def shred_queue(queue,size):
    """
    -------------------------------------------------------
    Description:
        shreds a queue into several equal sized queues of given size.
        Items of the queue is distributed sequentially into the minoir queues.
        If given size is invalid, print error message and return empty list
        At the end of the shredding process the input queue should be restored.  
    Use: queue_list = shred_queue(queue,size)
    -------------------------------------------------------
    Parameters:
        queue - a queue containing arbitrary items (Queue)
        size - size of each mini queue (int)
    Returns:
        queues - a list containing mini queues (list)            
    -------------------------------------------------------
    """
    queue_list = []
    queues = []
    count1 = 0
    
    if not (isinstance(size,int)) or (size<=0) or (size>(len(queue))):
        print('Error(shred_queue): invalid shred size')
        queues = []
    else:
        while not queue.is_empty():
            queue_item = deepcopy(queue.peek())
            queue_list.append(deepcopy(queue_item))
            queue.remove()
        
        queue_list2 = deepcopy(queue_list)
        while not (queue_list == []):
            mini_queue = Queue(size)
            if len(queue_list) >= size:
                for i in range(size):
                    mini_queue.insert(queue_list[i])
                queues.append(deepcopy(mini_queue))
                count1 = size
            
                while count1!=0:
                    queue_list.remove(queue_list[count1-1])
                    count1-=1
            
            else:
                for n in range(len(queue_list)):
                    mini_queue.insert(queue_list[n])
                queues.append(deepcopy(mini_queue))
                
                
                for _ in range(len(queue_list)):
                    queue_list.clear()
          
                  
        for x in queue_list2:
            queue.insert(x)
            
    return queues