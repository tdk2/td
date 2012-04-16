#include "./huffman.h"

#include <iostream>

#include <utility>
#include <boost/foreach.hpp>
#include <algorithm>
#include <vector>

#include "../utils/logic_shims.h"
#include "../trees/binary_tree.h"

namespace al { namespace greedy {


using namespace std;



void calcFreq(const std::string& str, freq_t&/*out*/ freq)  {
	const size_t strSize = str.size();
	for(size_t i = 0; i < strSize; ++i) {
		u_int8_t ch = static_cast<u_int8_t>(str[i]);
		freq_t::iterator it = freq.find(ch);
		if ( freq.find(ch) == freq.end()) {
			CharItem ci(ch, 1);
			freq[ch] = ci;
		} else {
			CharItem& ci =  (*it).second;
			ci.incFrequency();
		}
	}
}


bool operator < (const CharItem& it1, const CharItem& it2)  {
	return it1.frequency() > it2.frequency();
}

CharItem extractMin(char_items_t& items)  {
	pop_heap ( items.begin(), items.end() );
	CharItem result = *items.rbegin();
	items.pop_back();
	return result;
}
 
void buildPrefixCode(HuffmanCodeTree::node_ptr_type& leaf, std::vector<bool>& prefixCode) {

	HuffmanCodeTree::node_ptr_type p = leaf;

	while( !isNull(p->get_parent() ) ) {
		const bool bitVal = p->get_parent()->get_left() != p;
		prefixCode.push_back(bitVal);
		p = p->get_parent();
	}

	std::reverse( prefixCode.begin(), prefixCode.end() );
}

bool isLeaf(HuffmanCodeTree::node_ptr_type node) {
	return isNull( node->get_left() ) && isNull( node->get_right() );
}
void updatePrefixCodes(HuffmanCodeTree::node_ptr_type node, size_t& treeSum, freq_t&/*out*/ charsFreq) {
	if ( isNull(node) ) {
		return;
	}
	
	updatePrefixCodes(node->get_left(), treeSum, charsFreq);
	if (isLeaf (node) )	{
		prefix_code_t prefix_code;
		buildPrefixCode(node, prefix_code);
		CharItem& ci = node->get_data();
		treeSum += prefix_code.size() * ci.frequency();
		ci.setPrefixCode(prefix_code);
		charsFreq[ci.character()].setPrefixCode(prefix_code);
	}

	updatePrefixCodes(node->get_right(), treeSum, charsFreq);
}


void constructHuffmanCodes(freq_t&/*out*/ charsFreq, HuffmanCodeTree&/*out*/ tree) {

	char_items_t items;

	BOOST_FOREACH(const freq_t::value_type& p,  charsFreq) {
		items.push_back( p.second );
	}
	
	std::make_heap( items.begin(), items.end()/*, &CharItemsHeapCompare*/ );

	static const CharItem NULL_ITEM(-1, -1);

	HuffmanCodeTree::node_ptr_type z;
	for(size_t i = 0; i < charsFreq.size() - 1; ++i) {

		CharItem min1 = extractMin(items);
		CharItem min2 = extractMin(items);

		
		CharItem zData = CharItem(-1, min1.frequency() + min2.frequency() );
		z = tree.make_node(zData);
		zData.setNode(z);
		z->set_data(zData);

		HuffmanCodeTree::node_ptr_type min1Node = min1.getNode();
		if ( isNull( min1Node ) ) {
			min1Node = tree.make_node(min1);
		}

		HuffmanCodeTree::node_ptr_type min2Node = min2.getNode();
		if ( isNull( min2Node ) ) {
			min2Node = tree.make_node(min2);
		}
				
		z->set_left( min1Node );
		z->set_right( min2Node );    
		

		min1Node->set_parent(z);
		min2Node->set_parent(z);
		
		items.push_back( z->get_data() );
		push_heap(items.begin(), items.end());
	}

	tree.insert(z);


}

void huffman_compress(const std::string& str,  bit_vector_t&/*out*/ code,  HuffmanCodeTree&/*out*/ tree, freq_t&/*out*/ charsFreq) {
	calcFreq(str, charsFreq);

	constructHuffmanCodes(charsFreq, tree);

	size_t treeSize = 0;
	updatePrefixCodes(tree.get_root(), treeSize,  charsFreq);

	code.resize( treeSize );
	const size_t strSize = str.size();
	size_t bit_idx = 0;
	for(size_t i = 0; i < strSize; ++i) {
		const u_int8_t ch = static_cast<u_int8_t>( str[i] );
		const prefix_code_t chCode = charsFreq[ch].getPrefixCode();
		const size_t codeSize = chCode.size();

		for(size_t chbIdx = 0; chbIdx < codeSize; ++chbIdx) {
			code[bit_idx++] = chCode[chbIdx];
		}
	}
}


void huffman_decompress( const bit_vector_t& code, HuffmanCodeTree& tree, std::string&/*out*/ str ) {

	const size_t code_size = code.size();
	size_t i = 0;
	while(i < code_size) {
		
		
		HuffmanCodeTree::node_ptr_type node = tree.get_root();
		while( ! isLeaf(node) ) {
			const bool b = code[i++];
			if (b) {
				node = node->get_right();
			} else {
				node = node->get_left();
			}
		}

		str += static_cast<char>( node->get_data().character() );
	}
}

} } // namespace al { namespace greedy {

