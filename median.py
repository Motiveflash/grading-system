#This programme reads a list of numbers for a user, sort the list, and find the median value

def find_median(numbers):
  #sorts the list of numbers
  numbers.sort() 
  numbers_len = len(numbers)
  mid = numbers_len % 2

  #if the list has an odd number of elements, the median is the middle number
  if mid == 1:
    return numbers[mid]
  #if the list has an even number of elements, the median is the average of the two middle numbers
  else:
    return (numbers[mid - 1] + numbers[mid]) // 2
  
#takes user input for a list of numbers
numbers = list(map(int, input("Enter numbers separated by space: ").split()))
median = find_median(numbers)
print("The median is", median)