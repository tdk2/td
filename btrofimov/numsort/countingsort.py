

def countingsort(lst,k):
  blocks=[ 0 for i in range(k)]
  for i in lst:
    blocks[i-1] = blocks[i-1] + 1
  ret = []
  k = 0
  for elem in blocks:
    for i in range(elem):
     ret.append(k+1)
    k = k + 1
  return ret
  
print countingsort([100,5,65,32,27,18,1000,45,23],1000)