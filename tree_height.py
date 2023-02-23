# python3 tree_height.py
# 4 -1 4 1 1

import sys
import threading


def compute_height(n, parents):
    max_height = 0
    if n < 0:
        return max_height
    # Write this function
    child = n
    # Your code here
    for i in range(len(parents)):
        child = parents[child]
        max_height += 1
        if child == -1:
            break

    # print(max_height)
    return max_height if max_height > compute_height(n-1, parents) else compute_height(n-1, parents)


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
    values = map(int, values)
    values = list(values)

    # call the function and output it's result
    print("result: ", compute_height(elements_count - 1, values))
    
    # account for github input inprecision
    


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
