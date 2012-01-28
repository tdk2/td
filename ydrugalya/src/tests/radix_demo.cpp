#include <boost/progress.hpp>

#include "../utils/print_utils.h"
#include "../sort/radix_sort.h"


namespace al
{


typedef unsigned char byte_t;
typedef unsigned short ushort;
typedef unsigned int uint;

size_t bitsInBytes = 8;

ushort exctractByte(const ushort& src, size_t idx)
{
    const ushort shift = idx * bitsInBytes;
    return ( (0xff << shift ) & src) >> shift;
}

template<typename T>
void fill_random_num(T* arr, size_t elementsCount) {
    for(size_t i = 0; i < elementsCount; ++i )
	    arr[i] = rand() % std::numeric_limits<T>().max() / 2;
}

template<typename VT, typename KT>
void sortBytes(VT* const src, VT* dest, KT* buff, size_t elementsCount, size_t maxRange) {
    al::radix_sort<VT>(src, dest, buff, exctractByte, elementsCount,  maxRange, sizeof(VT) );
}

template<typename VT>
void testRadixSort(VT *arr, size_t elementsCount) {
    VT *dest = new VT[elementsCount];
    size_t *buff = new size_t[256];
    {
        std::cout << "\n radix sort " << " type size " << sizeof(VT) << " elements count:" << elementsCount << " \n";
        boost::progress_timer t(std::cout);
        sortBytes(arr, dest, buff, elementsCount, 256);
    }


    for(size_t i = 1; i < elementsCount; ++i) {
        if (dest[i-1] > dest[i]) {
            std::cout << "not sorted properly ";
        }
    }
    
  
    delete[] dest;
    delete[] buff;
}


template<typename VT>
void testRadixSortSimple() {
  
    VT A[] = {1000, 255, 99, 326, 584, 2, 1, 6, 316, 428, 614, 24868};
    
    const size_t ARR_LEN = sizeof(A) / sizeof( A[0] );
    VT B[ARR_LEN] = {0};
    VT C[256] = {0};

    sortBytes(A, B, C, ARR_LEN, 256);
	
    al::printArray(B);

    std::cout << "\n";
}

void radix_demo()
{
    using namespace al;

    typedef uint sorted_type;

    testRadixSortSimple<sorted_type>();
    
    static const size_t ELEMENTS_COUNT = 10000000;

    sorted_type *arr = new sorted_type[ELEMENTS_COUNT];

    fill_random_num(arr, ELEMENTS_COUNT);

    testRadixSort<sorted_type>(arr, ELEMENTS_COUNT);

    {
        std::cout << "\n std::sort " << " type size " << sizeof(sorted_type) << " elements count:" << ELEMENTS_COUNT << "\n";
        boost::progress_timer t(std::cout);
        std::sort(arr, arr + ELEMENTS_COUNT);
    }
    
    delete[] arr;
    std::cout << "\n";
}



}