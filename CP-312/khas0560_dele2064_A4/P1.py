"""
------------------------------------------------------------
Program will read input file passing an argument to the 
program and output to question will be written on the 
console screen 
------------------------------------------------------------
Author: Sahil Khasnobish
        Emily De Leon
ID: 190990560
    129012064
Email: khas0560@mylaurier.ca
        dele2064@mylaurier.ca
__updated__ = "2022-03-04"
------------------------------------------------------------
"""
import sys 


input_file = open(sys.argv[1], 'r')

num_list = []

num_list_str = input_file.readline().strip()
num_list = num_list_str.split(",")

def get_data(input_file):
    open(input_file, 'r')
    num_list = []
    plus_signs_char = ''
    minus_signs_char = ''

    plus_signs = 0
    minus_signs = 0

    line = input_file.readline()
    num_list = line.split(line, ',')

    line = input_file.next()
    plus_signs_char = line.readline()

    line = input_file.next()
    minus_signs_char = line.readline()

    return num_list, plus_signs, minus_signs

def greedy_alg(numbers, plus_signs, minus_signs):

    plus_count = plus_signs
    minus_count = minus_signs

    output_str = ""
    output = []
    sum = numbers[0]
    num1 = sum
    for i in range(len(numbers)-1):
        if(numbers[i]<0):
            output_str += "("
            output_str += str(numbers[i])
            output_str += ")"
        else:
            output_str += str(numbers[i])
        num2 = numbers[i+1]
        num1 = sum

        if(plus_count>0) and (minus_count>0):

            a = num1 + num2 #5
            b = num1 - num2 #-17
            c = num2 - num1 #17

            if (a>=b and a>=c):
                output_str+=" + "
                sum = a
                plus_count-=1
            elif(b>=a and b>=c):
                output_str += " - "
                sum = b
                minus_count-=1
            elif(c>=b and c>=a):
                output_str += " - "
                sum = c
                minus_count-=1

        elif(plus_count==0) and (minus_count>0):

            a = num1 - num2
            b = num2 - num1

            if (a >= b):
                output_str += " - "
                sum = a
                minus_count -= 1
            else:
                output_str += " - "
                sum = b
                minus_count -= 1
        else:
            output_str += " + "
            a = num1 + num2
            sum = a
            plus_count -= 1

    output_str += str(numbers[-1])
    return sum, output_str

def main():
    numbers = [-6,11,-13,17,5]
    plus_signs = 1
    minus_signs = 3
    sum, output_str = greedy_alg(numbers, plus_signs, minus_signs)
    print(sum)
    print(output_str)
    print("=", end=" ")
    print(sum, end=" ")

main()


