

def radixsort(lst,k):
  dl = 1
  for i in range(k):
    blocks=[ [] for i in range(10)]
    
    for elem in lst:
      idx = (elem/dl)%10
      blocks[idx].append(elem)
    dl = dl * 10  
    lst = []
    for elem in blocks:
      lst = lst + elem
  return lst

print radixsort([100,5,65,32,27,18],3)