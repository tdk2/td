#include <boost/shared_ptr.hpp>
#include "../utils/logic_shims.h"
#include "./binary_tree.h"

namespace al
{
    enum NODE_COLOR {RED, BLACK};

	template <typename T>
	class RBTree : BinaryTree<T>
	{
	public:

	    class RBNode 
	    {
          public:
             typedef T node_data_type;
             typedef boost::shared_ptr<RBNode> node_ptr_type;

		    private:
			    node_data_type m_data;
			    node_ptr_type m_pParent;
			    node_ptr_type m_pLeft;
			    node_ptr_type m_pRight;
                NODE_COLOR _color; 
		    public:
                
			    RBNode(const node_data_type data, 
				       const node_ptr_type pParent, 
				       const node_ptr_type pLeft, 
				       const node_ptr_type pRight          
                     ) :
				    m_pParent(parent),
				    m_pLeft(pLeft),
				    m_pRight(pRight) { }

                RBNode(const node_data_type data) : m_data(data) { 
                }
				
			    T get_data() const { return m_data; }

			    node_ptr_type get_parent() const { return m_pParent; }
			    void set_parent(node_ptr_type val) { m_pParent = val; }

			    node_ptr_type get_left() const { return m_pLeft; }
			    void set_left(node_ptr_type val) { m_pLeft = val; }

			    node_ptr_type get_right() const { return m_pRight; }
			    void set_right(node_ptr_type val) { m_pRight = val; }

                NODE_COLOR get_color() const { return _color; }
                void set_color(NODE_COLOR val) { _color = val; }
        };

        typedef boost::shared_ptr<RBNode> node_ptr_type;

        node_ptr_type NULL_NODE;

        RBTree() {
            NULL_NODE.reset( new RBNode( T() ) );
            NULL_NODE->set_color(BLACK);
            m_pRoot = NULL_NODE;
        }

        node_ptr_type get_root() {  return m_pRoot; }

        node_ptr_type make_node(T t) { return node_ptr_type( new RBNode(t) ); }

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
             // ���� ������ ��������� ��������, ��� ��. �� node
             // ������� �������� ������ ����� ����� � ������ 
             // ���������. �.�. ����������� �� ��������� ������� node
             if ( ! isNull( node->get_right() ) ) {
                return tree_minimum(node->get_right());
             }

             node_ptr_type parent_node = node->get_parent();
             node_ptr_type current_node = node;

             // ����������� ����� �� ������ �� ��� ���,
             // ���� �� �������� ���� ������� �������� �����
             // �������� ����� ������ ��������
             // �.�. ���� ����������� ������ node, ��� ����� ���������
             // ���� �������� ������� node
             while( !isNull(parent_node) && parent_node->get_right() == current_node ) {
                current_node = parent_node;
                parent_node = parent_node->get_parent();
             }

             return parent_node;
          }

          node_ptr_type tree_prede�essor(const node_ptr_type node) {
             if ( !isNull(node->get_left()) )  {
                return tree_maximum(node->get_right());
             }

             // �� ��� ��� ���� �� ����������� �� ����� �����...
             // � ���� ���� ����������
             node_ptr_type parent_node = node->get_parent();
             node_ptr_type current_node = node;

             while( !isNull(parent_node) && parent_node->get_left() == current_node) {
                current_node = parent_node;
                parent_node = parent_node->get_parent();
             }

             return parent_node;
          }


          void insertFixup(node_ptr_type z) {

              while(z->get_parent()->get_color() == RED) {

                  node_ptr_type zp = z->get_parent();

                  node_ptr_type zpp = zp->get_parent();

                  if ( zp == zpp->get_left() ) { // if father is left child of it's grandfather 
                      
                      node_ptr_type zu = zpp->get_right(); // 'right' uncle

                      if (zu->get_color() == RED) { // case 1. red uncle
                        
                        // we know that z.p.p is black. Otherwise prop 4 is violated in z.p.p
                        // recolor z. parent and uncle into the black and z.p.p into the red
                        zp->set_color(BLACK);
                        zu->set_color(BLACK);
                        zpp->set_color(RED);
                        z = z->get_parent()->get_parent();

                      } else {

                          if ( z == zp->get_right() ) {  // case 2. z's uncle y is black and z is a right child
                              z = zp;
                              zp = z->get_parent();
                              zpp = zp->get_parent();
                              leftRotate(z);
                          }

                          // case 3: z's uncle is black is z is a left child
                          zp->set_color(BLACK);
                          zpp->set_color(RED);
                          rightRotate(z);
                      } 


                  } else { // father is right child of it's grandfather. just change left and right

                      node_ptr_type zu = zpp->get_left(); // 'left' uncle

                      if (zu->get_color() == RED) { // case 1. red uncle

                          // we know that z.p.p is black. Otherwise prop 4 is violated in z.p.p
                          // recolor z. parent and uncle into the black and z.p.p into the red
                          zp->set_color(BLACK);
                          zu->set_color(BLACK);
                          zpp->set_color(RED);
                          z = zpp;
                      } else {
                          if ( z == zp->get_left() ) {  // case 2. z's uncle y is black and z is a right child
                              z = zp;
                              zp = z->get_parent();
                              zpp = zp->get_parent();
                              rightRotate(z);
                          }

                          // case 3: z's uncle is black is z is a left child
                          zp->set_color(BLACK);
                          zpp->set_color(RED);
                          leftRotate(z);
                      } 
                  }
              }

              m_pRoot->set_color(BLACK);
          }

          bool isNull(node_ptr_type n) {
              return n.get() == NULL_NODE.get();
          }

          void insert(node_ptr_type node) {
         
             node_ptr_type current_node = m_pRoot; 
             node_ptr_type parent_node = NULL_NODE;  // will point to parent node

             while ( !isNull(current_node) )    {
                parent_node = current_node;
                if (node->get_data() < current_node->get_data()) {
                   current_node = current_node->get_left();
                } else {
                   current_node = current_node->get_right();
                }
             }

             node->set_parent(parent_node);

             if ( isNull(parent_node) ) { // empty tree
                m_pRoot = node;
             } else if ( node->get_data() < parent_node->get_data() ) {
                parent_node->set_left(node);
             } else {
                parent_node->set_right(node);
             }

             node->set_left(NULL_NODE);
             node->set_right(NULL_NODE);
             node->set_color(RED);
             insertFixup(node);
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


//         void deleteNode(node_ptr_type z) {
// 
//             if ( isNull( z->get_left() ) ) { // case a
//                 transplant( z, z->get_right() );
//             } else if ( isNull(z->get_right() ) ) { // case b
//                 transplant( z, z->get_left() );
//             } else {
//                 // find predecessor
//                 node_ptr_type y = tree_minimum( z->get_right() );
// 
//                 // case d predecessor is right child of z
//                 if ( y->get_parent() != z ) {
//                      transplant( y, y->get_right() );
// 
//                      y->set_right( z->get_right() );
//                      y->get_right()->set_parent( y );
//                 }
// 
//                 transplant( z, y );
//                 y->set_left( z->get_left() );
//                 y->get_left()->set_parent( y );
//             }
//         }
	private:
		node_ptr_type m_pRoot;
	};

}