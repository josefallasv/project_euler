#Problem 1: Multiples of 3 or 5
#Link to problem: https://projecteuler.net/problem=1

#Create empty array for multiples and variable for sum of multiples
multiples = []
multiples_sum = 0

#Find multiples of 3 or 5 below 1000
for i in range(1,1000):
    if(i%3==0 or i%5==0):
       my_array.append(i) 

#Perform sum of the multiples
for i in range (0,len(my_array)):
    multiples_sum+=my_array[i]

#Print sum of multiples
print("the sum of multiples of 3 or 5 below 1000 is", multiples_sum)
