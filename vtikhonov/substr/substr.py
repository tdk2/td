import os, sys, string
sys.path.append(sys.path[0] + '/../hash')
import utils

# a hash
def rollingHash(text, base=256):
    return 0

# returns hash of 'moved window'
def nextRollingHash(prevHash, outChar, inChar):
    return 0

#finds all the occurances of pattern inside a given text 
#and returns a list of corresponding indices
def findSubstrRabinKarp(text, pattern, base=256, q=22111):
    if len(text) < len(pattern):
        return []
    if len(text) == len(pattern) and text == pattern:
        return [0]

 
    return []

# return a random charachers filled string of specified len
def getRandomString(len):
    chars = [chr(utils.Random(48, 122)) for x in xrange(len)]
    retValue = string.join(chars, '')
    return retValue 

def testRollingHash():
    StringLen = 1000
    PatternLen = 12
    testString = 'Hello world, this is me'
    StringLen = len(testString)
    #testString = getRandomString(StringLen)
    #print testString[0:PatternLen]
    Hash = rollingHash(testString[0:PatternLen])
    for x in xrange(StringLen-PatternLen):
        Hash = nextRollingHash(Hash, testString[x], testString[x+PatternLen])
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
