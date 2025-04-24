l = [2, 4, 1, 0, 5, 3, 6]

def sort_list_naive(l):
  nlen = len(l)
	
  for i in range(0, nlen):
    idx = i
    for j in range(i+1, nlen):
      if l[idx] > l[j]:
        idx = j
    l[i], l[idx] = l[idx], l[i]
  return l
	
print(sort_list_naive(l))
