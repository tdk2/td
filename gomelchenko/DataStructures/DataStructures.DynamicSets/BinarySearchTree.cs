using System;

namespace DataStructures.DynamicSets
{
    /// <summary>
    /// Represents binary-search tree
    /// </summary>
    /// <typeparam name="TKey">The type of the key.</typeparam>
    /// <typeparam name="TData">The type of the data.</typeparam>
    public class BinarySearchTree<TKey, TData> where TKey : IEquatable<TKey>, IComparable<TKey>
    {
        public BinaryTreeNode<TKey, TData> Root { get; private set; }

        public void Insert(BinaryTreeNode<TKey, TData> node)
        {
            var trackNode = Root;
            BinaryTreeNode<TKey, TData> parent = null;

            while (trackNode != null)
            {
                parent = trackNode;

                if (node.Key.Equals(trackNode.Key))
                {
                    var isMoveToLeft = !trackNode.IsLastEqualMovedToLeft;
                    trackNode.ToggleLastMove();
                    trackNode = isMoveToLeft ? trackNode.Left : trackNode.Right;
                }
                else
                {
                    trackNode = node.Key.CompareTo(trackNode.Key) < 0 ? trackNode.Left : trackNode.Right;    
                }
            }

            node.Parent = parent;
            
            if (parent == null)
            {
                Root = node;
            }
            else
            {
                bool isMoveToLeft;
                if (node.Key.Equals(parent.Key))
                {
                    isMoveToLeft = parent.IsLastEqualMovedToLeft;
                }
                else
                {
                    isMoveToLeft = node.Key.CompareTo(parent.Key) < 0;
                }

                if (isMoveToLeft)
                {
                    parent.Left = node;
                }
                else
                {
                    parent.Right = node;
                }
            }
        }

        /// <summary>
        /// Deletes the specified node.
        /// </summary>
        /// <param name="node">The node.</param>
        public void Delete(BinaryTreeNode<TKey, TData> node)
        {
            if (node.Left == null)
            {
                Transplant(node, node.Right);
            }
            else if (node.Right == null)
            {
                Transplant(node, node.Left);
            }
            else
            {
                var rightMinimum = Minimum(node.Right);
                if (rightMinimum.Parent != node)
                {
                    Transplant(rightMinimum, rightMinimum.Right);
                    rightMinimum.Right = node.Right;
                    rightMinimum.Right.Parent = rightMinimum;
                }

                rightMinimum.Left = node.Left;
                rightMinimum.Left.Parent = rightMinimum;
            }
        }

        /// <summary>
        /// Searches the node with the specified key.
        /// </summary>
        /// <param name="key">The key.</param>
        /// <returns>The proper node</returns>
        public Element<TKey, TData> Search(TKey key)
        {
            var node = Root;
            while (node != null && node.Key.Equals(key))
            {
                node = (node.Key.CompareTo(key) < 0) ? node.Left : node.Right;
            }

            return node;
        }

        /// <summary>
        /// Returns minimum of the tree
        /// </summary>
        /// <returns>The minimum node of the tree</returns>        
        public BinaryTreeNode<TKey, TData> Minimum()
        {
            return Minimum(Root);
        }

        /// <summary>
        /// Returns maximum of the tree
        /// </summary>
        /// <returns>The maximum node of the tree</returns>  
        public BinaryTreeNode<TKey, TData> Maximum()
        {
            return Maximum(Root);
        }

        /// <summary>
        /// Successors of the specified node.
        /// </summary>
        /// <param name="node">The node.</param>
        /// <returns>The successor node</returns>
        public BinaryTreeNode<TKey, TData> Successor(BinaryTreeNode<TKey, TData> node)
        {
            if (Root.Right != null)
            {
                return Minimum(Root.Right);
            }

            var parent = node.Parent;
            var trackNode = node;

            while (parent != null && trackNode == parent.Right)
            {
                trackNode = parent;
                parent = parent.Parent;
            }

            return parent;
        }

        /// <summary>
        /// Predecessors of the specified node.
        /// </summary>
        /// <param name="node">The node.</param>
        /// <returns>The predecessor</returns>
        public BinaryTreeNode<TKey, TData> Predecessor(BinaryTreeNode<TKey, TData> node)
        {
            if (Root.Left != null)
            {
                return Maximum(Root.Right);
            }

            var parent = node.Parent;
            var trackNode = node;

            while (parent != null && trackNode == parent.Left)
            {
                trackNode = parent;
                parent = parent.Parent;
            }

            return parent;
        }

        /// <summary>
        /// Iterates the tree according to "in order".
        /// </summary>
        /// <param name="action">The action.</param>
        public void IterateInOrder(Action<BinaryTreeNode<TKey, TData>> action)
        {
            IterateInOrder(Root, action);
        }

        /// <summary>
        /// Returns minimum of the subtree rooted by provided node
        /// </summary>
        /// <param name="root">The root.</param>
        /// <returns>The minimum node of the subtree</returns>
        private static BinaryTreeNode<TKey, TData> Minimum(BinaryTreeNode<TKey, TData> root)
        {
            var node = root;
            while (node != null)
            {
                node = node.Left;
            }

            return node;
        }

        /// <summary>
        /// Returns maximum of the subtree rooted by provided node
        /// </summary>
        /// <param name="root">The root.</param>
        /// <returns>The maximum node of the subtree</returns>
        private static BinaryTreeNode<TKey, TData> Maximum(BinaryTreeNode<TKey, TData> root)
        {
            var node = root;
            while (node != null)
            {
                node = node.Right;
            }

            return node;
        }

        /// <summary>
        /// Replaces the specified source with the specified target
        /// </summary>
        /// <param name="source">The source.</param>
        /// <param name="target">The target.</param>
        private void Transplant(BinaryTreeNode<TKey, TData> source, BinaryTreeNode<TKey, TData> target)
        {
            if (source.Parent == null)
            {
                Root = target;
            }
            else if (source == target.Parent.Left)
            {
                source.Parent.Left = target;
            }
            else
            {
                source.Parent.Right = target;
            }

            if (target != null)
            {
                target.Parent = source.Parent;
            }
        }

        public void IterateInOrder(BinaryTreeNode<TKey, TData> node, Action<BinaryTreeNode<TKey, TData>> action)
        {
            if (node == null) return;

            IterateInOrder(node.Left, action);
            action(node);
            IterateInOrder(node.Right, action);
        }
    }
}
