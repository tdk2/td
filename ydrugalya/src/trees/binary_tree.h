#pragma once
#include <boost/shared_ptr.hpp>
#include "../utils/logic_shims.h"

namespace al
{
	template <typename T>
	class BinaryTree
	{
	public:

	    class Node
	    {
          public:
             typedef T node_data_type;
             typedef boost::shared_ptr<Node> node_ptr_type;

		    protected:
			    node_data_type m_data;
			    node_ptr_type m_pParent;
			    node_ptr_type m_pLeft;
			    node_ptr_type m_pRight;
		    public:
			    Node(const node_data_type data, 
				     const node_ptr_type pParent, 
				     const node_ptr_type pLeft, 
				     const node_ptr_type pRight) :
				    m_pParent(parent),
				    m_pLeft(pLeft),
				    m_pRight(pRight) { }

                Node(const node_data_type data) : m_data(data) { 
                }
				
			    T get_data() const { return m_data; }
				void set_data(const node_data_type& data ) { m_data = data; }

			    node_ptr_type get_parent() const { return m_pParent; }
			    void set_parent(node_ptr_type val) { m_pParent = val; }

			    node_ptr_type get_left() const { return m_pLeft; }
			    void set_left(node_ptr_type val) { m_pLeft = val; }

			    node_ptr_type get_right() const { return m_pRight; }
			    void set_right(node_ptr_type val) { m_pRight = val; }
        };

        typedef boost::shared_ptr<Node> node_ptr_type;

        node_ptr_type get_root() {  return m_pRoot; }

        node_ptr_type make_node(T t) { return node_ptr_type( new Node(t) ); }

        node_ptr_type tree_minimum(node_ptr_type node) {
            node_ptr_type current_node = node;
             while( !isNull(current_node->get_left()) ) {
                current_node = current_node->get_left();
             }

             return current_node;
        }

        node_ptr_type tree_maximum(node_ptr_type node) {
             node_ptr_type current_node = node;
             while( !isNull(current_node->get_right()) ) {
                current_node = current_node->get_right();
             }

             return current_node;
        }

        node_ptr_type tree_successor(const node_ptr_type node) {
             // если правое поддерево непустое, что сл. за node
             // элемент является краним левым узлом в правом 
             // поддереве. т.е. минимальный из элементов больших node
             if ( ! isNull( node->get_right() ) ) {
                return tree_minimum(node->get_right());
             }

             node_ptr_type parent_node = node->get_parent();
             node_ptr_type current_node = node;

             // поднимаемся вверх по дереву до тех пор,
             // пока не встретим узел который является левым
             // дочерним узлом своего родителя
             // т.е. ищем наименьшего предка node, чей левый наследник
             // тоже является предком node
             while( !isNull(parent_node) && parent_node->get_right() == current_node ) {
                current_node = parent_node;
                parent_node = parent_node->get_parent();
             }

             return parent_node;
          }

          node_ptr_type tree_predeсessor(const node_ptr_type node) {
             if ( !isNull(node->get_left()) )  {
                return tree_maximum(node->get_right());
             }

             // до тех пор пока мы поднимаемся по левой ветке...
             // и есть куда подниматся
             node_ptr_type parent_node = node->get_parent();
             node_ptr_type current_node = node;

             while( !isNull(parent_node) && parent_node->get_left() == current_node) {
                current_node = parent_node;
                parent_node = parent_node->get_parent();
             }

             return parent_node;
          }


          void insert(node_ptr_type node) {
         
             node_ptr_type current_node = m_pRoot; // текущий узел
             node_ptr_type parent_node = m_pRoot;  // указывает на родительский 
                                                   // узел по отношению к проходимому узлу
             while (current_node != NULL)    {
                parent_node = current_node;
                // если данное во вставляемом узле меньше, сворачиваем в левую ветку
                // иначе - в правую
                if (node->get_data() < current_node->get_data()) {
                   current_node = current_node->get_left();
                }
                else {
                   current_node = current_node->get_right();
                }
               
             }

             node->set_parent(parent_node);

             if ( isNull(parent_node) ) { // деверево пустое
                m_pRoot = node;
             } else if ( node->get_data() < parent_node->get_data() ) {
                parent_node->set_left(node);
             } else {
                parent_node->set_right(node);
             }
        }

        void transplant(node_ptr_type u, node_ptr_type v) {
            if (isNull( u->get_parent() )) {
                // if u has no parent than it is root v must become root
                m_pRoot = v; 
            } else if ( u->get_parent()->get_left()  == u ) {
                u->get_parent()->set_left(v);
                // now parent of u has v as it's left child
            } else if ( u->get_parent()->get_right()  == u ) {
                u->get_parent()->set_right(v);
                // now parent of u has v as it's right child
            }

            if ( ! isNull(v) ) {
                v->set_parent( u->get_parent() );
                // now v rooted in u's parent
            }
        }

        void leftRotate(node_ptr_type x) {
            // ASSERT( isNull(x.get_rigth() )
            node_ptr_type y = x->get_right(); 
            
            // assign Gamma as a right child of x
            // we'll do y.left = x later, so it it a good place to
            // save y.left here. remember that x.right is stored 
            // in y now;
            x->set_right( y->get_left() );
            if ( !isNull( y->get_left() )  ) { // check y's left subtree is not empty
                y->get_left()->set_parent(x);
            }

            // reassign x's parent as parent to y
            y->set_parent( x->get_parent() );

            // establish connection between y and x's ex-parent
            if ( isNull( y->get_parent() ) ) {
                m_pRoot = y;
            } else if ( x->get_parent()->get_left() == x ) { // if x was left child
                x->get_parent()->set_left(y); // x was left child of it's parent now y is a left child
            } else { // x was right  child
                x->get_parent()->set_right(y); // x was right child of it's parent . now is is right child
            }

            y->set_left(x); // now y is a left child of x
            x->set_parent(y); 
        }

            
        void rightRotate(node_ptr_type y) {
            // ASSERT( isNull(y.get_left() )

            node_ptr_type x = y->get_left(); 
                       
            y->set_left( x->get_right() );
            if ( !isNull( y->get_right() )  ) { 
                x->get_right()->set_parent(y);
            }

            // reassign y's parent as parent to x
            x->set_parent( y->get_parent() );

            if ( isNull( x->get_parent() ) ) {
                   m_pRoot = x;
            } else if ( y->get_parent()->get_left() == y ) { 
                y->get_parent()->set_left(x); 
            } else { // x was right  child
                x->get_parent()->set_right(y); 
            }

            x->set_right(y); 
            y->set_parent(x); 
        }


        void deleteNode(node_ptr_type z) {

            if ( isNull( z->get_left() ) ) { // case a
                transplant( z, z->get_right() );
            } else if ( isNull(z->get_right() ) ) { // case b
                transplant( z, z->get_left() );
            } else {
                // find predecessor
                node_ptr_type y = tree_minimum( z->get_right() );

                // case d predecessor is right child of z
                if ( y->get_parent() != z ) {
                     transplant( y, y->get_right() );

                     y->set_right( z->get_right() );
                     y->get_right()->set_parent( y );
                }

                transplant( z, y );
                y->set_left( z->get_left() );
                y->get_left()->set_parent( y );
            }
        }
	private:
		node_ptr_type m_pRoot;
	};

}