#This code was partially completed in class on 1/22/2020
import time
import sys

WEIGHT = 200
cache = {}
CACHEHITS = 0
FUNCTIONCALLS = 0

def weightOn(r,c):
    
    global FUNCTIONCALLS
    FUNCTIONCALLS += 1

    if (r,c) in cache:
        global CACHEHITS
        CACHEHITS += 1
        return cache[(r,c)]
    if r == 0:
        result = 0
    elif c == 0:
        result = (WEIGHT + weightOn(r-1, c))/2.0
    elif c == r:
        result = (WEIGHT + weightOn(r-1 ,c-1 ))/2.0
    else:
        result = (WEIGHT*2 + weightOn(r-1,c-1) + weightOn(r-1, c))/2.0
    
    cache[(r,c)] = result
    return result



def main():
    rows = int(sys.argv[1]) #use the command line arguments to pull in the number of rows
    print()
    start = time.perf_counter()

    for row in range(rows):
        for col in range(row + 1): 
            print(f'{weightOn(row, col):.2f}', end = ' ')
        print()
    stop = time.perf_counter()
    print('Elapsed time:', stop-start, 'seconds')
    print('Number of Cache Hits: ', CACHEHITS)
    print('Number of Function Calls: ', FUNCTIONCALLS)

if __name__ == "__main__":
    main()


### Four Cases
# 1. r = 0  (0,0) Base Case. Where we will stop calling the function. 
# 2. c = 0 
# 3. r = c
# 4. r > c