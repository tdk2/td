#pragma once

#include <boost/shared_ptr.hpp>
#include <memory>
#include <cstring>


template <typename Type> inline
bool isNull(Type const& value) {
   return 0 == value;
}

template <typename Type> inline
bool isNull(std::auto_ptr<Type> const& ptr)
{
   return 0 == ptr.get();
}

template <typename Type> inline
bool isNull(boost::shared_ptr<Type> const& ptr)
{
   return 0 == ptr.get();
}


template <typename Container> inline
bool isEmpty(Container const& container)
{
   return container.empty();
}


inline
bool isEmpty(char const* pString)
{
   return (0 == pString) || (0 == std::strlen(pString));
}


//! Check presence of the bit in the value using bit mask. For example isBitSet(10100101b, 00100000b)
template< typename BITS_T, typename BIT_MASK_TYPE >
inline bool isBitSetByMask( BITS_T val, BIT_MASK_TYPE bitMask ) {
    return static_cast<BIT_MASK_TYPE>( val & bitMask ) == bitMask ;
}

//! Check presence of the bit in the value using bit number. For example isBitSet( 10100101b, 5 )
template< typename BITS_T, typename BIT_NUMBER_TYPE >
inline bool isBitSetByNo( BITS_T val, BIT_NUMBER_TYPE bitNumber ) {
    return isBitSetByMask(val, 1 << bitNumber );
}