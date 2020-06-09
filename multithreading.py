'''
The purpose of this program is to test the efficiency of multithreading
This program will time how long it takes to run 2 for loops adding 1+x 1000000 in order and compare it with
the results of running 2 for loops counting adding 1+x 1000000 times while multithreading
'''

# import libraries
import time
import threading


# test time of 2 for loops
start_time = time.time()
y=0
for x in range(1000000):
    y=y+x
y=0
for x in range(1000000):
    y=y+x

regular= 'Regular: ' + str(time.time() - start_time)



# test with threading
def for_one():
    y=0
    for x in range(1000000):
        y=y+x

def for_two():
    y=0
    for x in range(1000000):
        y=y+x

start_time = time.time()
t1 = threading.Thread(target=for_one) 
t2 = threading.Thread(target=for_two)

# starting thread 1 
t1.start() 
# starting thread 2 
t2.start() 

# wait until thread 1 is completely executed 
t1.join() 
# wait until thread 2 is completely executed 
t2.join()


# results
threaded= 'Threaded: ' + str(time.time() - start_time)

print(regular)
print(threaded)