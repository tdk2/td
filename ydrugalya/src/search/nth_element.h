#pragma once
#include <algorithm>
#include <vector>
#include "../sort/insertion_sort.h"

namespace al {

template<typename T>
const size_t partition(T* A, size_t startIdx, size_t endIdx) {
	T pivot = A[endIdx - 1];
	size_t lessThanPivotIdx = startIdx - 1;

	for (size_t j = startIdx; j < endIdx - 1; ++j) {
		if (A[j] > pivot)
            continue;
        ++lessThanPivotIdx;
	    std::swap(A[lessThanPivotIdx], A[j]);
	}
    ++lessThanPivotIdx;

    std::swap( A[ endIdx - 1 ] , A[lessThanPivotIdx] );

	return lessThanPivotIdx;
}


template<typename T>
void memswap(T *arr1, T *arr2, size_t count) {
    while(count--){
        std::swap(  arr1[count] ,  arr2[count] );
    }
};


template<typename T>
const size_t partition(T* A, size_t startIdx, size_t endIdx, size_t pivotIdx) {
	
    std::swap( A[pivotIdx],  A[endIdx - 1] );
    T pivot = A[endIdx - 1];

	size_t lessThanPivotIdx = startIdx - 1;

	for (size_t j = startIdx; j < endIdx - 1; ++j) {
		if (A[j] > pivot)
            continue;
        ++lessThanPivotIdx;
	    std::swap(A[lessThanPivotIdx], A[j]);
	}
    ++lessThanPivotIdx;

    std::swap( A[ endIdx - 1 ] , A[lessThanPivotIdx] );

	return lessThanPivotIdx;
}


template<typename T>
const size_t stable_partition(T* A, size_t startIdx, size_t endIdx) {
	  // 1. devide n elements size_to the groups of 5
    const size_t numElement = endIdx - startIdx;
    const size_t numGroups = numElement / 5;
    const size_t remainder = numElement % 5;

    // 2. sort each group by insertion sort
    std::vector<T> medians;
    size_t grpIdx = 0;
    while(grpIdx < numGroups) {
        size_t grpStartIdx = startIdx + grpIdx * 5;
        insertion_sort_recursive(&A[0] + grpStartIdx, 5);
        medians.push_back( *(&A[0] + grpStartIdx + 2) );
        ++grpIdx;
    }

    for(size_t j = 0; j < remainder; ++j) {
        size_t grpStartIdx = startIdx + numGroups * grpIdx * 5;
        insertion_sort_recursive(&A[0] + grpStartIdx, remainder);
        medians.push_back( *(&A[0] + grpStartIdx + remainder / 2 ) );
        ++grpIdx;
    }
    
    T med = Select(&medians[0], 0, medians.size(), medians.size() / 2 );

    size_t medIdx = 0;
    for(size_t j = startIdx; j < endIdx; ++j) {
        if (A[j] ==  med) {
            medIdx = j;
            break;
        }
    }

    partition(A, startIdx, endIdx, medIdx);

    medIdx = 0;
    for(size_t j = startIdx; j < endIdx; ++j) {
        if (A[j] ==  med) {
            medIdx = j;
        }
    }
    
    return medIdx;
}


template<typename T>
const size_t Select1(T* A, size_t startIdx, size_t endIdx, size_t i) {
    if (startIdx == endIdx)
        return startIdx;

    int pivotIdx = stable_partition(A, startIdx, endIdx);

    size_t countElements  = pivotIdx - startIdx;
    
    if (countElements == i) {
        return A[pivotIdx];
    }

    if (i < countElements) {
        return Select1(A, startIdx, pivotIdx - 1, i);
    } else {
        return Select1(A, pivotIdx + 1, endIdx, i - countElements);
    }

    return 0;
}


template<typename T>
const T Select(T* A, size_t startIdx, size_t endIdx, size_t i) {
    if (startIdx == endIdx)
        return startIdx;
    
    size_t pivot = partition( A, startIdx, endIdx);

    size_t countElement = pivot - startIdx;

    if (i == countElement) {
        return A[pivot];
    }
    
    if (i < countElement) {
        return Select(A, startIdx, pivot, i);
    } else {
        return Select(A, pivot, endIdx, i - countElement);
    }
}



}