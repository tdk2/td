

def blocksort(lst,a,b):
  delta = float(b-a)/len (lst)
  k = 0
  blocks=[ [] for i in range(len(lst))]
  for elem in lst:
    idx = int((elem-a)/delta)
    blocks[idx].append(elem)
    k=k+1
  ret = []
  for  k in range(len(blocks)):
    if (len(blocks[k])>1):
      a1 = a+k*delta
      b1 = a+(k+1)*delta
      blocks[k] = blocksort(blocks[k],a1,b1)
    ret = ret+blocks[k]
  return ret

print blocksort([0.1,0.2,0.3,0.4,0.5,0.6,0.63,0.62],0,1)