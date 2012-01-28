#include "../hash/hash_table.h"

#include <hash_map>
#include <map>
#include <iostream>
#include <boost/progress.hpp>

struct eqint {
  bool operator()(const int n1, int n2) const {
    return n1 == n2;
  }
};

static const size_t BITS_IN_WORD = 32;
static const size_t HIGH_BIT_MASK = 1 << (BITS_IN_WORD - 1);

template<typename T>
struct HashFunc {
    HashFunc(size_t r) : _r(r) {
        // _a chosen to be an odd integer in range of 2 ^ (w - 1) to 2 ^ w
        _a = 1 << (BITS_IN_WORD - 2) ;
        _a += 1 << 16;
        _a += 1 << 8;
        _a += 1 << 4;
        _a += 1 << 3;
        _a += 1;
    }

    size_t operator()(T k) const {
        // _a chosen to be an odd integer in range of 2 ^ (w - 1) to 2 ^ w
        // (A*k mod 2 ^ W) >> (w - r)
        return ( (_a * k) % HIGH_BIT_MASK ) >> ( (BITS_IN_WORD - _r) - 1 ) ;
    }

    size_t _r;
    size_t _a;
};

template<typename T>
void fill_random_num(T* arr, size_t elementsCount) {
for(size_t i = 0; i < elementsCount; ++i )
	arr[i] = rand() % std::numeric_limits<T>().max() ;
}

namespace al {

void increasingSlotsCount(std::vector<size_t>& vec) {
    size_t r = 10;

    while(r <  20) {
        size_t slots_count = ( 1 << r );
        size_t ELEMENTS_COUNT =  vec.size();
        HashFunc<int> f(r);
        al::HashTable<int, int, HashFunc<int>, eqint> hm(slots_count, f);
        // insert
        {
            std::cout << "\n custom hash map. inserting " << ELEMENTS_COUNT << " elements. into " << slots_count << " slots ";
            boost::progress_timer t(std::cout);
            for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
                hm.add(vec[i], i);
            }
        }

        int n;
        // select
        {
            
            std::cout << "\n custom hash map. accessing all elements. from " << slots_count << " slots " ;
            boost::progress_timer t(std::cout);
            for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
                n = hm.get(vec[i]);
            }
        }

        r += 2;
    }
}


void demo_hash_map() {
    using namespace std;
  
    size_t ELEMENTS_COUNT = 100000;
    std::vector<size_t> vec(ELEMENTS_COUNT);
    fill_random_num<size_t>(&vec[0], ELEMENTS_COUNT);
    std::map<int, int> m;

    increasingSlotsCount(vec);
 
    const size_t slots_count = 1024;
    HashFunc<int> f(10);
    al::HashTable<int, int, HashFunc<int>, eqint> hm(slots_count, f);
    hash_map<int, int> hmstd;
    
    {
      
        std::cout << "\n std::map. inserting " << ELEMENTS_COUNT << " elements: ";
        boost::progress_timer t(std::cout);
        for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
            m[vec[i]] = i;
        }

    }

    {
      
        std::cout << "\n custom hash map. inserting " << ELEMENTS_COUNT << " elements: ";
        boost::progress_timer t(std::cout);
        for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
            hm.add(vec[i], i);
        }
    }

    {
      
        std::cout << "\n std::hash map. inserting " << ELEMENTS_COUNT << " elements: ";
        boost::progress_timer t(std::cout);
        for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
            hmstd[vec[i]]  = i;
        }
    }
    
    int n = 0;

     {
        std::map<int, int> m;
        std::cout << "\n std::map. accessing all elements: " ;
        boost::progress_timer t(std::cout);
      
        for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
            n = m[vec[i]];
        }
    }

    {
       
        std::cout << "\n custom hash map. accessing all elements: " ;
        boost::progress_timer t(std::cout);
        for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
            n = hm.get(vec[i]);
        }
    }

    {
       
        std::cout << "\n std::hashmap. accessing all elements: " ;
        boost::progress_timer t(std::cout);
        for(size_t i = 0; i < ELEMENTS_COUNT; ++i) {
            n = hmstd[vec[i]];
        }
    }
}

}