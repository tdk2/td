import math
import random
import utils

# k is non negative integer
# m should not be power of two
def divisionHash(k, m):
    return k % m

# k is nonnegative integer
# for convenience purpose, m can be power of two
# A should belong to (0, 1)
def multiplyHash(k, m, A=((5**0.5-1)/2)):
    return int(m*(k*A % 1.0))

# k is nonnegative integer
# m can be same as in multiply_hash
# p is a prime number which is large enough, i.e. more than any key in hash table
# a belongs to {1, 2, ..., p-1}, b belongs to {0, 1, ..., p-1}
# a universal hash function set can be built using ordinal_hash functions:
#    Hp,m(k) = {ordinalHash(_,_,_,a,b)} for each a and b
def ordinalHash(k, m, p, a, b):
    return ((a*k + b) % p) % m

# get a hash function from universal set.
# a and b are generated randomly
def getHashFunctionFromUniversalSet(p):
    a, b = utils.Random(1, p-1), utils.Random(0, p-1)
    return lambda k, m: ordinalHash(k, m, p, a, b)
    
# h(k, i) = (h'(k) + i) mod m
def linearProbing(hashFunc, k, m, i):
    return (hashFunc(k, m) + i) % m

# h(k, i) = (h'(k) + c1*i + c2*i^2) mod m
# c1 and c2 must be != 0
def squareProbing(hashFunc, k, m, i, c1 = 0.5, c2 = 0.5):
    return (hashFunc(k, m) + int(c1*i + c2*i*i)) % m

# h(k, i) = (h1(k) + i*h2(k)) mod m
# Two auxiliary hash functions are used here
def doubleHashProbing(hashFuncs, k, m, i):
    if len(hashFuncs) < 2:
        raise ValueError("hashFuncs mush have at least two items")
    return (hashFuncs[0](k, m) + i*hashFuncs[1](k, m)) % m

class OpenAddressHashTable:
   def __init__(self, m, HashFunction):
      self.m = m
      self.HashFunction = HashFunction
      self.Table = [None]*m
#	

if __name__=="__main__":
    #funcs = [division_hash, multiply_hash]
    #print map(lambda f: f(100, 12), funcs)

    # uncomment the line below if you need obtain the same results each run
    random.seed(2)

    m = 64
    p = 117
    k = 3
    ht = OpenAddressHashTable(m, squareProbing( getHashFunctionFromUniversalSet(p)))
    #aux_hashs = [getHashFunctionFromUniversalSet(p) for x in xrange(2)]
    #f = lambda k, m: ordinalHash(k, m, p, 3, 4)
    f = getHashFunctionFromUniversalSet(p)
    aux_hashs = [f, lambda k, m: 1 + (k % (m-1))]
    myHash = lambda k, i: doubleHashProbing(aux_hashs, k, m, i)
    #print [myHash(k, i) for i in xrange(0, m)]
    print [0.5*i*i + 0.5*i for i in xrange(m)]
    i, j = 0, 0
    for x in xrange(m):
        print i,
        j = j+1
        i = (i + j) % m
           


    
    #print [f(k, m), f(k, m), myHash(k, 0), myHash(k, 0)]
    #print doubleHashProbing([getHashFunctionFromUniversalSet(p) for x in xrange(2)], 8, m, 1)
    #print squareProbing(getHashFunctionFromUniversalSet(p), 8, m, 1)
    #print map(lambda k: multiplyHash(k, m), [61, 62, 63, 64, 65])

