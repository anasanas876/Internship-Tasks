# Task 1
def is_prime(num):
    for i in range(2,num):
     if (num % i==0):
        
        return "Number is not prime"
     return "Number is prime"
print(is_prime(7))
    

     