#include <utility>
#include <list>
#include <vector>

namespace al
{

/** simple chained hash table implemenation with list-buckets */

template<typename KEY_T, typename EL_T, typename HASH_T, typename EQ_T> 
class HashTable {
public:
    HashTable(size_t bucketsCount, HASH_T func) 
        : _buckets(bucketsCount)
        , _hashFunc(func)   {
    }
        
    size_t getSize() const {
        return _buckets.size();
    }

    void add(KEY_T key, const EL_T& value) {
        size_t idx = _hashFunc(key);
        bucket_t& bucket = _buckets[idx];
        bucket.push_front( std::make_pair(key, value) );
    }

    const EL_T& get(const KEY_T& key) const {
        size_t idx = _hashFunc(key);
        const bucket_t& bucket = _buckets[idx];
        bucket_t::const_iterator it = bucket.begin();
        
        while( it != bucket.end() && ! _eqFunc((*it).first, key) ) {
            ++it;
        }

        return (*it).second;
    }

    void remove(const KEY_T& key) {
        size_t idx = _hashFunc(key) ;
        bucket_t& bucket = _buckets[idx];
        bucket_t::const_iterator it = bucket.begin();
        
        while( ! _eqFunc(*it, key) ) {
            ++it;
        }

        bucket.erase(it);
    }

private: //typdefs
    typedef std::pair<KEY_T, EL_T> KeyValuePair;
    typedef std::list<KeyValuePair> bucket_t;
    typedef std::vector<bucket_t> buckets_t;
private: //data
    buckets_t _buckets;
    HASH_T _hashFunc;
    EQ_T _eqFunc;
};

} // namespace al
