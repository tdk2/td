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
