'''
Created on 12.12.2011

@author: DK
'''

def get_hash( arr ):
    
    if len(arr) == 0:
        return 0
        
    result = ord( arr[0] )
    
    for i in xrange(1, len(arr)):
        result = result ^ ord( arr[i] )
         
    return result 


def update_hash( hash_value, prev_sym, next_sym ):
    return hash_value ^ ord( prev_sym ) ^ ord( next_sym )


def hash_strstr( string, sub_string ):
    
    if len(string) < len(sub_string) :
        return 0
    elif len(string) < len(sub_string) :
        if string == sub_string :
            return 1
        else:
            return 0
        
    search_hash = get_hash( sub_string )
    
    result = 0    
    for i in xrange( len(string) - len(sub_string) ):
        if search_hash == get_hash( string[i:i+len(sub_string)] ):
            if( string[i:i+len(sub_string)] == sub_string ):
                result += 1
                
    return result          
 
    
if __name__ == '__main__':
    
    string = "ardsdsasdasdsdfasd"
    sub_string = "sds"
    
    substr_count = hash_strstr( string, sub_string )
    
    pass