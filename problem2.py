#Problem 2: Even Fibonacci Numbers
#Link to problem: https://projecteuler.net/problem=2

sequence=[1,2]
sum_even_terms=0
counter=0

#Generate Fibonacci sequence up to (but not including) the first value that exceeds 4 million
while True:
    sequence.append(sequence[counter]+sequence[counter+1])
    counter=counter+1
    if sequence[len(sequence)-1]>=4000000:
        sequence.pop()
        break

#Sum even-values in sequence
for i in range(0,len(sequence)):
    if sequence[i]%2==0:
        sum_even_terms+=sequence[i]

#Print sum of the even-values in sequence
print("the sum of the even-values in sequence is",sum_even_terms)
    