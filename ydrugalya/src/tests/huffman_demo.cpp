#include <iostream>
#include <string>

#include "../greedy/huffman.h"
#include <boost/foreach.hpp>

namespace al {

void huffman_demo() {
	using namespace std;
	using namespace al::greedy;
	string src_string = "There are more things in heaven and earth, Horatio,	Than are dreamt of in your philosophy.";
	//string src_string = "40 ";
	bit_vector_t huffmanCode;
	HuffmanCodeTree tree;
	freq_t freq;
	cout << "source string : " << src_string << std::endl;
	huffman_compress( src_string, huffmanCode, tree, freq);
	

	cout << "Huffman code : ";
	BOOST_FOREACH(bool b, huffmanCode) {
		std::cout << static_cast<int>(b);
	}

	cout << endl;

	std::cout << "compress ration " << 1.0 * ( (src_string.size() * 8.0) / (1.0 * huffmanCode.size()) );
	
	cout << endl;
	
	string restored_string;
	huffman_decompress(huffmanCode, tree, restored_string);
	cout << "restored string: " <<  restored_string << std::endl;

}

}