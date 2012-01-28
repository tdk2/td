#pragma once

#include "counting_sort.h"

namespace al
{

template<typename VT, typename KT>
void radix_sort(const VT* src, 
                VT* dest, 
                KT* counterBuff, 
                const std::tr1::function< VT(const VT& val, size_t keyIdx) > extractKeyFunc,
                size_t elementsCount, 
                size_t buffCnt, 
                size_t keyCnt) {

    VT* tmp = new VT[ elementsCount ];
    memcpy( tmp, src, elementsCount * sizeof(VT) );
    for(size_t i = 0; i < keyCnt; ++i) {
        counting_sort(tmp, dest, counterBuff, extractKeyFunc, elementsCount, buffCnt, i );
        memcpy( tmp, dest, elementsCount * sizeof(VT) );
    }

    memcpy( dest, tmp, elementsCount * sizeof(VT) );

    delete[] tmp;
}

}; // namespace al


