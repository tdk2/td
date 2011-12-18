import os, sys, string
sys.path.append(sys.path[0] + '/../hash')
import utils

# a hash
def rollingHash(text, base=256):
    return 0

# returns hash of 'moved window'
def nextRollingHash(prevHash, outChar, inChar):
    return prevHash

# returns the same value as math.pow(a, n) % q, but more efficiently
def pow_by_mod(a, n, q):
    result = 1
    for x in xrange(n):
        result = (result*a) % q
    return result

#finds all the occurances of pattern inside a given text 
#and returns a list of corresponding indices
def findSubstrRabinKarp(text, pattern, base=256, q=22111):
    n,m = len(text), len(pattern) 
    if n < m:
        return []
    if n == m and text == pattern:
        return [0]

    p, t0, h = 0, 0, pow_by_mod(base, m-1, q)
    retValue = []
    for i in xrange(len(pattern)):
        p = (base*p + ord(pattern[i])) % q
        t0 = (base*t0 + ord(text[i])) % q
    ts = t0

    for s in xrange(n-m+1):
        if p == ts and pattern == text[s:s+m]:
            retValue.append(s)
        if s < n-m:
            ts = (base*(ts - ord(text[s])*h) + ord(text[s+m])) % q
    return retValue

# return a random charachers filled string of specified len
def getRandomString(len):
    chars = [chr(utils.Random(48, 122)) for x in xrange(len)]
    retValue = string.join(chars, '')
    return retValue 

def testRollingHash():
    StringLen = 1000
    PatternLen = 12
    testString = getRandomString(StringLen)
    #print testString[0:PatternLen]
    Hash = rollingHash(testString[0:PatternLen])
    for x in xrange(StringLen-PatternLen):
        Hash = nextRollingHash(Hash, testString[x], testString[x+PatternLen])
        #print testString[x+1 : x+PatternLen+1]
        RealHash = rollingHash(testString[x+1 : x+PatternLen+1])
        if Hash != RealHash:
            print "The rolling hash is broken"
            break
    

def testSubstr():
    text =  'abbracadabra'
    patterns = ['abbr', 'rac', 'ra', 'dabra', 'cadr'] 
    print [findSubstrRabinKarp(text, pattern) for pattern in patterns]

if __name__=="__main__":
    testRollingHash()
    #print chr(utils.Random(48, 122))
    testSubstr()
