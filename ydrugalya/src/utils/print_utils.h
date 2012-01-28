// File: PrintArray.h

#ifndef PrintArray_H
#define PrintArray_H

#include <algorithm>
#include <iostream>

namespace al {

template <class T, size_t n>
void printArray( const T (&buff)[n] ) {
    for(size_t i = 0; i < n; ++i) {
         std::cout << buff[i] << " ";
    }
}

template <class T>
void printArray( const T* buff, size_t n) {
    for(size_t i = 0; i < n; ++i) {
         std::cout << buff[i] << " ";
    }
}
        
}
#endif // #ifndef PrintArray_H
