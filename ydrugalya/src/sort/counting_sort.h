#pragma once

#include <algorithm>
#include <functional>


namespace al
{

template<typename VT, typename KT>
void counting_sort(const VT* src, // source array
                   VT* dest, // destination array
                   KT* counterBuff,  // auxilary buffer to keep counters
                   const std::tr1::function< VT(const VT& val, size_t keyIdx) > extractKeyFunc, // pointer to function responsible for key extraction
                   size_t elementsCount, // count of elements in source and destination arrays
                   size_t buffCnt, // count of elements in buffer
                   size_t keyIdx // key index - used to extract proper key from src[i]
                   
                   ) {
    // initialization step
    std::memset( counterBuff, 0, sizeof(KT) * buffCnt );
    
    for(size_t i = 0; i < elementsCount; ++i) {
       const VT& key = extractKeyFunc(  src[i],   keyIdx); 
	   counterBuff[ key ] += 1;
    }

    // after this step C[i] contains number of elements  <= A[i]
    // this number can be trnformed into the position by 
    // subtracting one
    for(size_t i = 1; i < buffCnt; ++i)
	   counterBuff[ i ] += counterBuff[i - 1];


    for(int i = elementsCount - 1; i >= 0; --i) {
        const VT& key = extractKeyFunc(  src[i],   keyIdx); 
		KT& position = counterBuff[key];
        dest[--position] = src[i];
	}
}


};// namespace al


