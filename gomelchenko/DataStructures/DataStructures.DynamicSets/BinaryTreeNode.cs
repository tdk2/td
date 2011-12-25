using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DataStructures.DynamicSets
{
    /// <summary>
    /// Represents a node in a binary tree
    /// </summary>
    /// <typeparam name="TKey">The type of the key.</typeparam>
    /// <typeparam name="TData">The type of the data.</typeparam>
    public class BinaryTreeNode<TKey, TData> : TreeNode<TKey, TData>
    {
        public BinaryTreeNode(TKey key, TData data)
        {
            Key = key;
            Data = data;
        }

        public BinaryTreeNode<TKey, TData> Parent { get; internal set; } 
        
        public BinaryTreeNode<TKey, TData> Left { get; internal set; }

        public BinaryTreeNode<TKey, TData> Right { get; internal set; }

        internal bool IsLastEqualMovedToLeft { get; set; }

        public void ToggleLastMove()
        {
            IsLastEqualMovedToLeft ^= true;
        }
    }
}
