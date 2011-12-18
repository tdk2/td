import os, sys, string
sys.path.append(sys.path[0] + '/../hash')
import utils

Base = 256
Q = 22111

# a hash
def rollingHash(text, base, q):
    hash = 0
    for char in text:
        hash = (base*hash + ord(char)) % q
    return hash

# returns hash of 'moved window'
# bm is actually (b ^ (m-1) ) mod q
def nextRollingHash(prevHash, outChar, inChar, base, bm, q):
    return (base*(prevHash - ord(outChar)*bm) + ord(inChar)) % q

# returns the same value as math.pow(a, n) mod q, but more efficiently
def pow_by_mod(a, n, q):
    result = 1
    for x in xrange(n):
        result = (result*a) % q
    return result

# wrapper around == operator. For debug purpose only
def areEqual(str1, str2):
    Equal = (str1 == str2)
    if not Equal:
        print "hash collision for %s and %s" % (str1, str2)
    return Equal

#finds all the occurances of pattern inside a given text 
#and returns a list of corresponding indices
def findSubstrRabinKarp(text, pattern, base=Base, q=Q):
    n,m = len(text), len(pattern) 
    if n < m:
        return []
    if n == m and text == pattern:
        return [0]

    retValue = []

    p = rollingHash(pattern, base, q)
    ts = rollingHash(text[0:m], base, q)
    h = pow_by_mod(base, m-1, q)

    for s in xrange(n-m+1):
        if p == ts and areEqual(pattern, text[s:s+m]):
            retValue.append(s)
        if s < n-m:
            ts = nextRollingHash(ts, text[s], text[s+m], base, h, q)

    return retValue

# return a random charachers filled string of specified len
def getRandomString(len):
    chars = [chr(utils.Random(48, 122)) for x in xrange(len)]
    retValue = string.join(chars, '')
    return retValue 

def testRollingHash():
    stringLen = 1000
    patternLen = 12
    testString = getRandomString(stringLen)
    bm = pow_by_mod(Base, patternLen-1, Q)
    #print testString[0:PatternLen]
    Hash = rollingHash(testString[0:patternLen], Base, Q)
    for x in xrange(stringLen-patternLen):
        Hash = nextRollingHash(Hash, testString[x], testString[x+patternLen], Base, bm, Q)
        #print testString[x+1 : x+PatternLen+1]
        RealHash = rollingHash(testString[x+1 : x+patternLen+1], Base, Q)
        if Hash != RealHash:
            print "The rolling hash is broken"
            break
    

def testSubstr():
    text =  'abbracadabra'
    patterns = ['abbr', 'rac', 'ra', 'dabra', 'cadr'] 
    print [findSubstrRabinKarp(text, pattern, Base, Q) for pattern in patterns]

if __name__=="__main__":
    testRollingHash()
    #print chr(utils.Random(48, 122))
    testSubstr()
