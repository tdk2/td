#include <iostream>
#include "../trees/binary_tree.h"

namespace al {

void inorder_tree_walk(al::BinaryTree<int>::node_ptr_type node);
void postorder_tree_walk(al::BinaryTree<int>::node_ptr_type node);
void preorder_tree_walk(al::BinaryTree<int>::node_ptr_type node);

void bst_demo() {
   al::BinaryTree<int> tree;

   // Cormen fig. 12.2
   tree.insert(tree.make_node(15));
   tree.insert(tree.make_node(6));
   tree.insert(tree.make_node(3));
   tree.insert(tree.make_node(2));
   tree.insert(tree.make_node(4));
   tree.insert(tree.make_node(7));
   tree.insert(tree.make_node(13));
   tree.insert(tree.make_node(9));
   tree.insert(tree.make_node(18));
   tree.insert(tree.make_node(17));
   tree.insert(tree.make_node(20));

   al::BinaryTree<int>::node_ptr_type node = tree.tree_minimum(tree.get_root());
   std::cout << "tree minimum : " << node->get_data() << "\n";
   
   node = tree.tree_maximum(tree.get_root());
   std::cout << "tree maximum : " << node->get_data() << "\n";

   node = tree.tree_successor( tree.tree_minimum( tree.get_root() ) );
   std::cout << "tree tree_successor (min) : " << node->get_data() << "\n";
   
   node = tree.tree_predeñessor( tree.tree_maximum( tree.get_root() ) );
   std::cout << "tree tree_predeñessor (max) : " << node->get_data() << "\n";

   std::cout << "inorder tree walk << ";
   inorder_tree_walk( tree.get_root() );

   std::cout << "\npreorder tree walk << ";
   preorder_tree_walk( tree.get_root() );
   
   std::cout << "\npostorder tree walk << ";
   postorder_tree_walk( tree.get_root() );
}


void inorder_tree_walk(al::BinaryTree<int>::node_ptr_type node) {
    if ( isNull(node) ) {
        return;
    }
    inorder_tree_walk( node->get_left() );
    std::cout << node->get_data() << " ";
    inorder_tree_walk( node->get_right() );
}

void postorder_tree_walk(al::BinaryTree<int>::node_ptr_type node) {
    if ( isNull(node) ) {
        return;
    }
    postorder_tree_walk( node->get_left() );
    postorder_tree_walk( node->get_right() );
    std::cout  << node->get_data() << " ";
}

void preorder_tree_walk(al::BinaryTree<int>::node_ptr_type node) {
    if ( isNull(node) ) {
        return;
    }
    std::cout  << node->get_data() << " ";
    postorder_tree_walk( node->get_left() );
    postorder_tree_walk( node->get_right() );
}

}
