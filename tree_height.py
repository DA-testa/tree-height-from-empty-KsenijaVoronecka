# python3 tree_height.py
# 4 -1 4 1 1
import sys
import threading
import numpy


def compute_height(n, parents):
    max_height = 0
    level_array = numpy.zeros(n, dtype='i')
    elements_array = numpy.zeros(n, dtype='i')

    # Write this function
    for child in range(n):

        if elements_array[child] == 1:
            continue
        
        steps_array = []
        # Your code here
        while True:
            
            if level_array[child] != 0:
                level_array[steps_array[len(steps_array)-1]] = level_array[steps_array[len(steps_array)-1]] + level_array[child]
                break

            elements_array[child] = 1
            level_array[child] = 1
            
            if len(steps_array) != 0:
                for step in range(len(steps_array)):
                    level_array[steps_array[step]] += 1

            # steps_array = numpy.append(steps_array, child)
            steps_array.append(child)
            child = parents[child]

            if child == -1:
                break

    # max_height = max(level_array)
    # max_height = 0
    # for i in range(len(level_array)):
    #     if level_array[i] > max_height:
    #         max_height = level_array[i]
 
    return max(level_array)


def main():
    # implement input form keyboard and from files
    command = input()

    if "I" in command:
        print("Enter a number of elements: ")
        # input number of elements
        elements_count = int(input())
        # input values in one variable
        print("Enter values: ")
        values = input()

    elif "F" in command:
        # let user input file name to use, don't allow file names with letter a
        print("Enter the file name: ")
        fileName = input()

        if "a" in fileName:
            print("wrong file name")
            return
        
        filePath = "./test/" + fileName
        with open(filePath, mode="r") as fail:
            # input number of elements
            elements_count = int(fail.readline())
            # input values in one variable
            values = fail.readline()

    else:
        print("error")
        return

    # separate values with space, split these values in an array
    values = values.split()
    values = list(map(int, values))
    values = numpy.array(values)

    # call the function and output it's result
    print("result: ", compute_height(elements_count, values))
    
    # account for github input inprecision
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
