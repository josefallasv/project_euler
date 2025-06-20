#Problem 3: Largest Prime Factor
#Link to problem: https://projecteuler.net/problem=3

number=600851475143
largest_prime_factor=0

#Check whether the input number is prime; return True if it is, otherwise return False
def prime(input: int):
    factors=[]
    for i in range(1,input+1):
        if input%i==0:
            factors.append(i)
    if len(factors)==2:
       return True
    else:
        return False
    
#Find all prime factors of input number and store longer prime factor in variable
for i in range(2,number):
    if number%i==0 and prime(i):
        largest_prime_factor=i
        print (largest_prime_factor)

print(largest_prime_factor)