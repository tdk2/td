// knapsack.cpp : Defines the entry point for the console application.
#include <vector>
#include <utility>
#include <hash_map>
#include "../trees/binary_tree.h"

namespace al { namespace greedy {

typedef unsigned char u_int8_t;
typedef unsigned long u_long_t;
typedef std::vector<u_int8_t> bytes_vector_t;
typedef std::vector<bool> bit_vector_t;
typedef bit_vector_t prefix_code_t;

class CharItem;
typedef al::BinaryTree<CharItem> HuffmanCodeTree;

class CharItem {
	u_int8_t  _char;
	u_long_t _freq;
	prefix_code_t _prefixCode;
	al::BinaryTree<CharItem>::node_ptr_type _node;
	
public:
	CharItem() 
		: _char(-1)
		, _freq(0)
		, _prefixCode()
		, _node() {
	}
	
	CharItem(u_int8_t ch, u_long_t freq) 
		: _char(ch)
		, _freq(freq)
		, _prefixCode()
		, _node() {
	}


	u_int8_t character() const {return _char; }
	u_long_t frequency() const {return _freq; }
	void incFrequency() { ++_freq; }

	const std::vector<bool>& getPrefixCode() const {
		return _prefixCode;
	}

	void setPrefixCode(const std::vector<bool>& code ) {
		_prefixCode = code;
	}
	
	al::BinaryTree<CharItem>::node_ptr_type getNode() const { 
        return _node; 
    }

	void setNode(HuffmanCodeTree::node_ptr_type val) { 
        _node = val; 
    }
};

typedef std::vector<CharItem> char_items_t;
typedef al::BinaryTree<CharItem> HuffmanCodeTree;
typedef std::hash_map<u_int8_t, CharItem> freq_t;



void huffman_compress(const std::string& str,  bit_vector_t&/*out*/ code,  HuffmanCodeTree&/*out*/ tree, freq_t&/*out*/ charsFreq);

void huffman_decompress( const bit_vector_t& code, HuffmanCodeTree& tree, std::string&/*out*/ str );




} } // namespace al { namespace greedy {
