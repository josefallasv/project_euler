#Problem 1: Multiples of 3 or 5

#create empty array and variable for sum of multiples
my_array = []
multiples_sum = 0

#find multiples of 3 or 5 below 1000
for i in range(1,1000):
    if(i%3==0 or i%5==0):
       my_array.append(i) 

#print values in array
#for i in range(0,len(my_array)):
#    print(my_array[i])

#perform sum of the multiples
for i in range (0,len(my_array)):
    multiples_sum+=my_array[i]

#print sum of multiples
print("the sum of multiples of 3 or 5 below 1000 is", multiples_sum)
