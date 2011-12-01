import math

class HashTable:
  
  
  def __init__(self):
    self.__func = self.__hashFunc
    self.__m = 1600
    self.__array = [ [] for i in range(self.__m)]
    
    
  def putPair(self, key, value):
    lst = self.__array[self.__func(key,self.__m)]
    lst.append( (key, value) )  


  def getValue(self,  key ):
    lst = self.__array[self.__func(key,self.__m)]
    for i in lst:
      if(i[0] == key):
        return i[1]
    return None
    
  def setFunc(self, newFunc):
    self.__func = newFunc  
  
  
  # mult method
  def __hashFunc(self,k,m):
    A = (math.sqrt(5)-1)/2
    return int(math.modf(math.modf(A*k)[0] * m)[1])
    

hash1 = HashTable()

hash1.putPair(234,"1")
hash1.putPair(23432444,"2")
hash1.putPair(234324,"3")
hash1.putPair(2344324,"4")
hash1.putPair(233334324,"5")
hash1.putPair(112344,"6")
hash1.putPair(237744324,"7")
hash1.putPair(23432488,"8")

#print hash1.array

print hash1.getValue(234324)