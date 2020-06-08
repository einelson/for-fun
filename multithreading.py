'''
The purpose of this program is to test the efficiency of multithreading
This program will time how long it takes to run 2 for loops counting from 1-1000 in order and compare it with
the results of running 2 for loops counting to 1000 while multithreading
'''

# import libraries
import time
import threading


# test time of 2 for loops
start_time = time.time()
for x in range(10000):
    print(x)
for x in range(10000):
    print(x)

regular= 'Regular: ' + str(time.time() - start_time)



# test with threading
def for_one():
    for x in range(10000):
        print(x)

def for_two():
    for x in range(10000):
        print(x)

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