"""
-------------------------
# Student Name: Sahil Khasnobish
# Student ID: 190990560
# Student email: khas0560@mylaurier.ca
#-------------------------
"""
from my_queue import Queue
from stack import Stack
from copy import deepcopy
MAX_SIZE = 100

def reverse_stack(stack):
    """
    -------------------------------------------------------
    Description:
        Reverse a stack using a queue
    Use: reverse_stack(stack)
    -------------------------------------------------------
    Parameters:
        stack - a stack of items (Stack)
    Returns:
        No returns
    -------------------------------------------------------
    """
    queue = Queue(MAX_SIZE)
    while not ((stack).is_empty()):
        item = stack.pop()
        queue.insert(item)
    while not queue.is_empty():
        queue_item = queue.peek()
        stack.push(queue_item)
        queue.remove()
    return

def queue_to_file(queue,filename):
    """
    -------------------------------------------------------
    Description:
        Writes students stored in a queue into given file.
        Queue becomes empty after writing
        Each student record appears in a separate line in file
        using the following format:
        [sid,first last]
    Use: queue_to_file(queue,filename)
    -------------------------------------------------------
    Parameters:
        queue - A queue containing students objects (Queue)
        filename - name of input file (str)
    Returns:
        No return
    -------------------------------------------------------
    """
    outFile = open(filename, 'w')
    while not queue.is_empty():
        student = queue.peek()
        student_str = ('[{},{} {}]\n'.format(student.sid, student.first, student.last))
        outFile.write(deepcopy(str(student_str)))
        queue.remove()
        outFile.close()
    return

def lshift_queue(queue,shifts):
    """
    -------------------------------------------------------
    Description:
        Shifts the queue to left by putting the front to the rear
        and repeating that as many as #shifts
        prints an error if shifts is negative or if queue is empty
    Use: lshift_queue(queue,shifts)
    -------------------------------------------------------
    Parameters:
        queue - A queue containing arbitrary objects (Queue)
        shifts - number of shifts to make the right(int)
    Returns:
        No returns
    -------------------------------------------------------
    """
    
    
    if queue.is_empty():
        print('Error(lshift_queue): Queue is empty')
    elif shifts<0:
        print('Error(lshift_queue): Invalid shifts value. Should be non-negative')
    else:
        if (len(queue))>shifts:
            count = 0
            while count != shifts:
                item = queue.peek()
                item2 = deepcopy(item)
                queue.remove()
                queue.insert(deepcopy(item2))
                count+=1
    return

def rshift_queue(queue,shifts):
    """
    -------------------------------------------------------
    Description:
        Shifts the queue to right by putting the rear to the front
        and repeating that as many as #shifts
        prints an error if shifts is negative or if queue is empty
    Use: rshift_queue(queue,shifts)
    -------------------------------------------------------
    Parameters:
        queue - A queue containing arbitrary objects (Queue)
        shifts - number of shifts to make the right(int)
    Returns:
        No returns
    -------------------------------------------------------
    """
    queue_list = []
    if queue.is_empty():
        print('Error(lshift_queue): Queue is empty')
    elif shifts<0:
        print('Error(lshift_queue): Invalid shifts value. Should be non-negative')
    else:
        new_shifts = len(queue) - shifts
        new_shifts = new_shifts%(len(queue))
        lshift_queue(queue, new_shifts)
    return