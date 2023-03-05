# python3 tree_height.py
# 4 -1 4 1 1
import sys
import threading
import numpy


def compute_height(n, parents):
    levels = {-1: 0}

    while n >= len(levels):
        for child, i in enumerate(parents):
            if i in levels:
                levels[child] = levels[i] + 1
    
    return max(levels.values())


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
