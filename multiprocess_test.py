#importing modules
import multiprocessing
import time

#define function to calculate the square value of a number
def calculate_square(nums):#defining the function
    for n in nums: #for loop 
        time.sleep(5)#essentially we slow down the process so we can see the output
        print('square ' + str(n*n) ) #print the calculated square of a number

#define function to calculate the cube value of a number
def calculate_cube(nums):
    for n in nums:
        time.sleep(5)
        print('cube ' + str(n*n*n) )

#if so we can see if it is the main script
##if __name__ == '__main__': #unnecessary in hindsight
arrs=[2,3,8,9]
p1 = multiprocessing.Process(target=calculate_square, args=(arrs,))
p2 = multiprocessing.Process(target=calculate_cube, args=(arrs,))

p1.start()#start multiprocess 1
p2.start()#start multiprocess 2
    
p1.join
p2.join
print(p1)
print(p2)1
    
print("Done")


#using map reduce
from multiprocessing import Pool


def f(n):
    return n*n

p = Pool(processes=3)
result = p.map(f,[1,2,3,4,5])
for n in result:
    print(n)

#using multithread
import threading
t=time.time()

t1=threading.Thread(target=calculate_square, args=(arrs,))#just like the others target=function, args=arguments of function
t2=threading.Thread(target=calculate_cube, args=(arrs,))#same thing but or cube

t1.start#start process for thread 1
t2.start#start process for thread 2

t1.join()#stop thread 1
t2.join()#stop thread 2
