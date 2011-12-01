import math

class HashTable:
  
  # constructor takes  just one parameter: recursion level value, for user instances it should be zero  
  def __init__(self,level):
    self.__func = self.__hashFunc
    self.__m = 160
    self.__A = (math.sqrt(5)-1)/2
    self.__level = level
    self.__array = [ [0,None] for i in range(self.__m)]
    
    
  # method allows to put value into hash.
  def putPair(self, key, value):
    elem = self.__array[self.__func(key,self.__m)]
    # if elem is just single pair
    if(elem[0]==0):
      elem[1] = (key, value)
      elem[0] = 1
    # if current recursion level is less then 3  then one more inner HashTable instance will be used
    elif(self.__level < 3):
      if(elem[0]!=2):
        tmp = elem[1]
        elem[0]= 2
        elem[1] = HashTable(self.__level+1)
        elem[1].setA(self.__A/2)
        # add previous elem
        elem[1].putPair(tmp[0],tmp[1])
      # add new elem
      elem[1].putPair(key,value)
    #otherwise  usual list will be created
    else:
      if(elem[0]!=5):
        elem[0] = 5
        elem[1] = [elem[1]]
      elem[1].append( (key, value) )
       
  # method allows to retreive value by key from hash    
  def getValue(self,  key ):
    elem = self.__array[self.__func(key,self.__m)]
    
    if(elem[0]==0):
      return None
    if(elem[0]==1):
      return elem[1][1]
    if(elem[0]==5): 
      for i in elem[1]:
        if(i[0] == key):
          return i[1]
    if(elem[0]==2):
      return elem[1].getValue(key)
    return None
    
  # method allows to change hash function, set by default    
  def setFunc(self, newFunc):
    self.__func = newFunc  
  
  # method allows to change A parameterm it used by inner HashTAble instances
  def setA(self, A):
    self.__A = A
  
  # internal default hash function - implementation of  Mult algo
  def __hashFunc(self,k,m):
    return int(math.modf(math.modf(self.__A*k)[0] * m)[1])

    
if __name__=="__main__":

  hash1 = HashTable(0)
  for i in range(100000):
    hash1.putPair(i,"a%d"%i)
  
  hash1.putPair(234,"1")
  hash1.putPair(23432444,"2")
  hash1.putPair(3444324,"3")
  hash1.putPair(2344324,"4")
  hash1.putPair(233334324,"5")
  hash1.putPair(112344,"6")
  hash1.putPair(237744324,"7")
  hash1.putPair(23432488,"8")

  #print hash1.array
  print "hash has been filled"
  print hash1.getValue(3444324)