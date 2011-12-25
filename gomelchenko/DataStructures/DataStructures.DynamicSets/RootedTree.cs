using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace DataStructures.DynamicSets
{
    /// <summary>
    /// Represents rooted tree
    /// </summary>
    /// <typeparam name="TKey">The type of the key.</typeparam>
    /// <typeparam name="TData">The type of the data.</typeparam>
    public abstract class RootedTree<TKey, TData> : Tree<TKey, TData> 
    {
        public TreeNode<TKey, TData> Root { get; protected set; } 
    }
}