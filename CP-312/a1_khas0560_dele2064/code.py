"""
CP312B - Algorithm Design/Analysis I
Sahil Khasnobish - 190990560
Emily De Leon - 129012064
Assignment 1
Jan 14, 2022
"""
import time

def question1(n):
    initial_time = time.time()

    sum = 0 #O(1)
    for i in range(n): #O(n)
        sum+=1          #O(1)
    #Answer: O(n)
    final_time = time.time()

    total_time = final_time - initial_time
    return total_time


def question2(n):
    initial_time = time.time()

    sum = 0  # O(1)
    for i in range(n):#
        for j in range(n):#O(n)
            sum += 1 #O(1)

    final_time = time.time()

    total_time = final_time - initial_time
    return total_time


def question3(n):
    initial_time = time.time()

    sum = 0  # O(1)
    for i in range(n):#O(n^3)
        for j in range(n*n):#O(n^2)
            sum += 1#O(1)

    final_time = time.time()

    total_time = final_time - initial_time
    return total_time


def question4(n):
    initial_time = time.time()

    sum = 0  # O(1)
    for i in range(n):#O(n^2)
        for j in range(i):#O(n)
            sum += 1#O(1)

    final_time = time.time()

    total_time = final_time - initial_time
    return total_time


def question5(n):
    initial_time = time.time()

    sum = 0  # O(1)
    for i in range(n):#O(n^4)
        for j in range(i*i):#O(n^3)
            for k in range(j):#O(n)
                sum += 1#O(1)

    final_time = time.time()

    total_time = final_time - initial_time
    return total_time

def question6(n):
    initial_time = time.time()

    sum = 0  # O(1)
    for i in range(n):#O(n)
        for j in range(i*i): #(n^2)
            if(j%i==0):
                for k in range(j): #O(n)
                    sum += 1 #O(1)

    final_time = time.time()

    total_time = final_time - initial_time
    return total_time


n = 50;

list = [10,20,30,40,50]



print("\nQuestion1 Time: \n", question1(n))
print("\nQuestion2 Time: \n", question2(n))
print("\nQuestion3 Time: \n", question3(n))
print("\nQuestion4 Time: \n", question4(n))
print("\nQuestion5 Time: \n", question5(n))
print("\nQuestion6 Time: \n", question6(n))

