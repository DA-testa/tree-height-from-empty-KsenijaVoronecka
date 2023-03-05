# python3 tree_height.py
# 4 -1 4 1 1
import sys
import threading
import numpy

def compute_height(n, parents):
    counted = [0] * n
    levels = [0] * n

    def find_level(place):
        if parents[place] == -1:
            counted[place] = 1
            return 1
        
        if counted[place] == 1:
            return levels[place]
        
        counted[place] = 1
        levels[place] = find_level(parents[place]) + 1

        return levels[place]
    
    for place in range(n):
        if counted[place] != 1:
            levels[place] = find_level(place)

    return max(levels)


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
    values = list(map(int, values.split()))
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
