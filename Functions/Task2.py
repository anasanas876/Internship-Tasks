# Task 2
def sum_average(numbers):
 
 total=sum(numbers)
 average=total/len(numbers)
 return total, average
numbers=[2,3,1,4,3,44,33,32,2,1]

print(sum_average(numbers))