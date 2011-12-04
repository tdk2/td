import matplotlib
from pylab import *

def hash1(k, m):
    return k % m

def hash2(k, m):
    A = 0.618
    return int ( m * ( ( k * A ) % 1.0 ) )

def my_hash(k):
    part3 = (k >> 24) & 0xff
    part2 = (k >> 16) & 0xff
    part1 = (k >> 8) & 0xff
    part0 = (k >> 0) & 0xff
    
    result = part3 ^ part2 ^ part1 ^ part0
    
    return result    
    

if __name__=="__main__":    
    m = 0xff
    n = m * 100
    x = range(0,n)
    
        
    hash_dict_1 = dict()    
    hash_dict_2 = dict()
    hash_dict_m = dict()
    
    for i in x:
        h1 = hash1(i, m)
        h2 = hash2(i, m)
        hm = my_hash(i)
        
        if hash_dict_1.has_key(h1):
            hash_dict_1[h1] += 1
        else:
            hash_dict_1[h1] = 1
        
            
        if hash_dict_2.has_key(h2):
            hash_dict_2[h2] += 1
        else:
            hash_dict_2[h2] = 1
        
        if hash_dict_m.has_key(hm):
            hash_dict_m[hm] +=+ 1
        else:
            hash_dict_m[hm] = 1
        
            
    subplot(311)
    matplotlib.pyplot.bar(hash_dict_1.keys(), hash_dict_1.values())
    title('h1')
    
    subplot(312)
    matplotlib.pyplot.bar(hash_dict_2.keys(), hash_dict_2.values())
    title('h2')
    
    subplot(313)
    matplotlib.pyplot.bar(hash_dict_m.keys(), hash_dict_m.values())
    title('hm')
    
    show()    
    
        
    
    
    
    
    