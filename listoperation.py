'''Assignment No:4
To accept N numbers from user. Compute and display maximum in list, minimum in 
list,sum and average of numbers using built-in function.'''

try:
 n = int(input("Enter no of elements: "))
 nos_list = []    # nos_list list is created
 for i in range(n):    # for loop
  num = int(input("Enter no: "))
  nos_list.append(num)  # numbers are added in nos_list list
 maxNo = max(nos_list)   # maximum number in list
 minNo = min(nos_list)   # minimum number in list
 sumNos = sum(nos_list)   # sum of numbers in list
 average = sumNos/len(nos_list) # average of numbers in list
 print('Max no is ',maxNo)
 print('Min no is ',minNo)
 print('Count: ',len(nos_list)) # length of list
 print('Sum of nos is ',sumNos)
 print('Average of nos is ',average)
except ValueError:
 print('Enter n and all elements as integer.')
