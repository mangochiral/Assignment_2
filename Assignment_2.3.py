def fabonacci(n):
  """A function is made called fabonnaci to recursively generate fabonnaci numbers"""
  if (n == 0 or n == 1):
    return n
  else:
    return fabonacci(n-2) + fabonacci(n-1)

print(fabonacci.__doc__)
################################################################################################################################
# Takes input from user
try:
  a = int(input("Enter the number: "))
# Generate a list lst_1 of fabonnaci number.
  lst_1 = []
  for i in range (a):
    x = fabonacci(i)
    lst_1.append(x)

  print(f'The list of fabonnaci numbers are: {lst_1}\n')
# A second list is made where the index position 0 will have item as 1. And rest of index will have item as quotient from previous fabonnaci list by diving with corresponding items
  q2 = 1
  lst_2 = []
  lst_2.append(q2)
  # for index, t in enumerate(lst_1):
  #   if index <= len(lst_1) - 3:
  #     y = (lst_1[index+2]/lst_1[index+1])
  #     lst_2.append(y)
  for ind in range(2, len(lst_1)):
    lst_2.append(lst_1[ind]/lst_1[ind - 1])

  print(f'The list of quotient of fabonnaci numbers are: {lst_2} \n')
# A second list is made where the index position 0 will have item as 0. And rest of index will have item as difference from previous quotient list by subtraction with corresponding items
  q3 = 0
  lst_3 = []
  lst_3.append(q3)
  for index,t in enumerate(lst_2):
    if index <= len(lst_2)-3:
      x = (lst_2[index+2]-lst_2[index+1])
      lst_3.append(x)

  print(f'The list of quotient of fabonnaci numbers are:{lst_3}')
except ValueError:
  print('The value entered was incorrect.Kindly supply integer!!')


