def trace(list_name):
  """The function trace take all the index positions (a,a) and adds them up to calculate the trace"""
  k = 0
  for index_list,i in enumerate(list_name):
    for index_sublist,j in enumerate(i):
      if index_list == index_sublist:
        k = k + j
  return k

def upper_triangle(list_name):
  """The function upper_triangular take all the index positions (a,b), where a < b  and adds them up to calculate the  upper triangular total value"""
  q = 0
  for index_list,i in enumerate(list_name):
    for index_sublist,j in enumerate(i):
      if index_list < index_sublist:
        q = q + j
  return q

def lower_triangle(list_name):
  """The function lower_triangular take all the index positions (a,b), where a > b  and adds them up to calculate the  lower triangular total value"""
  p = 0
  for index_list,i in enumerate(list_name):
    for index_sublist,j in enumerate(i):
      if index_list > index_sublist:
        p = p + j
  return p
# A list is made called matrx with 100 odd integers, 
matrx = []
for i in range (100):
  k = 2 * i + 1
  matrx.append(k)
# next another empty list of 10 10 empty list is made called row and add to X.
X = []
for n in range(10):
  row = []
  X.append(row)
# The empty list X will be filled by using the odd intergers for each empty list within X.
count = 0
for i in range(0,10):
  count = count + 10
  X[i]=matrx[count-10:count]
print(X)
# print(trace.__doc__)
print(f"The trace of your matrix is X:{trace(X)}")
# print(upper_triangle.__doc__)
print(f"The upper trianglar of your matrix is X:{upper_triangle(X)}")
# print(lower_triangle.__doc__)
print(f"The lower trianglar of your matrix is X:{lower_triangle(X)}")